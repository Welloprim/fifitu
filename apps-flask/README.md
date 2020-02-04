# Keras Model with Flask

> A pretty and customizable web app to deploy your DL model with ease


## Getting started

- Clone this repo 
- Install requirements
- Run the script
- Go to http://localhost:5000
- Done! :tada:

:point_down: Screenshot:


## Run with Docker

With **[Docker](https://www.docker.com)**, you can quickly build and run the entire application in minutes :whale:

```shell
# 1. First, clone the repo
$ git clone https://github.com/welloprim/fifitu/apps-flask.git
$ cd apps-flask

# 2. Build Docker image
$ docker build -t apps-flask .

# 3. Run!
$ docker run -it --rm -p 5000:5000 apps-flask
```

Open http://localhost:5000 and wait till the webpage is loaded.

## Local Installation

It's easy to install and run it on your computer.

```shell
# 1. First, clone the repo
$ git clone https://github.com/mtobeiyf/keras-flask-deploy-webapp.git
$ cd keras-flask-deploy-webapp

# 2. Install Python packages
$ pip install -r requirements.txt

# 3. Run!
$ python app.py
```

Open http://localhost:5000 and have fun. :smiley:

  
### Run the app

Run the script and hide it in background with `tmux` or `screen`.
```
$ python app.py
```

