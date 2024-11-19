import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")
db = client.hms_database

# Collections
patients_collection = db.patients
doctors_collection = db.doctors
caregivers_collection = db.caregivers
staff_collection = db.staff
