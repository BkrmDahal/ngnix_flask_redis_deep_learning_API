"""
Make flask server to preprocess the the image and add queue to
``redis`` database. Then check if predication is saved to ``redis`` database,
once predication is saved, return the predication json.
"""

import os
import sys
sys.path.insert(0, os.path.abspath('app/'))
sys.path.insert(0, os.path.abspath('../'))

from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import settings
import helpers
import flask
import redis
import uuid
import time
import json
import io

# initialize our Flask application and Redis server
app = flask.Flask(__name__)
db = redis.StrictRedis(host=settings.REDIS_HOST,
	port=settings.REDIS_PORT, db=settings.REDIS_DB)

def prepare_image(image, target):
	"""
	Preprocess the image for predication

	Args:
		images:``array``
			Array from image
		target:``array``
			shape of image for reshape

	Return:
		Preprocesses image array

	"""

	# if the image mode is not RGB, convert it
	if image.mode != "RGB":
		image = image.convert("RGB")

	# resize the input image and preprocess it
	image = image.resize(target)
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)
	image = imagenet_utils.preprocess_input(image)

	# return the processed image
	return image

@app.route("/")
def homepage():
	"""
	Endpoint for homepage
	"""
	return "Welcome to the PyImageSearch Keras REST API!"

@app.route("/predict", methods=["POST"])
def predict():
	"""
	Predicat the image class.

	Send the image as post request.

		.. code-block:: bash

    		   curl -X POST -F image=@jemma.png 'http://localhost/predict'

	Return:
		json of classes from predication

		.. code-block:: json

			{
			"predictions": [
				{
				"label": "beagle", 
				"probability": 0.9461532831192017
				}, 
				{
				"label": "bluetick", 
				"probability": 0.031958963721990585
				}, 
				{
				"label": "redbone", 
				"probability": 0.0066171870566904545
				}, 
				{
				"label": "Walker_hound", 
				"probability": 0.003387963864952326
				}, 
				{
				"label": "Greater_Swiss_Mountain_dog", 
				"probability": 0.0025766845792531967
				}
			], 
			"success": true
			}

	"""
	# initialize the data dictionary that will be returned from the
	# view
	data = {"success": False}

	# ensure an image was properly uploaded to our endpoint
	if flask.request.method == "POST":
		if flask.request.files.get("image"):
			# read the image in PIL format and prepare it for
			# classification
			image = flask.request.files["image"].read()
			image = Image.open(io.BytesIO(image))
			image = prepare_image(image,
				(settings.IMAGE_WIDTH, settings.IMAGE_HEIGHT))

			# ensure our NumPy array is C-contiguous as well,
			# otherwise we won't be able to serialize it
			image = image.copy(order="C")

			# generate an ID for the classification then add the
			# classification ID + image to the queue
			k = str(uuid.uuid4())
			image = helpers.base64_encode_image(image)
			d = {"id": k, "image": image}
			db.rpush(settings.IMAGE_QUEUE, json.dumps(d))

			# keep looping until our model server returns the output
			# predictions
			while True:
				# attempt to grab the output predictions
				output = db.get(k)

				# check to see if our model has classified the input
				# image
				if output is not None:
					# add the output predictions to our data
					# dictionary so we can return it to the client
					output = output.decode("utf-8")
					data["predictions"] = json.loads(output)

					# delete the result from the database and break
					# from the polling loop
					db.delete(k)
					break

				# sleep for a small amount to give the model a chance
				# to classify the input image
				time.sleep(settings.CLIENT_SLEEP)

			# indicate that the request was a success
			data["success"] = True

	# return the data dictionary as a JSON response
	return flask.jsonify(data)

# for debugging purposes, it's helpful to start the Flask testing
# server (don't use this for production
if __name__ == "__main__":
	print("* Starting web service...")
	app.run()
