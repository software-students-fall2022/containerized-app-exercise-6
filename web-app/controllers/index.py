import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response, session, flash
import datetime
import os

index_page = Blueprint( "index_page", __name__ )

app = Flask(__name__)
app.secret_key = "secret key"

client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")
db=client["Team6"]

def compute_percentage(docs):

    total=0

    count_array=[0,0,0,0,0,0,0,0]

    for doc in docs:

        total+=1

        count_array[doc['emotion']]+=1

    output=[0,0,0,0,0,0,0,0]

    for c in range(len(count_array)):

        output[c]=count_array[c]/total

    return output

def compute_mean(docs):

    total=0
    count = 0


    for doc in docs:

        
        count += 1

    output=total/count

    return output


def find_max(docs):

    count = 0

    count_array=[0,0,0,0,0,0,0,0]
    output=[]

    for doc in docs:

        count_array[doc['emotion']]+=1
        count += 1

    max = 0
    for c in range(len(count_array)):
        if (count_array[c] > max):
            max = count_array[c]


    for i in range(len(count_array)):
        if (count_array[i] == max):
            output.append(i)

    return output

@index_page.route('/')
def home():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    output=find_max(docs)

    for o in range(len(output)):
            print("The max numbr of emotion is "+str(output[o]))

    return render_template('/photo/test_result.html', docs = output)

    #return render_template('/photo/photo_demo.html')

@index_page.route("/gallery")
def gallery():
    return ""

'''
@index_page.route('/upload', methods=['POST'])
def upload():
    photo = request.form.get('photo')
    #machine learning stuff here
    #save image to Mongodb

    doc = {
            "Image": photo,
            "created_at": datetime.datetime.utcnow()
    }
    db.Image.insert_one(doc) # insert a new document
    docs = db.Image.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    return render_template('/photo/photo_response_demo.html', imgBase64 = photo)
'''
