from abc import ABCMeta


class Room(object):
    """creates room object from where living space and office inherit """
    __metaclass__ = ABCMeta
    max_capacity = 0
    members = []

    def __init__(self, room_name, room_type):
        self.room_name = room_name
        self.room_type = room_type


class LivingSpace(Room):
    """inherits from Room class"""
    # living_space_members = []
    max_capacity = 4

    def __init__(self, room_name):
        Room.__init__(self, room_name, "livingspace")


class Office(Room):
    """inherits from Room class"""
    # office_members = []
    max_capacity = 6

    def __init__(self, room_name):
        Room.__init__(self, room_name, "office")
