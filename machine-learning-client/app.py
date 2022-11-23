from flask import Flask
from controllers.index import index_page
from controllers.gallery import gallery_page

app = Flask(__name__)

app.register_blueprint( gallery_page,url_prefix = "/gallery" )
app.register_blueprint( index_page )

app.run(debug = True)