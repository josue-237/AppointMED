class Event:
    def __init__(self, start_date, end_date, appointment_id, doctor_id):
        """
        Initializes Event object
        :param start_date: Time event starts
        :param end_date: Time event ends
        :param appointment_id: ID of appointment associated with event
        :param doctor_id: ID of doctor associated with event
        """

        self.start_date = start_date
        self.end_date = end_date
        self.appointment_id = appointment_id
        self.doctor_id = doctor_id

    # Getters
    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

    def get_appointment_id(self):
        return self.appointment_id

    def get_doctor_id(self):
        return self.doctor_id

    # Setters
    def set_start_date(self, start_date):
        self.start_date = start_date

    def set_end_date(self, end_date):
        self.end_date = end_date

    def set_appointment_id(self, appointment_id):
        self.appointment_id = appointment_id

    def set_doctor_id(self, doctor_id):
        self.doctor_id = doctor_id

    ###
    def to_json(self):
        """
        Method returns every class property as a JSON
        :return: dictionary of properties and class values
        """
        return {
            "start_date": self.start_date,
            "end_date": self.end_date,
            "appointment_id": self.appointment_id,
            "doctor_id": self.doctor_id
        }