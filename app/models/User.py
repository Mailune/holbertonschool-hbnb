from .base_model import BaseModel

class User(BaseModel):
    def __init__(self, email, first_name, last_name, password=None):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save(self):
        if not self.is_email_unique():
            raise ValueError("Email already exists.")
        super().save()

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'password': self.password  # Note: Password should be hashed in a real application
        })
        return data

    def is_email_unique(self):
        users = User.get_all()  # Call get_all() without passing User
        for user in users:
            if user.email == self.email and user.id != self.id:
                return False
        return True

    @staticmethod
    def get(user_id):
        return BaseModel.get(User, user_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(User)
