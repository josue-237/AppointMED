class Event:
    def __init__(self, date: str, start_time: str, appointment_id: str, doctor_id: str):
        """
        Initializes Event object
        :param start_time: Time event starts
        :param date: Date event takes place
        :param appointment_id: ID of appointment associated with event
        :param doctor_id: ID of doctor associated with event
        """

        self.start_date = self.set_start_time(start_time)
        self.end_date = self.set_date(date)
        self.appointment_id = self.set_appointment_id(appointment_id)
        self.doctor_id = self.set_doctor_id(doctor_id)

    # Setters
    def set_start_time(self, start_time: str):
        if type(start_time) != str:
            raise TypeError("start_time must be a string")
        self.start_date = start_time

    def set_date(self, date: str):
        if type(date) != str:
            raise TypeError("date must be a string")
        self.end_date = date

    def set_appointment_id(self, appointment_id: str):
        if type(appointment_id) != str:
            raise TypeError("appointment_id must be a string")
        self.appointment_id = appointment_id

    def set_doctor_id(self, doctor_id: str):
        if type(doctor_id) != str:
            raise TypeError("doctor_id must be a string")
        self.doctor_id = doctor_id

    # Getters
    def get_start_time(self):
        return self.start_date

    def get_date(self):
        return self.end_date

    def get_appointment_id(self):
        return self.appointment_id

    def get_doctor_id(self):
        return self.doctor_id

    ###
    def to_json(self):
        """
        Method returns every class property as a JSON
        :return: dictionary of properties and class values
        """
        return {
            "start_time": self.start_date,
            "date": self.end_date,
            "appointment_id": self.appointment_id,
            "doctor_id": self.doctor_id
        }

    @staticmethod
    def create_event(start_time: str, date: str, appointment_id: str, doctor_id: str, database):
        """
        Method returns an event object and stores it in a mongoDB database
        :param start_time: Time event starts
        :param date: Date event takes place
        :param appointment_id: ID of appointment associated with event
        :param doctor_id: ID of doctor associated with event
        :param database: MongoDB database
        :return: Event object
        """
        event = Event(start_time, date, appointment_id, doctor_id)
        event_document = event.to_json()
        collection = database.db.events
        collection.insert_one(event_document)
        return event

    @staticmethod
    def get_event(appointment_id: str, database):
        """
        Method returns an event object from a mongoDB database
        :param appointment_id: ID of appointment associated with event
        :param database: MongoDB database
        :return: Event object
        """
        collection = database.db.events
        event_document = collection.find_one({"appointment_id": appointment_id})
        return Event(event_document["start_time"], event_document["date"], event_document["appointment_id"],
                     event_document["doctor_id"])
