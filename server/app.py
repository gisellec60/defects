#!/usr/bin/env python3

import smtplib
import json
import os
from flask import request, session, make_response, render_template, redirect, current_app
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import app, db, api
from datetime import date, datetime
from models import Defect

@app.route('/')
@app.route('/<int:id>')
def index(id=0):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(port=5555,debug=True)