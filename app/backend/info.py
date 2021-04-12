from flask import Flask, render_template, jsonify
import os

BP='../forms'

def show():
   
  with open(os.path.join(BP,'info.yml'), 'r') as f:

    return jsonify(f.read()) 
