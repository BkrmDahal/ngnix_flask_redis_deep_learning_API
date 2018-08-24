# Ngnix flask redis deep learning API
[![Documentation Status](https://readthedocs.org/projects/ngnix-flask-redis-deep-learning-api/badge/?version=latest)](https://ngnix-flask-redis-deep-learning-api.readthedocs.io/en/latest/?badge=latest)

Scalable deep learning model with Ngnix, flask, redis and docker. [Here is Documentation](https://ngnix-flask-redis-deep-learning-api.readthepngdocs.io/en/latest/)
![ngnix_flask_redis_deep_learning_API](https://i.imgur.com/5SaAys4.png)

```

+-------------+       +------------+      +------------------------+     +-----------+
|             |       |            |      |                        |     |           |
|    nginx    +-------+  gunicorn  +------+  flask deep learning   +-----+   redis   |
|             |       |            |      |       API app          |     |           |
+-------------+       +------------+      +------------------------+     +-----------+

```

## Environments setup

1. Please install `docker` and `docker-compose`.  
> Use ``install_docker.sh``

```sh
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
```

2. Run docker-compose

```sh
docker-compose up -d
```

### Inspire by 
[Deep learning in production with Keras, Redis, Flask, and Apache](https://www.pyimagesearch.com/2018/02/05/deep-learning-production-keras-redis-flask-apache/)  
[Github: docker-compose-flask](https://github.com/xiaopeng163/docker-compose-flask)
