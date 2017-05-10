import random
import stringcase

from app.room import Office, LivingSpace
from app.person import Fellow, Staff


class Amity(object):

    def __init__(self):
        self.fellows = []
        self.fellows_shuffle = []
        self.staff = []
        self.staff_shuffle = []
        self.people = []
        self.offices = []
        self.office_shuffle = []
        self.living_spaces = []
        self.rooms = []
        self.living_spaces_shuffle = []
        self.allocate_office = {}
        self.allocate_living_space = {}
        self.reallocate_person = {}

    def create_room(self, room_type, room_names):
        """function to create a room."""
        try:
            if stringcase.pascalcase(room_type) != "Office" and \
                    stringcase.pascalcase(room_type) != "Living Space":
                raise NameError
            if room_names == (room for room in self.rooms):
                return "Room already exists"
            else:
                if stringcase.pascalcase(room_type) == "Office":
                    room = Office(room_names)
                    self.offices.append(room)
                    self.office_shuffle.append(room)
                    self.rooms.append(room_names)
                    print("Offices created successfully")
                    return "Offices created successfully"
                elif stringcase.pascalcase(room_type) == "Living Space":
                    room = LivingSpace(room_names)
                    self.living_spaces.append(room)
                    self.living_spaces_shuffle.append(room)
                    self.rooms.append(room_names)
                    print("Living Spaces Created Successfully")
                    return "Living Spaces Created Successfully"
        except NameError:
            print("invalid entry. Please enter office or living space")
            return "invalid entry. Please enter office or living space"

    def add_person(self, first_name, last_name, designation,
                   wants_accommodation):
        """add person to system and allocates a random room"""
        print("one")
        name = first_name + last_name
        print("two")
        try:
            if designation != "Staff" and designation != "Fellow":
                raise ValueError
            print("three")
            try:
                print("four")
                if wants_accommodation != "Y" and wants_accommodation != "N":
                    raise ValueError
                print("five")
                if designation == "Staff" and wants_accommodation == "Y":
                    print("Staff cannot be allocated Living Space")
                    return "Staff cannot be allocated Living Space"
                else:
                    print("six")
                    if stringcase.pascalcase(designation) == "Staff":
                        print("seven")
                        person = Staff(first_name, last_name)
                        print("eight")
                        self.staff.append(person)
                        self.staff_shuffle.append(person)
                        self.people.append(name)
                        print(self.people)
                        print("nine")
                        print(self.allocate_office())
                        print("Person has been added successfully.")

                    elif stringcase.pascalcase(designation) == "Fellow":
                        person = Fellow(first_name, last_name, wants_accommodation)
                        self.fellows.append(person)
                        self.fellows_shuffle.append(person)
                        self.people.append(name)
                        print(self.people)
                        print(self.allocate_office())
                        print(self.allocate_living_space())
                        print("Person has been added successfully.")
                print(self.people)
                # return "Person has been added successfully."
            except ValueError:
                print("Incorrect entry. Please enter Y or N")
                return "Incorrect entry. Please enter Y or N"
        except ValueError:
            print("Incorrect entry. Please enter either Staff or Fellow")
            return "Incorrect entry. Please enter either Staff or Fellow"

    def allocate_office():
        """function to allocate person to room"""
        for office in random.shuffle(self.office_shuffle):
            if len(office.office_members) <= office.max_people:
                office.office_members.append(name)
                print("{} has been allocated to {}".format(name,
                                                           office.room_names))
                return "{} has been allocated to {}".format(name,
                                                            office.room_names)

    def allocate_living_space():
        if self.wants_accommodation == "Y":
            for living_space in random.shuffle(self.living_spaces_shuffle):
                if len(living_space.living_space_members) <= 4:
                    living_space.living_space_members.append(self.name)
                    print("{} has been allocated to {}".format(self.name, living_space.room_name))
                    return "{} has been allocated to {}".format(self.name, living_space.room_name)

    # def reallocate_person(self, id, room_name):
    #     """function to re-allocate person to a new room"""
    #     self.id = input("<person id>: ")
    #     try:
    #         self.room_name = input("<room_name>")
    #         person_name = (name for name[int(self.id) - 1] in
    #                        self.people)
    #         old_office = (office for office in self.offices if
    #                       person_name == name
    #                       in office.office_members)
    #         if room_name != (office.room_name for office in self.offices):
    #             raise NameError
    #         self.room_name.office_members.append(person_name)
    #         old_office.office_members.remove(person_name)
    #         print("{} successfully reallocated to {}".format(person_name,
    #                                                          self.room_name))
    #     except NameError:
    #         print("Room does not exist")
        # code for living space reallocations to come here

    def load_people():
        """adds people from a text file"""
        text_file = input("<filename: ")
        file_name = text_file.txt.readlines()
        file_name.readlines()
        for sentence in file_name:
            sentence = sentence.split()
            for word in sentence:
                if word in sentence == "Y":
                    wants_accommodation = "Y"
                elif word in sentence == "N":
                    wants_accommodation = "N"
                elif word in sentence == "Staff":
                    designation = "Staff"
                elif word in sentence == "Fellow":
                    designation = "Fellow"
                else:
                    first_name = word[0]
                    last_name = word[1]
                add_person(first_name, last_name, designation, wants_accommodation)

    def load_state():
        """loads data from database into application"""
        pass

    def save_state():
        """Persists all the data stored in the app to a SQLite database"""
        pass

    def print_allocations(self):
        """prints a list of allocations"""
        self.office_allocations = dict((item.room_name, item.office_members)
                                       for item in self.offices)
        self.living_space_allocations = dict((item.room_name,
                                              item.living_space_members)
                                             for item in self.living_spaces)
        for office_key, office_value in self.office_allocations.items():
            print(office_key)
            print(("---------------") * len(self.office_allocations))
            print(", ".join(office_value))
        for living_key, living_value in self.living_space_allocations.items():
            print(living_key)
            print(("---------------") * len(self.office_allocations))
            print(", ".join(living_value))

    def print_unallocated(self):
        """prints a list of unallocated people"""
        pass

    def print_room(self, room_name):
        """prints names of people in room"""
        for office_key, office_value in self.office_allocations.items():
            if self.room_name == office_key:
                print(office_value)
        for living_key, living_value in self.living_space_allocations:
            if self.room_name == living_key:
                print(living_value)
