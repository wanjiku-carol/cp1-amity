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
        self.office_allocations = {}
        self.living_space_allocations = {}
        self.reallocated_person = {}

    def create_room(self, room_type, room_name):
        """function to create a room."""
        try:
            if stringcase.pascalcase(room_type) != "Office" and \
                    stringcase.pascalcase(room_type) != "Livingspace":
                raise NameError
            if room_name == (room for room in self.rooms):
                return "Room already exists"
            else:
                if stringcase.pascalcase(room_type) == "Office":
                    room = Office(room_name)
                    self.offices.append(room)
                    self.office_shuffle.append(room)
                    self.rooms.append(room_name)
                    print(self.rooms)
                    print("Offices created successfully")
                    return "Offices created successfully"
                elif stringcase.pascalcase(room_type) == "Livingspace":
                    room = LivingSpace(room_name)
                    self.living_spaces.append(room)
                    self.living_spaces_shuffle.append(room)
                    self.rooms.append(room_name)
                    print(self.rooms)
                    print("Living Spaces Created Successfully")
                    return "Living Spaces Created Successfully"
        except NameError:
            print("invalid entry. Please enter office or living space")
            return "invalid entry. Please enter office or living space"

    def add_person(self, first_name, last_name, designation,
                   wants_accommodation):
        """add person to system and allocates a random room"""
        name = first_name + last_name
        try:
            if designation != "Staff" and designation != "Fellow":
                raise ValueError
            try:
                if wants_accommodation != "Y" and wants_accommodation != "N":
                    raise ValueError
                if designation == "Staff" and wants_accommodation == "Y":
                    print("Staff cannot be allocated Living Space")
                    return "Staff cannot be allocated Living Space"
                else:
                    if stringcase.pascalcase(designation) == "Staff":
                        person = Staff(first_name, last_name)
                        self.staff.append(person)
                        self.staff_shuffle.append(person)
                        self.people.append(name)
                        self.allocate_office(name)

                    elif stringcase.pascalcase(designation) == "Fellow":
                        person = Fellow(first_name, last_name, wants_accommodation)
                        self.fellows.append(person)
                        self.fellows_shuffle.append(person)
                        self.people.append(name)
                        self.allocate_office(name)
                        self.allocate_living_space(name, wants_accommodation)
            except ValueError:
                print("Incorrect entry. Please enter Y or N")
                return "Incorrect entry. Please enter Y or N"
        except ValueError:
            print("Incorrect entry. Please enter either Staff or Fellow")
            return "Incorrect entry. Please enter either Staff or Fellow"

    def allocate_office(self, name):
        """function to allocate person to room"""
        # add exceptions
        available_offices = [office for office in self.offices if
                             len(office.office_members) < office.max_capacity]
        if available_offices:
            available_office = random.choice(available_offices)
            available_office.office_members.append(name)
            print("{} added to {} office".format(name, available_office.room_name))

        else:
            print("There are no offices available")

    def allocate_living_space(self, name, wants_accommodation):
        available_living_spaces = [living_space for living_space in
                                   self.living_spaces if
                                   len(living_space.living_space_members)
                                   < living_space.max_capacity]
        if available_living_spaces:
            available_living_space = random.choice(available_living_spaces)
            if wants_accommodation == "Y":
                available_living_space.living_space_members.append(name)
                print("{} added to {} living space".format(name,
                                                           available_living_space.room_name))
        else:
            print("There are no living spaces available")

    def reallocate_person(self, first_name, last_name, new_room_name):
        """function to re-allocate person to a new room"""
        try:
            print(self.rooms)
            if new_room_name not in self.rooms:
                raise NameError
            person_name = first_name + last_name
            old_office = [office for office in self.offices if person_name
                          == name in office.office_members]
            new_office = [room for room in self.offices if new_room_name
                          == room.room_name]
            new_office.office_members.append(person_name)
            print("{} reallocated to {} office".format(person_name,
                                                       new_office.room_name))
        except NameError:
            print("Office does not exist")
        # code for living space reallocations to come here

    def load_people(self, text_file):
        """adds people from a text file"""
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
                self.add_person(first_name, last_name, designation, wants_accommodation)

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
