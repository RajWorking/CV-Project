import json
import os

from colorize import colorize, encode_image

from flask import Flask, request
from flask_cors import CORS

import cv2
import numpy as np

app = Flask(__name__)
app.config.update(SECRET_KEY=os.getenv('SECRET', 'secret'))

CORS(app, resources={r"/*": {"origins": "*"}})


def to_json(payload, status=200):
    return json.dumps(payload, indent=4, sort_keys=True, default=str), status, {
        'content-type': 'application/json'}


@app.route('/a', methods=['POST', 'GET'])
def get_prediction():

    # data = request.get_json()

    # print(request.files['file'])

    #read image file string data
    filestr = request.files['file'].read()
    #convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)


    # model_type = data['model']
    # temp = data['temp']

    input_image, output_img = colorize(img)

    obj = {
        'input': encode_image(input_image),
        'output': encode_image(output_img),
    }
    
    # return to_json(obj)

    return to_json({'hi': 'hi'})

@app.route('/', methods=['GET'])
def hello():

    return to_json({'hello': 'hello'})

if __name__ == '__main__':
    app.run(threaded=True, port=8000, debug=True)



