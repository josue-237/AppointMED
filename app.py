from flask import Flask, render_template, request, redirect
import pymongo
import os
from appointment import Appointment
from flask_pymongo import PyMongo
import certifi
from event import Event
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

doctor_ids = {"Richard Silverstein": "1234"}

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
        time_slots2=[]
        time=''
        
        # time_slots= Appointment.get_available_time_slots(doc_id,"04-22-2022",mongo)
        return render_template("appointment.html", day='', time_slots=time_slots2,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)
    else:
        day = request.form.get('day')
        time=''
        time=request.form.get('time')
        appt_id=Appointment.generate_appointment_id()
        collection = mongo.db.events
        time_slots2=Appointment.get_available_time_slots(doc_id,day,mongo,time_slots)
        if time:
            return redirect("/Schedule/"+appt_id)
        return render_template("appointment.html", day=day, time_slots=time_slots2,
                               doctor_image="https://www.pinnaclecare.com/wp-content/uploads/2017/12/bigstock-African-young-doctor-portrait-28825394.jpg",
                               doctor_name="Richard Silverstein", doctor_specialty="Dermatologist",
                               doctor_address="14 Calle Peral N Ste La Mayaguez PR, 00680, Estados Unidos",
                               doctor_phone="559-206-4429", medical_plans=medical_plans)
    # elif request.form == "POST"  and time:
    #     return redirect('/Schedule/'+time)


@app.route("/datepicker")
def datepicker():
    return render_template("datepicker.html")


@app.route("/seed_db")
def seed_db():
    # collection = mongo.db.events
    # collection.remove({})
    doc_id=doctor_ids["Richard Silverstein"]
    collection = mongo.db.events
    event1=Event("22-06-2022","08:30am","2423fe323",doc_id)
    event1json=to_json("08:30am","04/25/2022","2423fe323",doc_id)
    collection.insert(event1json)
    event2json=to_json("09:30am","04/25/2022","2423fe323",doc_id)
    collection.insert(event2json)
    event3json=to_json("10:30am","04/25/2022","2423fe323",doc_id)
    collection.insert(event3json)
    event4json=to_json("11:30am","04/25/2022","2423fe323",doc_id)
    collection.insert(event4json)
    event5json=to_json("01:30pm","04/25/2022","2423fe323",doc_id)
    collection.insert(event5json)
    # event2=Event.create_event("22-06-2022","09:30am","2423fe323",doc_id,mongo)
    # event3=Event.create_event("22-06-2022","10:30am","2423fe323",doc_id,mongo)
    # event4=Event.create_event("22-06-2022","11:30am","2423fe323",doc_id,mongo)
    # event5=Event.create_event("22-06-2022","01:30pm","2423fe323",doc_id,mongo)
    
    return "seeded successfully"
  
def to_json(start_time,date,appointment_id,doc_id):
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