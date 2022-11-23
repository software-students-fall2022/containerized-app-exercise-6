import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response, session, flash
import datetime
import os
import face_recognition
import os
import matplotlib.pyplot as plt 
from PIL import Image, ImageDraw
from io import BytesIO
import base64
import re
import numpy

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


def face_detect(image_data):
    image = face_recognition.load_image_file(BytesIO(base64.b64decode(image_data)))
    face_locations = face_recognition.face_locations(image) 
    
    #test code, can be removed
    #print("I found {} face(s) in this photograph.".format(len(face_locations)))
    for face_location in face_locations:
        top, right, bottom, left = face_location
        #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # get face
        face_image = image[top:bottom, left:right]
        image = Image.fromarray(face_image)
      
        # pil_image.show()
        #plt.imshow(image)
        #plt.axis('off')    
        #plt.show()
   
    if(len(face_locations) > 0):
        buffer = BytesIO()
        image.save(buffer,format="PNG")                  
        myimage = buffer.getvalue()   
        myimage = "data:image/png;base64," + base64.b64encode(myimage).decode('utf-8')
        
        return myimage
    return None

def face_features(image_data):
    image = face_recognition.load_image_file(BytesIO(base64.b64decode(image_data)))
    face_landmarks_list = face_recognition.face_landmarks(image)
    
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)
    
    for face_landmarks in face_landmarks_list:
        for facial_feature in face_landmarks.keys():
            d.line(face_landmarks[facial_feature], width=5)

    if(len(face_landmarks_list) > 0):
        buffer = BytesIO()
        pil_image.save(buffer,format="PNG")                  
        myimage = buffer.getvalue()   
        myimage = "data:image/png;base64," + base64.b64encode(myimage).decode('utf-8')
        
        return myimage
    return None
    

def face_color(image_data):
    image = face_recognition.load_image_file(BytesIO(base64.b64decode(image_data)))
     
    face_landmarks_list = face_recognition.face_landmarks(image)

    pil_image = Image.fromarray(image)

    # 绘图
    for face_landmarks in face_landmarks_list:
        d = ImageDraw.Draw(pil_image, 'RGBA')

        # eyebrow
        d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
        d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

        # lip
        d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
        d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
        d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

        # eye
        d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

        # eye outline
        d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
        d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)
    
    
    if(len(face_landmarks_list) > 0):
        buffer = BytesIO()
        pil_image.save(buffer,format="PNG")                  
        myimage = buffer.getvalue()   
        myimage = "data:image/png;base64," + base64.b64encode(myimage).decode('utf-8')
        
        return myimage
    return None


@index_page.route('/upload', methods=['POST'])
def upload():
    photo = request.form.get('photo')
    
    
    #print(photo)
    #machine learning stuff here
    #save image to Mongodb
 
    
    #transform photo to bytes for machine learning
    image_data = re.sub('^data:image/.+;base64,', '', photo)
    
    """
    doc = {
            "Image": photo,
            "created_at": datetime.datetime.utcnow()
    }
    db.Image.insert_one(doc) # insert a new document
    docs = db.Image.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp
    """
    
    #img = face_detect(image_data)   
    img = face_features(image_data)
    #img = face_color(image_data)
    return render_template('/photo/photo_response_demo.html', imgBase64 = img)
    

