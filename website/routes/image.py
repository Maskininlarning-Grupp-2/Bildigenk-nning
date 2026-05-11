import ast
import json
import os.path
from flask import Blueprint, request, redirect, flash, url_for, render_template
from werkzeug.utils import secure_filename

from website.routes.api import evaluate_image
from website.test import allowed_file

image_bp = Blueprint('image', __name__, url_prefix='/image')

@image_bp.route('/animals', methods=['GET', 'POST'])
def animals():
    if request.method == 'POST':
        image = request.files['file']
        PATH = './website/static/assets/images/temp/'
        if image and allowed_file(image.filename):

            # Retrieve result
            response = evaluate_image()
            data = response.get_data().decode('utf-8').replace('true', 'True')
            data = eval(data)
            accuracy = data['accuracy']
            animal = data['animal']
            filename = secure_filename(image.filename)
            if len(os.listdir(PATH)) > 0:
                for file in os.listdir(PATH):
                    os.remove(os.path.join(PATH, file))
            image.seek(0)
            image.save(os.path.join(PATH, filename))
            return render_template("image/animals.html", file=os.path.join('/static/assets/images/temp/', filename), accuracy=accuracy, animal=animal)
    return render_template("image/animals.html", file = "", accuracy = "", animal = "")