class Appointment:
    def __init__(self,doctor_image,address,specialty, appointment_id, doctor_id,days=[],time_slots_taken=[]):
        """
        Initializes Event object
        :param days: days that have time slots taken
        :param time_slots_taken: Time event starts
        :param doctor_image: Time event ends
        :param address: ID of appointment associated with event
        :param specialty: specialty of doctor
        :param appointment_id: appointment id created when an appointment is scheduled
        :param doctor_id: ID of doctor associated with event
        """

        self.time_slots_taken = self.set_days(time_slots_taken)
        self.doctor_image = self.set_end_date(end_date)
        self.appointment_id = self.set_appointment_id(appointment_id)
        self.doctor_id = self.set_doctor_id(doctor_id)

    # Setters
    

    def set_appointment_id(self, appointment_id):
        if type(appointment_id) != str:
            raise TypeError("appointment_id must be a string")
        self.appointment_id = appointment_id

    def set_doctor_id(self, doctor_id):
        if type(doctor_id) != str:
            raise TypeError("doctor_id must be a string")
        self.doctor_id = doctor_id

    
