from .base_model import BaseModel

class Review(BaseModel):
    def __init__(self, user_id, place_id, rating, comment):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'user_id': self.user_id,
            'place_id': self.place_id,
            'rating': self.rating,
            'comment': self.comment
        })
        return data

    @staticmethod
    def get(review_id):
        return BaseModel.get(Review, review_id)

    @staticmethod
    def get_all():
        return BaseModel.get_all(Review)
