from flask import Blueprint, render_template, request, flash, jsonify
from .models import Freightproperty
from . import db

flights = Blueprint('flights', __name__)

@flights.route('/flight', methods=['GET', 'POST'])
def flight():
     transportation_type = "flights"
     if request.method == 'POST': 
        weight = request.form.get('weight')
        length = request.form.get('length')
        breadth = request.form.get('breadth')
        height = request.form.get('height')
        count = request.form.get('count')
        source = request.form.get('source')
        source_pincode = request.form.get('source_pincode')
        destination = request.form.get('destination')
        destination_pincode = request.form.get('destination_pincode')
        new_quote = Freightproperty(transportation_type=transportation_type,count=count,weight=weight,length=length,breadth=breadth,height=height,source=source,source_pincode=source_pincode,destination=destination,destination_pincode=destination_pincode)
        db.session.add(new_quote) 
        db.session.commit()
        flash('Calculating Quote', category='success')
     return render_template('flight.html')