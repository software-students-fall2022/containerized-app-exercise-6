import os
from os.path import dirname, join
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from controllers import index
from PIL import Image, ImageDraw
from io import BytesIO
import re
import base64
import face_recognition
from hsemotion.facial_emotions import HSEmotionRecognizer


with open("tests/test_group.jpg", "rb") as group_img:
    test_raw_group_img = base64.b64encode(group_img.read())
test_group_img_bytes = BytesIO(base64.b64decode(test_raw_group_img))

with open("tests/test_happy.jpg", "rb") as happy_img:
    test_raw_happy_img = base64.b64encode(happy_img.read())
test_happy_img_bytes = BytesIO(base64.b64decode(test_raw_happy_img))

with open("tests/test_sad.jpg", "rb") as sad_img:
    test_raw_sad_img = base64.b64encode(sad_img.read())
test_sad_img_bytes = BytesIO(base64.b64decode(test_raw_sad_img))

with open("tests/test_fear.jpg", "rb") as fear_img:
    test_raw_fear_img = base64.b64encode(fear_img.read())
test_fear_img_bytes = BytesIO(base64.b64decode(test_raw_fear_img))

with open("tests/test_noface.jpg", "rb") as noface_img:
    test_raw_noface_img = base64.b64encode(noface_img.read())
test_noface_img_bytes = BytesIO(base64.b64decode(test_raw_noface_img))

class Tests:
    def test_face_detect(self):
        image = face_recognition.load_image_file(test_group_img_bytes)
        face_locations = face_recognition.face_locations(image,1,"cnn") 
        result = []
        imgs = []
        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]
            imgs.append(Image.fromarray(face_image))
        if(len(imgs) > 0):
            for img in imgs:
                buffer = BytesIO()
                img.save(buffer,format="PNG")                  
                myimage = buffer.getvalue()   
                myimage = "data:image/png;base64," + base64.b64encode(myimage).decode('utf-8')
                result.append(myimage)
        assert result==index.face_detect(test_group_img_bytes)
    
    def test_face_detect_load_image_fail(self):
        assert None==index.face_detect(None)

    def test_get_emotion_happiness(self):
        assert "Happiness"==index.get_emotion(test_happy_img_bytes)


    def test_get_emotion_sadness(self):
        assert "Sadness"==index.get_emotion(test_sad_img_bytes)

    def test_get_emotion_surprise(self):
        assert "Fear"==index.get_emotion(test_fear_img_bytes)

    def test_face_detect_with_emotions(self):
        imgs = index.face_detect(test_group_img_bytes)
        result = []
        if(imgs is not None and len(imgs) > 0):
            for img in imgs:
                raw = re.sub('^data:image/.+;base64,', '', img)
                raw = BytesIO(base64.b64decode(raw))
                emotion = index.get_emotion(raw)
                result.append({"img":img,"emotion":emotion})
            assert result==index.face_detect_with_emotions(test_group_img_bytes)
        else:
            assert None==index.face_detect_with_emotions(test_group_img_bytes)

    def test_face_detect_without_face(self):
        assert None==index.face_detect_with_emotions(test_noface_img_bytes)