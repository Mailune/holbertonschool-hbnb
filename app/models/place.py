from .base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, num_rooms, num_bathrooms, price_per_night, max_guests):
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'description': self.description,
            'address': self.address,
            'city_id': self.city_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'host_id': self.host_id,
            'num_rooms': self.num_rooms,
            'num_bathrooms': self.num_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests
        })
        return data

    @staticmethod
    def get(place_id):
        return BaseModel.get(Place, place_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(Place)
