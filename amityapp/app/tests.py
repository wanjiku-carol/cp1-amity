import unittest
from app.amity import Amity


class AmityModelTests(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()
        self.amity.add_person("Hohay", "Bombay", "Staff", "N")
        self.amity.add_person("Jennifer", "Mwakini", "Fellow", "Y")
        self.amity.create_room("Office", "India, Johannes, Cairo")
        self.amity.create_room("Living Space", "Kisumu, Nairobi, Mombasa")

    def tearDown(self):
        del self.amity

    def test_create_office(self):
        '''tests it creates office'''
        new_office = self.amity.create_room("office", "medical")
        self.assertEqual(new_office, "Offices created successfully")

    def test_create_living_space(self):
        '''tests it creates living space'''
        new_living_space = self.amity.create_room("Living Space", "Mara")
        self.assertEqual(new_living_space,
                         "Living Spaces Created Successfully")

    def test_wrong_room_type(self):
        '''tests error message if wrong room type is put'''
        new_wrong_room_type = self.amity.create_room("Something Wrong",
                                                     "Wrong Room")
        self.assertEqual(new_wrong_room_type,
                         "invalid entry. Please enter office or living space")

    def test_add_staff_allocate_to_office(self):
        ''''test that a person is added'''
        new_staff = self.amity.add_person("Joy", "Kenzo", "Staff", "N")
        self.assertEqual(new_staff, "Successful!")

    def test_add_fellow_allocate_to_office(self):
        new_fellow = self.amity.add_person("Klaudia", "Mwangi", "Fellow", "Y")
        self.assertEqual(new_fellow, "Successful!")

    def test_add_fellow_allocate_to_living_space(self):
        new_fellow = self.amity.add_person("Klaudia", "Mwangi", "Fellow", "Y")
        self.assertEqual(new_fellow, new_fellow, "Successful!")

    def test_staff_cannot_be_allocated_living_space(self):
        staff_to_living = self.amity.add_person("James", "Kamau", "Staff", "Y")
        self.assertEqual(staff_to_living, "Staff cannot be allocated Living Space")

    def test_wrong_wants_accomodation_entry(self):
        person_wrong_wants_accom = self.amity.add_person("Kevin", "Ochieng",
                                                         "Staff", "What")
        self.assertEqual(person_wrong_wants_accom, "Incorrect entry. Please enter Y or N")

    def test_wrong_designation(self):
        person_wrong_des = self.amity.add_person("Evalyn", "Kyalo", "Watchman",
                                                 "N")
        self.assertEqual(person_wrong_des, "Incorrect entry. Please enter either Staff or Fellow")


if __name__ == '__main__':
    unittest.main()
