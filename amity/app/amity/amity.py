import random
import stringcase

from app.room_files.room import Room, Office, Living_space
from app.person_files.person import Person, Fellow, Staff


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

    def create_room(self, args):
        """function to create a room."""
        try:
            room_type = stringcase.pascalcase(input("<room_type>: "))
            if room_type != "Office" and room_type != "Living Space":
                raise NameError
            self.room_names = input("<room_name>: ")
            self.room_name_split = self.room_names.split(",")
            for room_name in self.room_name_split:
                if room_name == (room for room in self.rooms):
                    return "Room already exists"
                else:
                    if room_type == "Office":
                        room = Office(room_name)
                        self.offices.append(room)
                        self.office_shuffle.append(room)
                        self.rooms.append(room_name)
                        return "Offices created successfully"
                    elif room_type == "Living Space":
                        room = Living_space(room_name)
                        self.living_spaces.append(room)
                        self.living_spaces_shuffle.append(room)
                        self.rooms.append(room_name)
                        return "Living Spaces Created Successfully"
        except NameError:
            return "invalid entry. Please enter office or living space"

    def add_person(self, first_name, last_name, designation,
                   wants_accommodation):
        """add person to system and allocates a random room"""
        try:
            self.first_name = input("First Name: ")
            self.last_name = input("Last Name: ")
            name = self.first_name + " " + self.last_name
            if self.first_name.isalpha() and self.last_name.isalpha() is False:
                raise TypeError
            try:
                self.designation = input("add_person <Staff|Fellow>: ")
                if self.designation != "Staff" and \
                        self.designation != "Fellow":
                    raise ValueError
                try:
                    self.wants_accommodation = \
                        input("wants_accommodation Y/N: ")
                    if self.wants_accommodation != "Y" and \
                            self.wants_accommodation != "N":
                        raise ValueError
                    if self.designation == "Staff" and\
                            self.wants_accommodation == "Y":
                        return "Staff cannot be allocated Living Space"
                    else:
                        if self.designation == "staff":
                            person = Staff(name)
                            self.staff.append(person)
                            self.staff_shuffle.append(person)
                            self.people.append(name)
                        elif self.designation == "fellow":
                            person = Fellow(name,
                                            self.wants_accommodation)
                            self.fellows.append(person)
                            self.fellows_shuffle.append(person)
                            self.people.append(name)
                        self.allocate_room(person)
                        return "Person has been added successfully."
                except ValueError:
                    return "Incorrect entry. Please enter Y or N"
            except ValueError:
                return "Incorrect entry. Please enter either Staff or Fellow"
        except TypeError:
            return "The name cannot contain numbers or special characters"

    def allocate_room(self):
        """function to allocate person to room"""
        if len(self.rooms) == 0:
            print("There are no rooms added")
        elif len(self.people) == 0:
            print("There are no people to allocate to rooms")
        else:
            for office in random.shuffle(self.office_shuffle):
                if len(office.office_members) <= office.max_people:
                    office.office_members.append(random.shuffle(self.people))
                else:
                    print("Office has a maximum limit of 6 people")
            for living_space in random.shuffle(self.living_spaces_shuffle):
                for fellow in self.fellows_shuffle if fellow.wants_accommodation == "Y":
                    if len(living_space.living_space_members) <= 4:
                        living_space.living_space_members.append(fellow)
                    else:
                        print("Living Space has a maximum of 4 people")

    def reallocate_person(self, id, room_name):
        """function to re-allocate person to a new room"""
        self.id = input("<person id>: ")
        try:
            self.room_name = input("<room_name>")
            person_name = (name for name[int(self.id) - 1] in
                           self.people)
            old_office = (office for office in self.offices if
                          person_name == name
                          in office.office_members)
            if room_name != (office.room_name for office in self.offices):
                raise NameError
            self.room_name.office_members.append(person_name)
            old_office.office_members.remove(person_name)
            print("{} successfully reallocated to {}".format(person_name,
                                                             self.room_name))
        except NameError:
            print("Room does not exist")
        # code for living space reallocations to come here

    def load_people():
        """adds people from a text file"""
        text_file = input("<filename: ")
        file_name = text_file.txt.readlines()
        file_name.readlines()
        for sentence in file_name:
            sentence = sentence.split()
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
                qrint(living_value)
