import ast
import json
import os
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
        os.makedirs(PATH, exist_ok=True)  # Skapa mappen om den inte finns
        if image and allowed_file(image.filename):
            # Retrieve result
            response = evaluate_image()
            data = json.loads(response.get_data(as_text=True))
            accuracy = data['accuracy']
            animal = data['animal']
            return render_template("image/animals.html", accuracy=accuracy, animal=animal)
    return render_template("image/animals.html", file = "", accuracy = "", animal = "")