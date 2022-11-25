import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response, session, flash
import datetime
import os
import sys

index_page = Blueprint( "index_page", __name__ )

app = Flask(__name__)
app.secret_key = "secret key"

client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")
db=client["Team6"]

def compute_percentage():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    total=0

    count_array=[0,0,0,0,0,0,0,0]

    for doc in docs:

        total+=1

        count_array[doc['emotion']]+=1

    output=[0,0,0,0,0,0,0,0]

    for c in range(len(count_array)):

        output[c]=count_array[c]/total

    return output

def compute_median():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    total=0

    count_array=[0,0,0,0,0,0,0,0]

    for doc in docs:

        total+=1

        count_array[doc['emotion']]+=1

    index=total / 2

    count=0

    for c in count_array:

        if (index-c<=0):

            output=count

        else:

            index=index-c

            count+=1

    return output

def compute_mean():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    total=0

    count = 0

    for doc in docs:

        total+=doc['emotion']

        count += 1

    output=total/count

    return output


def find_max():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

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

def find_min():

    docs = db.result.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    count = 0

    count_array=[0,0,0,0,0,0,0,0]
    output=[]

    for doc in docs:

        count_array[doc['emotion']]+=1
        count += 1

    min = sys.maxsize
    for c in range(len(count_array)):
        if (count_array[c] < min):
            min = count_array[c]

    for i in range(len(count_array)):
        if (count_array[i] == min):
            output.append(i)

    return output

@index_page.route('/')
def home():

    percentage=compute_percentage()

    mean=compute_mean()

    median=compute_median()

    MaxNumber=find_max()

    MinNumber=find_min()

    dictionary={
        "Percentage":percentage,
        "Mean":mean,
        "Median":median,
        "MaxNumber of emotion":MaxNumber,
        "MinNumber of emotion": MinNumber
    }

    return render_template('/photo/test_result.html', docs = dictionary)

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
