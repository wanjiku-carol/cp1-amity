import random

from app.room import Office, LivingSpace
from app.person import Fellow, Staff
from app.models import Persons, Rooms, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///amity.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Amity(object):

    def __init__(self):
        self.fellows = []
        self.staff = []
        self.people = []
        self.offices = []
        self.offices_with_members = []
        self.living_spaces = []
        self.living_spaces_with_mem = []
        self.rooms = []
        self.office_allocations = {}
        self.living_space_allocations = {}

    def create_room(self, room_type, room_name):
        """function to create a room."""
        try:
            if room_type.title() != "Office" and\
                    room_type.title() != "Livingspace":
                raise NameError
            if room_name in self.rooms:
                print("{} already exists". format(room_name))
            else:
                if room_type.title() == "Office":
                    room = Office(room_name)
                    self.offices.append(room)
                    self.rooms.append(room_name)
                    print(self.rooms)
                    print("Offices created successfully")
                    return "Offices created successfully"
                elif room_type.title() == "Livingspace":
                    room = LivingSpace(room_name)
                    self.living_spaces.append(room)
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
            except ValueError:
                print("Incorrect entry. Please enter Y or N")
                return "Incorrect entry. Please enter Y or N"
        except ValueError:
            print("Incorrect entry. Please enter either Staff or Fellow")
            return "Incorrect entry. Please enter either Staff or Fellow"

    def allocate_office(self, name):
        """function to allocate person to room"""
        available_offices = [office for office in self.offices if
                             len(office.office_members) < office.max_capacity]
        if len(available_offices) > 0:
            available_office = random.choice(available_offices)
            available_office.office_members.append(name)
            self.offices_with_members.append(available_office)
            print("{} added to {} office".format(name, available_office.room_name))
            print("Successful!")

        else:
            print("There are no offices available")

    def allocate_living_space(self, name, wants_accommodation):
        available_living_spaces = [living_space for living_space in
                                   self.living_spaces if
                                   len(living_space.living_space_members)
                                   < living_space.max_capacity]
        if len(available_living_spaces) > 0:
            available_living_space = random.choice(available_living_spaces)
            if wants_accommodation == "Y":
                available_living_space.living_space_members.append(name)
                self.living_spaces_with_mem.append(available_living_space)
                print("{} added to {} living space".format(name,
                                                           available_living_space.room_name))
                print("Successful!")
        else:
            print("There are no living spaces available")

    def reallocate_person(self, first_name, last_name, new_room_name):
        """function to re-allocate person to a new room"""
        full_name = first_name + last_name
        available_offices = [office for office in self.offices if
                             len(office.office_members) < office.max_capacity]
        available_living_spaces = [living_space for living_space in
                                   self.living_spaces if
                                   len(living_space.living_space_members)
                                   < living_space.max_capacity]
        for office in self.offices_with_members:
            for name in office.office_members:
                for available_office in available_offices:
                    if full_name == name:
                        if new_room_name == available_office.room_name:
                            available_office.office_members.append(full_name)
                            office.office_members.remove(name)
                            print("{} successfully reallocated to {}".
                                  format(full_name, new_room_name))
                            print(available_office.office_members)

        for living_space_rm in self.living_spaces_with_mem:
            for name in living_space_rm.living_space_members:
                for available_living_space in available_living_spaces:
                    if full_name == name:
                        if new_room_name == available_living_space.room_name:
                            available_living_space.living_space_members.append(full_name)
                            living_space_rm.living_space_members.remove(name)
                            print("{} successfully reallocated to {}".format(full_name,
                                                                             new_room_name))
                            print(available_living_space.living_space_members)
                        else:
                            return("{} room not available".format(new_room_name))

    def load_people(self, text_file):
        """adds people from a text file"""
        with open(text_file) as txt_file:
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
        for person in session.query(Persons) .order_by(Persons.id):
            print("========People in Database==========")
            print(person.id, person.first_name, person.last_name,
                  person.wants_accommodation)
        for room in session.query(Rooms).order_by(Rooms.id):
            print("========Rooms in Database==========")
            print(room.id, room.room_name, room.room_type)

    def save_state(self, db_name):
        """Persists all the data stored in the app to a SQLite database"""
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

    def print_allocations(self, file_name):
        """prints a list of allocations"""
        file_open = open(file_name, 'w')
        for office in self.offices:
            if len(office.office_members) > 0:
                print(office.room_name)
                print(office.office_members)
                file_open.write("{}: {}\n".format(office.room_name, office.office_members))
        for living_space in self.living_spaces:
            if len(living_space.living_space_members) > 0:
                print(living_space.room_name)
                print(living_space.living_space_members)
                file_open.write("{}: {}\n".format(living_space.room_name,
                                                  living_space.living_space_members))

    def print_unallocated(self):
        """prints a list of unallocated people"""
        for fellow in self.fellows:
            fellow_name = fellow.first_name + fellow.last_name
            for staff_p in self.staff:
                staff_name = staff_p.first_name + staff_p.last_name
                for office in self.offices:
                    for living_space in self.living_spaces:
                        if fellow.wants_accommodation == "Y" and fellow_name\
                                not in living_space.living_space_members:
                            print(fellow_name)
                    if fellow_name and staff_name not in office.office_members:
                        print(fellow_name)
                        print(staff_name)

    def print_room(self, room_name):
        """prints names of people in room"""
        for office in self.offices:
            print(office.room_name)
            print(office.office_members)
        for living_space in self.living_spaces:
            print(living_space.room_name)
            print(living_space.living_space_members)
