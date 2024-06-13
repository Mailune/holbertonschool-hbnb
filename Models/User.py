#!/usr/bin/python3


from BaseEntity import BaseEntity


class User(BaseEntity):
    emails = set()  # attribute to store unique emails

    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        if email in User.emails:
            raise ValueError("Email already exists")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        User.emails.add(email)

    def update_email(self, new_email):
        if new_email in User.emails:
            raise ValueError("Email already exists")
        User.emails.remove(self.email)
        self.email = new_email
        User.emails.add(new_email)
        self.save()

    def update_first_name(self, new_first_name):
        self.first_name = new_first_name
        self.save()

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
        self.save()

    def update_password(self, new_password):
        self.password = new_password
        self.save()

    def delete(self):
        User.emails.remove(self.email)
        super().delete()
