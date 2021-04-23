#!/usr/bin/python3

from flask import Flask, render_template, request
from flask import jsonify
import os
import connexion
import info
# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("spec.yaml")

# create a URL route in our application for "/"
@app.route("/")

def home():
    return render_template('home.html') 

@app.route("/info")
def x():
  return render_template('info.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

