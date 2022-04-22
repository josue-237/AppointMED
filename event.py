class Event:
    def __init__(self, date, start_time, appointment_id, doctor_id):
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
    def set_start_time(self, start_time):
        if type(start_time) != str:
            raise TypeError("start_time must be a string")
        self.start_date = start_time

    def set_date(self, date):
        if type(date) != str:
            raise TypeError("date must be a string")
        self.end_date = date

    def set_appointment_id(self, appointment_id):
        if type(appointment_id) != str:
            raise TypeError("appointment_id must be a string")
        self.appointment_id = appointment_id

    def set_doctor_id(self, doctor_id):
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
