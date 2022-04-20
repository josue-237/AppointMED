from flask import Flask
import pymongo
import os

app = Flask(__name__)
# MongoDB
client = pymongo.MongoClient("mongodb+srv://admin:" + os.environ["MONGO_APPOINTMED_PWD"] +
                             "@cluster0.vsmni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
