# Deploy Keras Model with Flask as Web App in 10 Minutes

> A pretty and customizable web app to deploy your DL model with ease


## Getting started in 10 minutes

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
$ cd keras-flask-deploy-webapp

# 2. Build Docker image
$ docker build -t keras_flask_app .

# 3. Run!
$ docker run -it --rm -p 5000:5000 keras_flask_app
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

