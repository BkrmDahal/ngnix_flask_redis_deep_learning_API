.. ngnix-flask-redis-deep-learning-API, created by
   sphinx-quickstart on Thu Aug  9 13:47:11 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to ngnix-flask-redis-deep-learning-API's documentation!
===============================================================

Scalable deep learning model with Ngnix, flask, redis and docker.

ngnix-flask-redis-deep-learning-API
------------------------------------

.. code-block:: json

    +-------------+       +------------+         +--------------------------------+     +-----------+
    |             |       |            |         |                                |     |           |
    |    nginx    +-------+  gunicorn  +---------+  flask deep learning API app   +-----+   redis   |
    |             |       |            |         |                                |     |           |
    +-------------+       +------------+         +--------------------------------+     +-----------+


Environments setup
^^^^^^^^^^^^^^^^^^^^^

1. Please install `docker` and `docker-compose`.  
> Use ``install_docker.sh``

.. code-block:: bash 

    # install docker file
    sudo apt remove docker docker-engine docker.io
    sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo apt-key fingerprint 0EBFCD88

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt update
    sudo apt install docker-ce -y

    # install docker compose
    sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

    # install docker as sudo for user so  that we dont have to type sudo before docker
    # sudo usermod -aG docker $<<USERNAME>>


2. Run docker-compose

.. code-block:: bash 

    docker-compose up -d


Packages:
=========

.. toctree::
   :maxdepth: 2

   app


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

**********
References
**********

.. target-notes::

.. -`Deep learning in production with Keras, Redis, Flask, and Apache`: https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/
.. -`Github: docker-compose-flask`: https://github.com/xiaopeng163/docker-compose-flask

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
