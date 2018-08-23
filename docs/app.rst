app package
===========

app.helpers module
------------------

Helper funcation for preprocessing

.. automodule:: app.helpers
    :members:
    :undoc-members:
    :show-inheritance:

app.run\_model\_server module
-----------------------------

Run deep learning model which predication the classes and update predication 
to ``redis`` database with id and json

.. automodule:: app.run_model_server
    :members:
    :undoc-members:
    :show-inheritance:

app.run\_web\_server module
---------------------------

Make flask server to preprocess the the image and queue to
``redis`` database. 

Check if predication is saved in ``redis`` data,
Once predication is saved, output the predication json

.. automodule:: app.run_web_server
    :members:
    :undoc-members:
    :show-inheritance:

app.settings module
-------------------

Environment variables for app

.. code-block:: bash

    # initialize Redis connection settings
    REDIS_HOST = "redis"
    REDIS_PORT = 6379
    REDIS_DB = 0

    # initialize constants used to control image spatial dimensions and
    # data type
    IMAGE_WIDTH = 224
    IMAGE_HEIGHT = 224
    IMAGE_CHANS = 3
    IMAGE_DTYPE = "float32"

    # initialize constants used for server queuing
    IMAGE_QUEUE = "image_queue"
    BATCH_SIZE = 32
    SERVER_SLEEP = 0.25
    CLIENT_SLEEP = 0.25

.. automodule:: app.settings
    :members:
    :undoc-members:
    :show-inheritance:

app.simple\_request module
--------------------------

Simple post request using request library

.. automodule:: app.simple_request
    :members:
    :undoc-members:
    :show-inheritance:

app.stress\_test module
-----------------------

Stress test for server

.. code-block:: bash

	python stress_test.py

.. automodule:: app.stress_test
    :members:
    :undoc-members:
    :show-inheritance:

