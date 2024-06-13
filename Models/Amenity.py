#!/usr/bin/python3


from BaseEntity import BaseEntity


class Amenity(BaseEntity):
    def __init__(self, name):
        super().__init__()
        self.name = name
