.. email documentation master file, created by
   sphinx-quickstart on Thu Aug  9 13:47:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ngnix-flask-redis-deep-learning-API's documentation!
===============================================================

Scaleable deep learning model with Ngnix, flask, redis and docker.

Details:

.. toctree::
   :maxdepth: 2

   ngnix_flask_redis_deep_learning_API


Input
-----

.. code-block:: bash

    curl -X POST -F image=@jemma.png 'http://localhost/predict'

Output
------

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



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
