from crypt import methods
from flask import Flask, request, jsonify
from torch_utils import transform_image, get_prediction

app = Flask(__name__)
# export FLASK_APP=main.py  export FLASK_ENV=development

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # xxx.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/predict', methods=['POST'])
def predict():
  if request.method == 'POST':
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({'error': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'error': 'format not supported'})

        try:
            img_bytes = file.read()
            tensor = transform_image(img_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item() + 1, 'class_name': str(prediction.item()+1)}
            return jsonify(data)
        except:
            return jsonify({'error': 'error during prediction'})