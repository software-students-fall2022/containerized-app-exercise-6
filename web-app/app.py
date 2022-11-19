import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for, make_response, session, flash
import datetime


app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def home():
    return render_template('photo_demo.html')

@app.route('/upload', methods=['POST'])
def upload():
    photo = request.form.get('photo')
    print(photo)
    return render_template('photo_response_demo.html', imgBase64 = photo)

app.run(debug = True)