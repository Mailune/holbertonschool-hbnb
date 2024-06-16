from .base_model import BaseModel

class City(BaseModel):
    def __init__(self, name, country_code, description=None):
        super().__init__()
        self.name = name
        self.country_code = country_code
        self.description = description

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_code': self.country_code,
            'description': self.description
        })
        return data

    @staticmethod
    def get(city_id):
        return BaseModel.get(City, city_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(City)
