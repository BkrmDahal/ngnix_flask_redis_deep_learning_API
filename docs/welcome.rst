Welcome and setup
=================


Ngnix-flask-redis-deep-learning-API
------------------------------------

.. code-block:: json

    +-------------+       +------------+      +------------------------+     +-----------+
    |             |       |            |      |                        |     |           |
    |    nginx    +-------+  gunicorn  +------+  flask deep learning   +-----+   redis   |
    |             |       |            |      |       API app          |     |           |
    +-------------+       +------------+      +------------------------+     +-----------+


Environments setup
------------------

1. Please install `docker` and `docker-compose`.

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