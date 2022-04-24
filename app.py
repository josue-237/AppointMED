from flask import Flask, render_template, request, redirect
import pymongo
import os
from appointment import Appointment
from flask_pymongo import PyMongo
import certifi
from event import Event
from doctor import Doctor
import qrcode


# -- Initialization section --
app = Flask(__name__)

# name of database
app.config["MONGO_DBNAME"] = "AppointMED"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:1CBSqy89oXd60vpW@cluster0.vq3ym.mongodb.net/AppointMED?retryWrites=true&w=majority"


time_slots = ["08:00am", "08:30am", "09:00am", "09:30am", "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm",
              "12:30pm", "01:00pm", "01:30pm", "02:00pm", "02:30pm", "03:00pm", "03:30pm", "04:00pm", "04:30pm"]

doctor_ids = {"Richard Silverstein": "1234"}

mongo = PyMongo(app, tlsCAFile=certifi.where())

# mongo.db.create_collection('doctors')

@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        doctors = Doctor.get_doctors(mongo)
    else:
        specialty = request.form['doctor-specialty']
        name = request.form['doctor-name']
        doctors = Doctor.get_filtered_doctors(mongo, specialty, name)
    return render_template("home.html", doctors=doctors)


@app.route("/Schedule/<doc_id>", methods=["GET", "POST"])
def schedule(doc_id):
    medical_plans = ["Triple S", "Medicaid", "UnitedHealth"]
    doctor_name = "Richard Silverstein"
    doc_id = doctor_ids[doctor_name]
    
    if request.form == "GET":
        time_slots2=[]
        time=''
        
        # time_slots= Appointment.get_available_time_slots(doc_id,"04-22-2022",mongo)
        return render_template("appointment.html", day='', time_slots=time_slots2,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)
    else:
        day = str(request.form.get('day'))
        time=''
        time=request.form.get('time')
        appt_id=Appointment.generate_appointment_id()
        collection = mongo.db.events
        time_slots2=Appointment.get_available_time_slots(doc_id,day,mongo,time_slots)
        if time:
            day=request.form.get('day2')
            print(day)
            Event.create_event(day,time,appt_id,doc_id,mongo)
            return redirect("/Schedule/"+appt_id)
        return render_template("appointment.html", day=day, time_slots=time_slots2,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)
            

@app.route("/datepicker")
def datepicker():
    return render_template("datepicker.html")


@app.route("/seed_db")
def seed_db():
    # collection = mongo.db.events
    # collection.remove({})
    # doc_id = doctor_ids["Richard Silverstein"]
    # collection = mongo.db.events
    # event1 = Event("22-06-2022", "08:30am", "2423fe323", doc_id)
    # event1json = to_json("08:30am", "04/25/2022", "2423fe323", doc_id)
    # collection.insert(event1json)
    # event2json = to_json("09:30am", "04/25/2022", "2423fe323", doc_id)
    # collection.insert(event2json)
    # event3json = to_json("10:30am", "04/25/2022", "2423fe323", doc_id)
    # collection.insert(event3json)
    # event4json = to_json("11:30am", "04/25/2022", "2423fe323", doc_id)
    # collection.insert(event4json)
    # event5json = to_json("01:30pm", "04/25/2022", "2423fe323", doc_id)
    # collection.insert(event5json)
    # event2=Event.create_event("22-06-2022","09:30am","2423fe323",doc_id,mongo)
    # event3=Event.create_event("22-06-2022","10:30am","2423fe323",doc_id,mongo)
    # event4=Event.create_event("22-06-2022","11:30am","2423fe323",doc_id,mongo)
    # event5=Event.create_event("22-06-2022","01:30pm","2423fe323",doc_id,mongo)
    doctor1 = Doctor.create_doctor("Damaris", "Torres", ["neurologist"], "San Juan, P.R.", 18.466333, -66.105721, ["Triple S", "Medicaid"], "787-777-7776", 'url()', mongo)
    doctor1 = Doctor.create_doctor(" Jose", "Rodriguez", ["dermatologist"], "Rio Grande, P.R.", 18.38023, -65.83127, ["Triple S"], "787-776-7776", 'url()', mongo)
    doctor1 = Doctor.create_doctor("Pedro", "Figueroa", ["allergist"], "Mayaguez, P.R.", 18.20107, -67.139627, ["Medicaid"], "787-576-7776", 'url()', mongo)

    return "seeded successfully"


def to_json(start_time, date, appointment_id, doc_id):
    """
        Method returns every class property as a JSON
        :return: dictionary of properties and class values
        """
    return {
        "start_time": start_time,
        "date": date,
        "appointment_id": appointment_id,
        "doctor_id": doc_id
    }
