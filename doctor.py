
import hashlib
import time


class Doctor:
    """
    A class used to represent an Doctor

    ...

    Attributes
    ----------
    first_name : str
        The doctor's First Name
    last_name : str
        The doctor's Last Name
    specialty : list of str
        A list of specialties the doctor has
    address : str
        The doctor's office address
    lat : float
        The doctor's office latitude cordinate
    lng : float
        The doctor's office longitude cordinate
    medical_coverages : list of str
        The medical plan coverages the doctor accepts
    phone_number : int
        The doctor's office phone number.
    photo_url : str
        The doctor's photo url.
    curr_specialties : list of str
        a list of the current supported spealties.
    doc_id: id
        The doctor's unique id.

    Methods
    -------
    valid_first_name(first_name)
       Validates the type and value of the first_name
    valid_last_name(self, last_name)
        Validates the type and value of the last_name
    valid_specialties(self, specialties):
        Validates the type and value of specialties
    valid_address(self, address):
        Validates the type and value of the address
    valid_lat(self, lat):
        Validates the type and value of the lat
    valid_lng(self, lng):
        Validates the type and value of the lng
    valid_medical_coverages(self, medical_coverages):
       Validates the type and value of the medical_coverages
    valid_phone_number(self, phone_number):
        Validates the type and value of the phone_number
    valid_photo_url(self, photo_url):
        Validates the type and value of the photo_url
    generate_doctor_id():
        Generates a unique doctor's id
    """

    curr_specialties = {'dermatologist', 'allergist', 'cardiologist', 'gastroenterologist'}

    def __init__(self, first_name, last_name, specialties, address, lat, lng, medical_coverages, phone_number, photo_url):
        """
        Parameters
        ----------
        first_name : str
            The doctor's First Name
        last_name : str
            The doctor's Last Name
        specialty : list of str
            A list of specialties the doctor has
        address : str
            The doctor's office address
        lat : float
            The doctor's office latitude cordinate
        lng : float
            The doctor's office longitude cordinate
        medical_coverages : list of str
            The medical plan coverages the doctor accepts
        phone_number : int
            The doctor's office phone number.
        photo_url : str
            The doctor's photo url.
        doc_id: id
            The doctor's unique id.
        """   
        self.first_name = self.valid_first_name(first_name)
        self.last_name = self.valid_last_name(last_name)
        self.specialty = self.valid_specialties(specialties)
        self.address = self.valid_address(address)
        self.lat = self.valid_lat(lat)
        self.lng = self.valid_lng(lng)
        self.medical_coverages = self.valid_medical_coverages(medical_coverages)
        self.phone_number = self.valid_phone_number(phone_number)
        self.photo_url = self.valid_photo_url(photo_url)
        self.doc_id = self.generate_doctor_id()

    def valid_first_name(self, first_name):
        """ Validates the type and value of the first_name

        Parameters
        ----------
        first_name : str
            The doctor's First Name

        Raises
        ------
        TypeError
            If the doctor's First Name is not of type string.

        ValueError
            If the doctor's First Name exceeds 25 characters.
        """
        if type(first_name) != str:
            raise TypeError("The doctor's first name is not of type string")
        if len(first_name) > 25:
            raise ValueError("The doctor's first name exceeds 25 characters")
        return first_name

    def valid_last_name(self, last_name):
        """ Validates the type and value of the last_name

        Parameters
        ----------
        last_name : str
            The doctor's Last Name

        Raises
        ------
        TypeError
            If the doctor's Last Name is not of type string.

        ValueError
            If the doctor's Last Name exceeds 25 characters.
        """
        if type(last_name) != str:
            raise TypeError("The doctor's last name is not of type string")
        if len(last_name) > 25:
            raise ValueError("The doctor's last name exceeds 25 characters")
        pass

    def valid_specialties(self, specialties):
        """ Validates the type and value of specialties

        Parameters
        ----------
        specialties: list of str
            A list of specialties the doctor has

        Raises
        ------
        TypeError
            If the doctor's specialties is not of type list or any specialty is not of type str.

        ValueError
            If one of the doctor's specialties does not match the current specialties we support.
        """
        if type(specialties) != list:
            raise TypeError("The doctor's specialties is not of type list")
        for specialty in specialties:
            if type(specialty) != str:
                raise TypeError("The doctor's specialty is not of type string")
            if specialty not in self.curr_specialties:
                raise ValueError(specialty +  "specialty is currently not supported")
        return specialties

    def valid_address(self, address):
        """ Validates the type and value of the address

        Parameters
        ----------
        address : str
            The doctor's office address

        Raises
        ------
        TypeError
            If the doctor's office address is not of type string.

        ValueError
            If the doctor's office address exceeds 50 characters.
        """
        if type(address) != str:
            raise TypeError("The doctor's address is not of type str")
        if len(address) > 50:
            raise ValueError("The doctor's address exceeds 50 characters")
        return address

    def valid_lat(self, lat):
        """ Validates the type and value of the lat

        Parameters
        ----------
        lat : float
            The doctor's office latitude cordinate

        Raises
        ------
        TypeError
            If the doctor's office latitude cordinate is not of type float.

        ValueError
            If the doctor's office latitude cordinate is not in range of [-90 to 90].
        """
        if type(lat) != float:
            raise TypeError("The the doctor's office latitude cordinate is not of type float")
        if lat <= -91.0 or lat >= 90.0:
            raise ValueError("The Doctor's office latitude cordinate is not in range of [-90 to 90].")
            
    def valid_lng(self, lng):
        """ Validates the type and value of the lng

        Parameters
        ----------
        lng : float
            The doctor's office longitude cordinate

        Raises
        ------
        TypeError
            If the doctor's office longitude cordinate is not of type float.

        ValueError
            If the doctor's office longitude cordinate is not in range of [-180 to 180].
        """
        if type(lng) != float:
            raise TypeError("The the doctor's office latitude cordinate is not of type float")
        if lng <= -181.0 or lng >= 181.0:
            raise ValueError("The Doctor's office latitude cordinate is not in range of [-180 to 180].")
    
    def valid_medical_coverages(self, medical_coverages):
        """ Validates the type and value of the medical_coverages

        Parameters
        ----------
        medical_coverages : list of str
            The medical plan coverages the doctor accepts

        Raises
        ------
        TypeError
            If the doctor's medical_coverages is not of type list or any medical coverage is not of type str.

        """
        if type(medical_coverages) != list:
            raise TypeError("Medical coverages should be of type list")
        
        for coverage in medical_coverages:
            if type(coverage) != str:
                raise TypeError("Medical coverage should be of type str")
    
        return medical_coverages

    def valid_phone_number(self, phone_number):
        """ Validates the type and value of the phone_number

        Parameters
        ----------
        phone_number : int
            The doctor's office phone number.

        Raises
        ------
        TypeError
            If the doctor's office phone number is not an int
        """
        if type(phone_number) != int:
            raise TypeError("Doctor's office phone number should be of type int")
        return phone_number

    def valid_photo_url(self, photo_url):
        """ Validates the type and value of the photo_url

        Parameters
        ----------
        photo_url : str
            The doctor's photo url.

        Raises
        ------
        TypeError
            If the doctor's photo url is not a string.
        """
        if type(photo_url) != str:
            raise TypeError("Doctor'sphoto url should be of type string")
        return photo_url

    def generate_doctor_id():
        """ Generates a unique doctor's id
        """
        cur_time = str(time.time())
        hashed_time = hashlib.sha1()
        hashed_time.update(cur_time.encode("utf8"))
        return hashed_time.hexdigest()