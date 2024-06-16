import uuid
from datetime import datetime
from app.persistence.data_manager import DataManager

storage = DataManager()

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        storage.save(self)

    def delete(self):
        storage.delete(self.id, self.__class__.__name__)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    @staticmethod
    def get(cls, object_id):
        data = storage.get(object_id, cls.__name__)
        if data:
            obj = cls.__new__(cls)
            obj.__dict__.update(data)
            obj.created_at = datetime.fromisoformat(data['created_at'])
            obj.updated_at = datetime.fromisoformat(data['updated_at'])
            return obj
        return None

    @staticmethod
    def get_all(cls):
        data = storage.get_all(cls.__name__)
        objects = []
        for item in data:
            obj = cls.__new__(cls)
            obj.__dict__.update(item)
            obj.created_at = datetime.fromisoformat(item['created_at'])
            obj.updated_at = datetime.fromisoformat(item['updated_at'])
            objects.append(obj)
        return objects
