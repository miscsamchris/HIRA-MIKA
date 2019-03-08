# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:51:26 2019

@author: TLSWM
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True, host='10.177.7.168', port="5000")