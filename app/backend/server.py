#!/usr/bin/python3

from flask import Flask, render_template, request
from flask import jsonify
import os
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# Read the yaml file to configure the endpoints
app.add_api("spec.yaml")

# create a URL route in our application for "/"
@app.route("/")

def home():
    msg = {"msg": "THIS IS MY SERVER IT IS FROM ME"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

