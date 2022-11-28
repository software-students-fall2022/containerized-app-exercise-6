import os
from os.path import dirname, join
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controllers import index
#import index
import pymongo

def test_percentage():

    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")

    db=client["Team6"]

    output=index.compute_percentage(db.TestImage)

    expected_result=[0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.1111111111111111]

    for out in range(len(output)):

        assert output[out]==expected_result[out], "The output percentage is not correct"

def test_find_min():

    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")

    db=client["Team6"]

    output=index.find_min(db.TestImage)

    expected_result=['Anger', 'Contempt', 'Disgust', 'Fear', 'Neutral', 'Sadness', 'Surprise']
    

    for out in range(len(output)):

        assert output[out]==expected_result[out], "The output min is not correct"

def test_find_max():

    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")

    db=client["Team6"]

    output=index.find_max(db.TestImage)

    expected_result=['Happiness']

    for out in range(len(output)):

        assert output[out]==expected_result[out], "The output max is not correct"

def test_find_non_existing_collection():
    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")

    db=client["Team6"]
    
    output=index.compute_percentage(db.NonExist)
    
    assert output == [], "The output is not correct"
