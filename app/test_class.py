import unittest
import pytest

from app.amity import Amity


class AmityModelTests(unittest.TestCase):
    def setUp(self):
        """Set up Amity ()"""
        self.amity = Amity()

    def tearDown(self):
        del self.amity

    def test_create_office(self):
        '''tests it creates office'''
        new_office = self.amity.create_room("office", "medical")
        self.assertEqual(new_office, "MEDICAL office created successfully")

    def test_create_living_space(self):
        '''tests it creates living space'''
        new_living_space = self.amity.create_room("Livingspace", "Mara")
        self.assertEqual(new_living_space,
                         "MARA living space created successfully")

    def test_wrong_room_type(self):
        '''tests error message if wrong room type is put'''
        new_wrong_room_type = self.amity.create_room("Something Wrong",
                                                     "Wrong Room")
        self.assertEqual(new_wrong_room_type,
                         "invalid entry. Please enter office or living space")

    def test_staff_cannot_be_allocated_living_space(self):
        staff_to_living = self.amity.add_person("Kevin", "Kamau", "Staff", "Y")
        self.assertEqual(staff_to_living, "Staff cannot be allocated Living Space")

    def test_wrong_designation(self):
        person_wrong_des = self.amity.add_person("Evalyn", "Kyalo", "Watchman")
        self.assertEqual(person_wrong_des, "Incorrect entry. Please enter staff or fellow")

    def test_reallocate_person(self):
        self.amity.create_room("Office", "Jamuhuri")
        self.amity.add_person("James", "Kabue", "Staff")
        self.amity.create_room("Office", "Madaraka")
        test_reallocate = self.amity.reallocate_person("James", "Kabue", "Madaraka")
        self.assertEqual(test_reallocate, "JAMES KABUE reallocated to MADARAKA office")

    def test_reallocate_to_the_same_room(self):
        self.amity.create_room("Office", "Bagdad")
        self.amity.add_person("Alex", "Simanzi", "Staff")
        test_reallocate = self.amity.reallocate_person("Alex", "Simanzi", "Bagdad")
        self.assertEqual(test_reallocate, "Cannot reallocate to the same room")

    def test_reallocate_to_the_non_existent_room(self):
        self.amity.create_room("Office", "Bagdad")
        self.amity.add_person("Alex", "Simanzi", "Staff")
        test_reallocate = self.amity.reallocate_person("Alex", "Simanzi", "Israel")
        self.assertEqual(test_reallocate, "Room does not exist")


if __name__ == '__main__':
    unittest.main()
