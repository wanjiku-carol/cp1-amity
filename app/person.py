from abc import ABCMeta


class Person(object):
    """creates a person object from where the fellow and
    staff subclasses inherit"""

    __metaclass__ = ABCMeta

    def __init__(self, first_name, last_name, designation, wants_accommodation):
        self.first_name = first_name
        self.last_name = last_name
        self.designation = designation
        self.wants_accommodation = wants_accommodation


class Fellow(Person):
    """inherits from Person Class"""

    def __init__(self, first_name, last_name, wants_accommodation):
        Person.__init__(self, first_name, last_name, "Fellow", wants_accommodation)


class Staff(Person):
    """inherits from Person Class"""

    def __init__(self, first_name, last_name):
        Person.__init__(self, first_name, last_name, "Staff", "N")
