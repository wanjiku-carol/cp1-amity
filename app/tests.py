import unittest
from app.room.room import Room
from app.amity.amity import Amity


class AmityTests(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()
        self.room = Room()

    def test_add_person(self):
        """test if add_person will add a person and give designation"""
        new_person = ["Joy Kenzo", "Staff", False]
        self.add_person(new_person)
        """Assert that there is a room to allocate new person in the "rooms"
         dictionary"""
        self.assertGreater(len(rooms), 0)
        self.assertFalse(self.add_person(new_person),
                         "There are no rooms to allocate to new person")

        self.assertTrue(self.add_person(new_person), (new_person[0] + " has\
        been added"))

    def test_added_person_exists(self):
        new_same_person = ["Joy Kenzo", "Staff", False]
        self.add_person(new_person)
        """test that the error message for duplicate addition is generated"""

        self.assertTrue(self.add_person(new_same_person), (new_same_person[0]
                                                           + " already exists")
                        )
        """test that the dictionary "people" has the new_same_person"""
        # self.assertthat_(people, has_value(new_same_person))

    def test_create_room(self):
        new_room = ["Kilimanjaro", "Office"]
        self.create_room(new_room)
        self.assertTrue(self.create_room(new_room), (new_room[0]
                                                     + "room created"))
        """test that the "rooms" dictionary now has the added room"""
        # self.assertthat_(rooms, has_value(new_room))

    def test_wants_allocation(self):
        new_fellow = ["Steve", "Fellow", True]
        self.assertEqual(
            self.wants_allocation(new_fellow),
            True)
        self.assertFalse(new_fellow[1], "Staff")


if __name__ == '__main__':
    unittest.main()
