# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 14:31:33 2022

@author: gmanu
"""

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def i():
    return render_template("index.html")

if __name__=="__main__":
    app.run()