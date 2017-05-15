import random
import os
import os.path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.room import Office, LivingSpace
from app.person import Fellow, Staff
from app.models import Persons, Rooms, Base


class Amity(object):

    def __init__(self):
        self.fellows = []
        self.staff = []
        self.people = []
        self.offices = []
        self.offices_with_members = []
        self.office_members = {}
        self.unallocated_offices = []
        self.living_spaces = []
        self.living_spaces_with_mem = []
        self.living_mem = {}
        self.unallocated_living = []
        self.rooms = []
        self.office_allocations = {}
        self.living_space_allocations = {}

    def create_room(self, room_type, room_name):
        """function to create a room."""
        try:
            if not room_type.title() == "Office" and not room_type.title() ==\
                    "Livingspace":
                raise NameError
            if room_name in self.rooms:
                print("{} already exists". format(room_name))
            else:
                if room_type.title() == "Office":
                    room = Office(room_name)
                    self.offices.append(room)
                    self.rooms.append(room_name)
                    print("{} office created successfully".format(room.room_name.upper()))
                    return ("{} office created successfully".format(room.room_name.upper()))
                elif room_type.title() == "Livingspace":
                    room = LivingSpace(room_name)
                    self.living_spaces.append(room)
                    self.rooms.append(room_name)
                    print("{} living space created successfully".format(room.room_name.upper()))
                    return "{} living space created successfully".format(room.room_name.upper())
        except NameError:
            print("invalid entry. Please enter office or living space")
            return "invalid entry. Please enter office or living space"

    def add_person(self, first_name, last_name, designation,
                   wants_accommodation="N"):
        """add person to system and allocates a random room"""

        if not isinstance(first_name, str) and not isinstance(last_name, str):
            print("Incorrect entry. Name cannot have special characters")
        name = first_name + " " + last_name
        if not designation == "Staff" and not designation == "Fellow":
            print("Incorrect entry. Please enter staff or fellow")
        else:
            if designation == "Staff" and wants_accommodation == "Y":
                print("Staff cannot be allocated Living Space")
        if name in self.people:
            print("{} already exists".format(name.upper()))
        else:
            if designation.title() == "Staff":
                person = Staff(first_name, last_name)
                self.staff.append(person)
                self.people.append(name)
                self.allocate_office(name)

            elif designation.title() == "Fellow":
                person = Fellow(first_name, last_name, wants_accommodation)
                self.fellows.append(person)
                self.people.append(name)
                self.allocate_office(name)
                self.allocate_living_space(name, wants_accommodation)

    def allocate_office(self, name):
        """function to allocate person to office"""
        available_offices = [office for office in self.offices if
                             len(office.office_members) < office.max_capacity]
        if available_offices:
            available_office = random.choice(available_offices)
            for office in self.offices:
                if name in office.office_members:
                    break
                else:
                    available_office.office_members.append(name)
                    self.offices_with_members.append(available_office)
                    print("{} added to {} office".format(
                        name.upper(), available_office.room_name.upper()))
                    print("Successful!")

        else:
            print("There are no offices available. {} added to unallocated list".format(name))
            self.unallocated_offices.append(name)

    def allocate_living_space(self, name, wants_accommodation="N"):
        """allocate fellow to living space"""
        available_living_spaces = [living_space for living_space in
                                   self.living_spaces if
                                   len(living_space.living_space_members)
                                   < living_space.max_capacity]
        if available_living_spaces:
            available_living_space = random.choice(available_living_spaces)
            if wants_accommodation == "Y":
                for living_space in self.living_spaces:
                    if name not in living_space.living_space_members:
                        available_living_space.living_space_members.append(name)
                        self.living_spaces_with_mem.append(available_living_space)
                        self.living_mem[available_living_space] = available_living_space.living_space_members
                        print("{} added to {} living space".format(name,
                                                                   available_living_space.room_name))
                        print("Successful!")
        else:
            print("There are no living spaces available. {} added to unallocated list")
            self.unallocated_living.append(name)

    def reallocate_person(self, first_name, last_name, new_room_name):
        """function to re-allocate person to a new room"""
        full_name = first_name + " " + last_name
        available_offices = [office for office in self.offices if
                             len(office.office_members) < office.max_capacity]
        available_living_spaces = [living_space for living_space in
                                   self.living_spaces if
                                   len(living_space.living_space_members)
                                   < living_space.max_capacity]

        if full_name not in self.people:
            print("Person does not exist")
        elif new_room_name not in self.rooms:
            print("Room does not exist")
        else:
            for available_living_space in available_living_spaces:
                if new_room_name == available_living_space.room_name:
                    print("Cannot reallocate from office to living space")
                else:
                    for keys, values in self.office_members.items():
                        if full_name in values:
                            if new_room_name == keys.room_name:
                                print("Cannot reallocate to the same room")
                            else:
                                keys.office_members.remove(full_name)
                                for available_office in available_offices:
                                    if new_room_name == available_office.room_name:
                                        available_office.office_members.append(full_name)
                                        print("{} reallocated to {} office".format(full_name,
                                                                                   new_room_name))
            for available_office in available_offices:
                if new_room_name == available_office.room_name:
                    pass
                else:
                    for keys, values in self.living_mem.items():
                        if full_name in values:
                            if new_room_name == keys.room_name:
                                print("Cannot reallocate to the same room")
                            else:
                                keys.living_space_members.remove(full_name)
                                for available_living_space in available_living_spaces:
                                    if new_room_name == available_living_space.room_name:
                                        available_living_space.living_space_members.append(
                                            full_name)
                                        print("{} reallocated to {} living space".format(full_name,
                                                                                         new_room_name))

    def load_people(self, text_file):
        """adds people from a text file"""
        if os.path.isfile(text_file) is False:
            print("File does not exist")
        else:
            with open(text_file, 'r') as txt_file:
                if (os.stat(text_file).st_size == 0):
                    print('File is empty!')
                else:
                    file_name = txt_file.readlines()
                    for sentence in file_name:
                        words = sentence.split()
                        if len(words) == 3:
                            first_name = words[0].title()
                            last_name = words[1].title()
                            designation = words[2].title()
                            wants_accommodation = "N"
                            self.add_person(first_name, last_name, designation,
                                            wants_accommodation)
                        elif len(words) == 4:
                            first_name = words[0].title()
                            last_name = words[1].title()
                            designation = words[2].title()
                            wants_accommodation = words[3].title()
                            self.add_person(first_name, last_name, designation,
                                            wants_accommodation)

    def load_state(self, db_name):
        """loads data from database into application"""
        if db_name:
            engine = create_engine('sqlite:///{}'.format(db_name))
        else:
            engine = create_engine('sqlite:///amity.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        if db_name is None:
            db_name = 'amity.db'
        print("========People in Database==========")
        for person in session.query(Persons) .order_by(Persons.id):
            print(person.id, person.first_name, person.last_name,
                  person.designation, person.wants_accommodation)
        print("========Rooms in Database==========")
        for room in session.query(Rooms).order_by(Rooms.id):
            print(room.id, room.room_name, room.room_type)

    def save_state(self, db_name):
        """Persists all the data stored in the app to a SQLite database"""
        if db_name:
            engine = create_engine('sqlite:///{}'.format(db_name))
        else:
            engine = create_engine('sqlite:///amity.db')

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        if db_name is None:
            db_name = 'amity.db'

        for person in self.staff:
            staff_user = Persons(first_name=person.first_name,
                                 last_name=person.last_name,
                                 designation=person.designation,
                                 wants_accommodation=person.wants_accommodation)
            session.add(staff_user)
        for fellow in self.fellows:
            fellow_user = Persons(first_name=fellow.first_name,
                                  last_name=fellow.last_name,
                                  designation=fellow.designation,
                                  wants_accommodation=fellow.wants_accommodation)
            session.add(fellow_user)

        for office in self.offices:
            off_add = Rooms(room_name=office.room_name,
                            room_type=office.room_type)
            session.add(off_add)
        for living_space in self.living_spaces:
            livi_spac_add = Rooms(room_name=living_space.room_name,
                                  room_type=living_space.room_type)
            session.add(livi_spac_add)
        session.commit()
        session.close()
        print("Save Successful")

    def print_allocations(self, file_name):
        """prints a list of allocations"""
        for key_off, value_off in self.office_members.items():
            if not file_name:
                print(key_off.room_name)
                print("-------------------------")
                print(", ".join(value_off))
            else:
                if os.path.isfile(file_name) is False:
                    print("File does not exist")
                else:
                    with open(file_name, 'w') as file_open:
                        file_open.write("{}: {}\n".format(key_off.room_name,
                                                          ", ".join(value_off)))
                        file_open.close()
        for key_liv, value_liv in self.living_mem.items():
            if not file_name:
                print(key_liv.room_name)
                print("-------------------------")
                print(", ".join(value_liv))
            else:
                if os.path.isfile(file_name) is False:
                    print("File does not exist")
                else:
                    with open(file_name, 'w') as file_open:
                        file_open.write("{}: {}\n".format(key_liv.room_name,
                                                          ", ".join(value_liv)))
                        file_open.close()

    def print_unallocated(self, file_name):
        """prints a list of unallocated people"""
        if not file_name:
            if not self.unallocated_offices:
                print("There is no one awaiting allocation to office")
            if not self.unallocated_living:
                print("There is no one awaiting allocation to living space")
            print("=====awaiting allocation to office ======")
            print(", ".join(self.unallocated_offices))
            print("=====awaiting allocation to living space =====")
            print(", ".join(self.unallocated_living))
        else:
            if os.path.isfile(file_name) is False:
                print("File does not exist")
            else:
                with open(file_name, 'w') as file_open:
                    file_open.write("=====awaiting allocation to office ======")
                    file_open.write(", ".join(self.unallocated_offices))
                    file_open.write("=====awaiting allocatopn to living space =====")
                    file_open.write(", ".join(self.unallocated_living))
                    file_open.close()

    def print_room(self, room_name):
        """prints names of people in room"""
        for office in self.offices:
            if room_name == office.room_name:
                print(", ".join(office.office_members))
        for living_space in self.living_spaces:
            if room_name == living_space.room_name:
                print(", ".join(living_space.living_space_members))
