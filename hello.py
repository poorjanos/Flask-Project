# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:04:17 2019

@author: PoorJ
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
     return "Hello World!"

if __name__ == '__main__':
     app.run(port = 5000, debug = True)