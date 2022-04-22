class Appointment:
    def __init__(self,doctor_image,address,specialty, appointment_id, doctor_id):
        """
        Initializes Event object
        :param doctor_image: Time event ends
        :param address: ID of appointment associated with event
        :param specialty: specialty of doctor
        :param appointment_id: appointment id created when an appointment is scheduled
        :param doctor_id: ID of doctor associated with event
        """

        
        self.appointment_id = self.set_appointment_id(appointment_id)
        self.doctor_id = self.set_doctor_id(doctor_id)
        self.doctor_image=self.set_doctor_image(doctor_image)
        self.address=self.set_doctor_address(address)
        self.specialty=self.set_doctor_specialty(specialty)

    # Setters
    

    def set_appointment_id(self, appointment_id):
        if type(appointment_id) != str:
            raise TypeError("appointment_id must be a string")
        self.appointment_id = appointment_id
    def set_doctor_id(self, doctor_id):
        if type(doctor_id) != str:
            raise TypeError("doctor_id must be a string")
        self.appointment_id = doctor_id
    def set_doctor_specialty(self, specialty):
        if type(specialty) != str:
            raise TypeError("specialty must be a string")
        self.doctor_id = specialty
    def set_doctor_address(self, address):
        if type(address) != str:
            raise TypeError("address must be a string")
        self.doctor_id = address
    def set_doctor_image(self, doctor_image):
        if type(doctor_image) != str:
            raise TypeError("doctor_image must be a string")
        self.doctor_id = doctor_image

    
