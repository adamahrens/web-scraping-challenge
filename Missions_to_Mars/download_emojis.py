import datetime as dt
import numpy as np
import sqlalchemy
import wget
import requests
import scrape_emojis
import shutil
import scrape_mars
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/emojis")

emojis = mongo.db.emojis.find()

for emoji_data in emojis:
    print(emoji_data)
    # Open the url image, set stream to True, this will return the stream content.
    resp = requests.get(emoji_data['url'], stream=True)
    file_path = './emojis/' + emoji_data['file']

    # Open a local file with wb ( write binary ) permission.
    local_file = open(file_path, 'wb')

    # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
    resp.raw.decode_content = True

    # Copy the response stream raw data to local image file.
    shutil.copyfileobj(resp.raw, local_file)

    # Remove the image url response object.
    del resp
