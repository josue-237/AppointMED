from flask import Flask, render_template, request, redirect
import pymongo
import os
from appointment import Appointment
from flask_pymongo import PyMongo
import certifi

app = Flask(__name__)
# MongoDB
# client = pymongo.MongoClient("mongodb+srv://admin:" + os.environ["MONGO_APPOINTMED_PWD"] +
#                              "@cluster0.vsmni.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://SDS:" + os.environ.get(
    "MONGO_PW") + "@cluster0.zc52h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

app.config["MONGO_DBNAME"] = "cluster0"

app.config[
    "MONGO_URI"
] = "mongodb+srv://SDS:" + os.environ.get(
    "MONGO_PW") + "@cluster0.zc52h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

time_slots = ["08:00am", "08:30am", "09:00am", "09:30am", "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm",
              "12:30pm", "01:00pm", "01:30pm", "02:00pm", "02:30pm", "03:00pm", "03:30pm", "04:00pm", "04:30pm"]

doctor_ids = {"Richard Silverstein": 1234}

mongo = PyMongo(app, tlsCAFile=certifi.where())
db = client.test


# mongo.db.create_collection('events')

@app.route("/")
@app.route("/home")
def home():
    pass


@app.route("/Schedule", methods=["GET", "POST"])
def schedule():
    medical_plans = ["Triple S", "Medicaid", "UnitedHealth"]
    doctor_name = "Richard Silverstein"
    doc_id = doctor_ids[doctor_name]
    if request.form == "GET":

        # time_slots= Appointment.get_available_time_slots(doc_id,"04-22-2022",mongo)
        return render_template("appointment.html", day='', time_slots=time_slots,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)
    else:
        day = request.form.get('day')
        return render_template("appointment.html", day=day, time_slots=time_slots,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)


@app.route("/datepicker")
def datepicker():
    return render_template("datepicker.html")


@app.route("/seed_db")
def seed_db():
    pass
