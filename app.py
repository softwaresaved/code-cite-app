"""
Simple flask app
"""
import os
from flask import Flask
app = Flask(__name__)


UPLOAD_FOLDER = '/tmp/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Set the app secret key to prevent CSRF

app.secret_key = os.urandom(24)

@app.route('/', methods=['GET'])
def root():
    """
    Root page of site
    """
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

