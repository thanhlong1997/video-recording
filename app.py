
from flask import Flask
import os
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
template_dir = my_absolute_dirpath + '/template'
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__,template_folder=template_dir)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024