# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template, jsonify, make_response, json
from flask.ext.sqlalchemy import sqlalchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlist: ///' + os.path.join(basedir,'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = sqlalchemy(app)
