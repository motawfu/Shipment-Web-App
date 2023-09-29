from flask import Blueprint, render_template, request, flash, jsonify
from .models import Freightproperty
from . import db
import json
import datetime as datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home(): 
   return render_template("index.html")

@views.route('/road.html', methods=['GET', 'POST'])
def road():
   return render_template("road.html")

@views.route('/ship.html', methods=['GET', 'POST'])
def ship():
   return render_template("ship.html")