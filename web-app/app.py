from flask import Flask
from controllers.index import index_page

app = Flask(__name__)

app.register_blueprint( index_page )

app.run(debug = True)