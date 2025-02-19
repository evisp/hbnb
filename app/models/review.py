from app.models.base import BaseModel


class Review(BaseModel):
    text: str
    rating: int
    place: str
    user: str

    def __init__(self, text, rating, place, user) -> None:
        super().__init__()
        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    @property
    def place(self):
        """Getter for place."""
        return self.__place

    @place.setter
    def place(self, place):
        """Setter for place."""
        from app.models.place import Place

        if not isinstance(place, Place):
            raise ValueError("place must be a Place instance")

        self.__place = place

    @property
    def user(self):
        """Getter for user."""
        return self.__user

    @user.setter
    def user(self, user):
        """Setter for user."""
        from app.models.user import User

        if not isinstance(user, User):
            raise ValueError("user must be a User instance")

        self.__user = user
