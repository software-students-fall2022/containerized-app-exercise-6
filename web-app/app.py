import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for, make_response, session, flash
import datetime
import os

app = Flask(__name__)
app.secret_key = "secret key"

client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")
db=client["Team6"]

app.config.from_pyfile( "config/base_setting.py" )

@app.route('/')
def home():
    return render_template('/photo/photo_demo.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.form.get('photo')
    #machine learning stuff here
    #save image to Mongodb
    '''
    doc = {
            "Image": photo,
            "created_at": datetime.datetime.utcnow()
    }
    db.Image.insert_one(doc) # insert a new document
    docs = db.Image.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp
    '''
    return render_template('/photo/photo_response_demo.html', imgBase64 = photo)

app.run(debug = True)