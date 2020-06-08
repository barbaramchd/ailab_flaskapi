from app import app
from app import q
from app import r
from PIL import Image
import time
from app.tasks import create_image_set

from flask import render_template, request, redirect, flash, url_for

import os
import secrets

## ROUTES ##

## RESIZING IMAGES ##

app.config["SECRET_KEY"] = "yoshi"
app.config["IMAGE_UPLOADS"] = 'C:\\Users\\barba\\Desktop\\app\\app\\static\\img\\uploads'

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['GET','POST'])
def upload():


    message = None

    if request.method == 'POST':

        if request.files:

            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print("hhii")

            q.enqueue(create_image_set, image.filename)

            print("Image saved")

            message = f"/image/{image.filename.split('.')[0]}"

            return redirect(request.url)
    
    return render_template('success.html', message=message)   


@app.route('/images/<img>')
def view_image(dir, img):
    return render_template('success.html', dir=dir, img=img)
