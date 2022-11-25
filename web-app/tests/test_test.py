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

    output=index.compute_percentage()

    expected_result=[0,0.125,0.125,0.125,0.125,0.125,0.125,0.25]

    for out in range(len(output)):

        assert output[out]==expected_result[out], "The output percentage is not correct"

def test_find_min():

    client = pymongo.MongoClient("mongodb+srv://okkiris:F3iQz3hSCxOwhhOu@cluster0.ubegai3.mongodb.net/?retryWrites=true&w=majority")

    db=client["Team6"]

    output=index.find_min()

    expected_result=[0]

    for out in range(len(output)):

        assert output[out]==expected_result[out], "The output min is not correct"


    

