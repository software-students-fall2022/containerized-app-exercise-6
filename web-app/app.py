from flask import Flask
from controllers.index import index_page
from controllers.gallery import gallery_page

app = Flask(__name__)

app.register_blueprint( gallery_page,url_prefix = "/gallery" )
app.register_blueprint( index_page )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6001, debug=True)

