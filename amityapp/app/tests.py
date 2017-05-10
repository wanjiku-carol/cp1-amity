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

    def test_add_person(self):
        ''''test that a person is added'''
        new_staff = self.amity.add_person("Joy", "Kenzo", "Staff", "N")
        self.assertEqual(new_staff, "Person has been added successfully.")

        new_fellow = self.amity.add_person("Klaudia", "Mwangi", "Fellow", "Y")
        self.assertEqual(new_fellow, "Person has been added successfully.")

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

    def test_name_error(self):
        name_with_error = self.amity.add_person("Sam76", "8?.", "Staff", "N")
        self.assertEqual(name_with_error, "The name cannot contain numbers or special characters")

    # def test_reallocate_nonexistent_person(self):
    #     '''test you cannot reallocate a non-existent person'''
    #     test_nonexist_person = self.amity.reallocate_person(8, "Kilimanjaro")
    #     self.assertEqual(test_nonexist_person,
    #                      "Person does not exist. Please add this person")
    #
    # def test_reallocate_to_non_existent_room(self):
    #     '''test you cannot reallocate to a person to a non-existent room'''
    #     test_nonexist_room = self.amity.reallocate_person(1, "Jerusalem")
    #     self.assertEqual(test_nonexist_room, "Room does not exist.")
    #
    # def test_reallocate_staff_to_living_space(self):
    #     '''test cannot reallocate staff to living space'''
    #     test_staff_to_living_space = self.amity.reallocate_person(1, "Mara")
    #     self.assertEqual(test_staff_to_living_space, "Staff cannot be allocated\
    #                     living space")
    #
    # def test_reallocate_fellow_to_living_space(self):
    #     '''test reallocate fellow'''
    #     reallocate_fellow = self.amity.reallocate_person(2, "Tsavo")
    #     self.assertEqual(reallocate_fellow, "Reallocated Successfully")
    #
    # def test_reallocate_fellow_not_in_living_space(self):
    #     '''test you cannot reallocate a fellow that is not already allocated'''
    #     self.amity.add_person("Plantain Kiheto", "Fellow", False)
    #     test_realloc_not_alloc = self.amity.reallocate_person(4, "Mara")
    #     self.assertEqual(test_realloc_not_alloc, "Cannot reallocate.\
    #     Person was not allocated to any living space.")
    #
    # def test_reallocate_person_to_new_office(self):
    #     '''test reallocate a person to a new office'''
    #     self.amity.create_room("Office", ["Office"])
    #     reall_to_office = self.amity.reallocate_person(3, "Wall Street")
    #     self.assertEqual(reall_to_office, "Reallocated Successfully!")


if __name__ == '__main__':
    unittest.main()
