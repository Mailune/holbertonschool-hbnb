# /usr/bin/python3


from BaseEntity import BaseEntity
from User import User
from Place import Place


class Review(BaseEntity):
    def __init__(self, user, place, comment):
        super().__init__()
        if isinstance(user, User) is False:
            raise ValueError("user must be an instance of User")
        if isinstance(place, Place) is False:
            raise ValueError("place must be an instance of Place")
        self.user = user
        self.place = place
        self.comment = comment

    def update_comment(self, new_comment):
        self.comment = new_comment
        self.save()
