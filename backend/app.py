import json
import os

from colorize import colorize, encode_image

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
app.config.update(SECRET_KEY=os.environ.get('SECRET'))

CORS(app, resources={r"/*": {"origins": "*"}})


def to_json(payload, status=200):
    return json.dumps(payload, indent=4, sort_keys=True, default=str), status, {
        'content-type': 'application/json'}

@app.route('/api/predict', methods=['GET'])
def get_prediction():

    data = request.get_json()

    image_bytes = data['img']
    model_type = data['model']
    temp = data['temp']

    input_image, output_img = colorize(bytearray(image_bytes), model_type, temp)

    obj = {
        'input': encode_image(input_image),
        'output': encode_image(output_img),
    }
    
    return to_json(obj)

if __name__ == '__main__':
    app.run(threaded=True, port=8000, debug=True)
