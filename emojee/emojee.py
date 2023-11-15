#!/bin/python3

from flask import Flask, request
from emoji import emojize
import os

app = Flask(__name__)

@app.route("/")
def emojee():
    emoji_name = request.args.get('name', "No emoji yet :c")
    return emojize(emoji_name)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))