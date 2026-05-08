import os.path
import shutil

from flask import Blueprint, request, redirect, flash, url_for, render_template
from werkzeug.utils import secure_filename

from website.test import allowed_file

image_bp = Blueprint('image', __name__, url_prefix='/image')

@image_bp.route('/animals', methods=['GET', 'POST'])
def animals():
    if request.method == 'POST':
        # call function here
        print("This will recieve data from the model eventually")

        image = request.files['file']
        PATH = './website/static/assets/images/temp/'
        if image and allowed_file(image.filename):
            print("This will recieve data from the model eventually")
            filename = secure_filename(image.filename)
            if len(os.listdir(PATH)) > 0:
                for file in os.listdir(PATH):
                    os.remove(os.path.join(PATH, file))
            image.save(os.path.join(PATH, filename))
            return render_template("image/animals.html", file=os.path.join('../static/assets/images/temp/', filename))
    return render_template("image/animals.html", file ="")