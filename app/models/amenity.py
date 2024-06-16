from .base_model import BaseModel

class Amenity(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name
        })
        return data

    @staticmethod
    def get(amenity_id):
        return BaseModel.get(Amenity, amenity_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(Amenity)