#!/usr/bin/python3


from BaseEntity import BaseEntity
from User import User
from Amenity import Amenity


class Place(BaseEntity):
    def __init__(
        self,
        owner,
        city_id,
        name,
        description,
        number_rooms,
        number_bathrooms,
        max_guest,
        price_by_night,
        latitude,
        longitude,
    ):
        super().__init__()
        self.owner = owner
        self.city_id = city_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []

    def add_amenity(self, amenity):
        if isinstance(amenity, Amenity):
            self.amenities.append(amenity)
        else:
            return False
        return True

    def delete_amenity(self, amenity):
        if isinstance(amenity, Amenity) and amenity in self.amenities:
            self.amenities.remove(amenity)
            return True
        return False
