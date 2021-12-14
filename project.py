# Download file
# save file

import requests
import os
import shutil

global dump

def download_file():
    global dump
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data"
    file = requests.get(url, stream=True)
    dump = file.raw

def save_file():
    global dump
    location = os.path.abspath("E:\folder\abalone.data")
    with open("file.gz", 'wb') as location:
        shutil.copyfileobj(dump, location)