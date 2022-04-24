import unittest
from doctor import Doctor


class TestDoctor(unittest.TestCase):
    def setUp(self):
        self.doctor1 = Doctor("Jose", "Sanchez", ["dermatologist"], "123 Ave", 80.0, 80.0, ["MCS", "TRIPLES"],
                              7874036543, "test_url.com")
        self.doctor2 = Doctor("Juan", "Perez", ["allergist"], "312 Park Ave", -90.0, 180.0, ["MCS", "TRIPLES"],
                              7874036543, "test_url.com")
        self.doctor3 = Doctor("Henry", "Smith", ["cardiologist"], "1600 Amphitheatre Parkway Mountain View, CA 94043",
                              23.4, 120.55, ["MCS", "TRIPLES"], 7874036543, "test_url.com")

    def test00_init(self):
        self.assertEqual(self.doctor1.first_name, "Jose")
        self.assertEqual(self.doctor1.last_name, "Sanchez")
        self.assertEqual(self.doctor1.specialty, "dermatologist")
        self.assertEqual(self.doctor1.address, "123 Ave")
        self.assertEqual(self.doctor1.lat, 80.0)
        self.assertEqual(self.doctor1.lng, 80.0)
        self.assertEqual(self.doctor1.medical_coverages, ["MCS", "TRIPLES"])
        self.assertEqual(self.doctor1.phone_number, 7874036543)
        self.assertEqual(self.doctor1.photo_url, "test_url.com")

        self.assertEqual(self.doctor2.first_name, "Juan")
        self.assertEqual(self.doctor2.last_name, "Perez")
        self.assertEqual(self.doctor2.specialty, "allergist")
        self.assertEqual(self.doctor2.address, "312 Park Ave")
        self.assertEqual(self.doctor2.lat, -90.0)
        self.assertEqual(self.doctor2.lng, 180.0)
        self.assertEqual(self.doctor2.medical_coverages, ["MCS", "TRIPLES"])
        self.assertEqual(self.doctor2.phone_number, 7874036543)
        self.assertEqual(self.doctor2.photo_url, "test_url.com")

        self.assertEqual(self.doctor3.first_name, "Henry")
        self.assertEqual(self.doctor3.last_name, "Smith")
        self.assertEqual(self.doctor3.specialty, "cardiologist")
        self.assertEqual(self.doctor3.address, "1600 Amphitheatre Parkway Mountain View, CA 94043")
        self.assertEqual(self.doctor3.lat, 23.4)
        self.assertEqual(self.doctor3.lng, 120.55)
        self.assertEqual(self.doctor3.medical_coverages, ["MCS", "TRIPLES"])
        self.assertEqual(self.doctor3.phone_number, 7874036543)
        self.assertEqual(self.doctor3.photo_url, "test_url.com")
