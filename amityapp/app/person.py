class Person(object):

    def __init__(self, first_name, last_name, designation, wants_accommodation):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.wants_accommodation = wants_accommodation


class Fellow(Person):

    def __init__(self, first_name, last_name, wants_accommodation):
        Person.__init__(self, first_name, last_name, "Fellow")


class Staff(Person):

    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name, "Staff", "N")
