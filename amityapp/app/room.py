class Room(object):

    def __init__(self, room_names, room_type):
        self.room_name = room_names
        self.room_type = room_type


class LivingSpace(Room):
    living_space_members = []

    def __init__(self, room_names, max_people=4):
        Room.__init__(self, room_names, "living space")


class Office(Room):
    office_members = []

    def __init__(self, room_names, max_people=6):
        Room.__init__(self, room_names, "office")
