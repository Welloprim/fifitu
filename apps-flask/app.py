import os
import sys

# Flask
from flask import Flask, redirect, url_for, request, render_template, Response, jsonify, redirect
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import requests, json
# Some utilites
import numpy as np
from util import base64_to_pil


# Declare a flask app
app = Flask(__name__)


# You can use pretrained model from Keras
# Check https://keras.io/applications/
from keras.applications.mobilenet_v2 import MobileNetV2

#print('Model loaded. Check http://127.0.0.1:5000/')


# Model saved with Keras model.save()
MODEL_PATH = 'models/model.h5'
#Classes
label_class = ['Hauts & Tee-shirts','Pantalons','Sweats et sweats à capuche','Robes','Manteaux & vestes','Sandales','Chemises','Baskets','Sacs','Bottines','Jupes']

# Load your own trained model
model = load_model(MODEL_PATH)
#model = MobileNetV2(weights='imagenet')
model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')


def model_predict(img, model):
    img = img.resize((96,96))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    x = preprocess_input(x, mode='tf')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the image from post request
        img = base64_to_pil(request.json)

        # Save the image to ./uploads
        # img.save("./uploads/image.png")

        # Make prediction
        preds = model_predict(img, model)

        # Process the result
        # find the index of the class with maximum score
        pred = preds.argmax(axis=-1)

        # print the label of the class with maximum score
        result = str(label_class[pred[0]]) # Convert to string
        result = result.replace('_', ' ').capitalize()
        # Serialize the result, you can add additional fields
        return jsonify(result=result)

    return None

def print_json(obj):
    """Print the object as json"""
    print(json.dumps(obj, sort_keys=True, indent=2, separators=(',', ': ')))



if __name__ == '__main__':
    #app.run(port=5002, debug=True, threaded=True)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5050), app)
    http_server.serve_forever()
