from flask import Flask
import face_recognition
from controllers.index import index_page
from controllers.gallery import gallery_page


import os
import matplotlib.pyplot as plt 
from PIL import Image

from io import BytesIO


app = Flask(__name__)

app.register_blueprint( gallery_page,url_prefix = "/gallery" )
app.register_blueprint( index_page )



  
  
if __name__ == '__main__':
     app.run(host='127.0.0.1', port=7001, debug=True)