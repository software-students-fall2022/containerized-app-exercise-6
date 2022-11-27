import pymongo
from bson.objectid import ObjectId
from flask import Flask, render_template, request, Blueprint, redirect, url_for, make_response, session, flash
import datetime
import os
import sys

index_page = Blueprint( "index_page", __name__ )

app = Flask(__name__)
app.secret_key = "secret key"

def is_docker():
    path = '/proc/self/cgroup'
    return (
        os.path.exists('/.dockerenv') or
        os.path.isfile(path) and any('docker' in line for line in open(path))
    )
if(is_docker()):
    client = pymongo.MongoClient("db", 27017)
else:
    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")


db=client["Team6"]

def compute_percentage():

    emotion_dict={
        'Anger':0,
        'Contempt':1,
        'Disgust':2,
        'Fear':3,
        'Happiness':4,
        'Neutral':5,
        'Sadness':6,
        'Surprise':7
    }

    docs = db.TestImage.find({}).sort("created_at", -1).limit(1) # sort in descending order of created_at timestamp

    for doc in docs:
        
        docs_id=doc['_id']

        total=0

        count_array=[0,0,0,0,0,0,0,0]

        for result in doc['results']:

            total+=1
                
            emotion=emotion_dict[result['emotion']]

            count_array[emotion]+=1

        output=[0,0,0,0,0,0,0,0]

        for c in range(len(count_array)):

            output[c]=count_array[c]/total

        key_list = list(emotion_dict.keys())

        val_list = list(emotion_dict.values())

        output_dict={}

        for n in range(len(output)):

            position = val_list.index(n)

            output_dict[key_list[position]]=output[n]

        db.TestImage.update({"_id" :ObjectId(docs_id)},{"$set":{"Percentage":output_dict}})

    return output

def find_max():

    emotion_dict={
        'Anger':0,
        'Contempt':1,
        'Disgust':2,
        'Fear':3,
        'Happiness':4,
        'Neutral':5,
        'Sadness':6,
        'Surprise':7
    }

    docs = db.TestImage.find({}).sort("created_at", -1).limit(1)

    count_array=[0,0,0,0,0,0,0,0]
    output=[]

    for doc in docs:

        docs_id=doc['_id']

        for result in doc['results']:
            
            emotion=emotion_dict[result['emotion']]

            count_array[emotion]+=1

        max = 0
        for c in range(len(count_array)):
            if (count_array[c] > max):
                max = count_array[c]


        for i in range(len(count_array)):
            if (count_array[i] == max):
                output.append(i)
        
        key_list = list(emotion_dict.keys())
        val_list = list(emotion_dict.values())


        for j in range(len(output)):
            position = val_list.index(output[j])
            output[j] = key_list[position]

        db.TestImage.update({"_id" :ObjectId(docs_id)},{"$set":{"MaxEmotion":output}})

    return output

def find_min():

    emotion_dict={
        'Anger':0,
        'Contempt':1,
        'Disgust':2,
        'Fear':3,
        'Happiness':4,
        'Neutral':5,
        'Sadness':6,
        'Surprise':7
    }

    docs = db.TestImage.find({}).sort("created_at", -1).limit(1) # sort in descending order of created_at timestamp

    count_array=[0,0,0,0,0,0,0,0]
    output=[]

    for doc in docs:

        docs_id=doc['_id']

        for result in doc['results']:
            
            emotion=emotion_dict[result['emotion']]

            count_array[emotion]+=1

        min = sys.maxsize
        for c in range(len(count_array)):
            if (count_array[c] < min):
                min = count_array[c]

        for i in range(len(count_array)):
            if (count_array[i] == min):
                output.append(i)

        key_list = list(emotion_dict.keys())
        val_list = list(emotion_dict.values())


        for j in range(len(output)):
            position = val_list.index(output[j])
            output[j] = key_list[position]

        db.TestImage.update({"_id" :ObjectId(docs_id)},{"$set":{"MinEmotion":output}})

    return output

@index_page.route('/')
def home():
    
    percentage=compute_percentage()
    MaxNumber=find_max()
    MinNumber=find_min()

    docs = db.TestImage.find({}).sort("created_at", -1) # sort in descending order of created_at timestamp

    return render_template('/photo/test_result.html', docs = docs)
'''
    doc = {
            "original": 'photo',
            "results": [{"img":'img',"emotion":'Anger'},{"img":'img',"emotion":'Contempt'},{"img":'img',"emotion":'Disgust'},
            {"img":'img',"emotion":'Fear'},{"img":'img',"emotion":'Happiness'},{"img":'img',"emotion":'Neutral'},{"img":'img',"emotion":'Sadness'},
            {"img":'img',"emotion":'Happiness'},{"img":'img',"emotion":'Surprise'}]
        }

    db.TestImage.insert_one(doc)

    doc = {
            "original": 'photo',
            "results": [{"img":'img',"emotion":'Anger'},{"img":'img',"emotion":'Neutral'},
            {"img":'img',"emotion":'Fear'}, {"img":'img',"emotion":'Neutral'},{"img":'img',"emotion":'Sadness'}]
        }

    db.TestImage.insert_one(doc)
'''

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
