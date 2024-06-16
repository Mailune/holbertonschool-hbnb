from .base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'code': self.code
        })
        return data

    @staticmethod
    def get(country_id):
        return BaseModel.get(Country, country_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(Country)
