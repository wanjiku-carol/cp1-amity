from abc import ABCMeta


class Room(object):
    """creates room object from where living space and office inherit """
    __metaclass__ = ABCMeta
    max_capacity = 0

    def __init__(self, room_names, room_type):
        self.room_name = room_names
        self.room_type = room_type


class LivingSpace(Room):
    """inherits from Room class"""
    living_space_members = []
    max_capacity = 4

    def __init__(self, room_names):
        Room.__init__(self, room_names, "living space")


class Office(Room):
    """inherits from Room class"""
    office_members = []
    max_capacity = 6

    def __init__(self, room_names):
        Room.__init__(self, room_names, "office")
