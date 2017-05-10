class Room(object):

    def __init__(self, room_names, room_type):
        self.room_name = room_names
        self.room_type = room_type


class LivingSpace(Room):
    living_space_members = []
    max_capacity = 4

    def __init__(self, room_names):
        Room.__init__(self, room_names, "living space")


class Office(Room):
    office_members = []
    max_capacity = 6

    def __init__(self, room_names):
        Room.__init__(self, room_names, "office")
