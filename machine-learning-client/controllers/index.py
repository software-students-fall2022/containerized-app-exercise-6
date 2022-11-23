import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response, session, flash
import datetime
import os
import face_recognition
import os
import matplotlib.pyplot as plt 
from PIL import Image
from io import BytesIO
import base64
import re

index_page = Blueprint( "index_page", __name__ )

app = Flask(__name__)
app.secret_key = "secret key"

client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")
db=client["Team6"]

@index_page.route('/')
def home():
    return render_template('/photo/photo_demo.html')

@index_page.route("/gallery")
def gallery():
    return ""

@index_page.route('/upload', methods=['POST'])
def upload():
    photo = request.form.get('photo')
    
    
    #print(photo)
    #machine learning stuff here
    #save image to Mongodb
    
    
    #transform photo to bytes for machine learning
    image_data = re.sub('^data:image/.+;base64,', '', photo)
    image = face_recognition.load_image_file(BytesIO(base64.b64decode(image_data)))
    face_locations = face_recognition.face_locations(image) 
    
    #test code, can be removed
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        top, right, bottom, left = face_location
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # get face
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        # jupyter 绘图
        # pil_image.show()
        plt.imshow(pil_image)
        plt.axis('off')    
        plt.show()
    
    """
    doc = {
            "Image": photo,
            "created_at": datetime.datetime.utcnow()
    }
    db.Image.insert_one(doc) # insert a new document
    docs = db.Image.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp
    """
    return render_template('/photo/photo_response_demo.html', imgBase64 = photo)

