from app.models.base import BaseModel


class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()
        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []  # List to store related reviews
        self.amenities = []  # List to store related amenities

    @property
    def owner(self):
        """Getter for owner."""
        return self.__owner

    @owner.setter
    def owner(self, owner):
        """Setter for owner."""
        from app.models.user import User

        if not isinstance(owner, User):
            raise ValueError("owner must be a User instance")

        self.__owner = owner

    @property
    def price(self):
        """Getter for price."""
        return self.__price

    @price.setter
    def price(self, price):
        """Setter for price."""
        if not isinstance(price, (int, float)):
            raise TypeError("price must be an int or float")

        if price < 0:
            raise ValueError("price must be a positive number")

        self.__price = price

    @property
    def latitude(self):
        """Getter for latitude."""
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude):
        """Setter for latitude."""
        if not isinstance(latitude, (int, float)):
            raise TypeError("latitude must be an int or float")

        if latitude < -90 or latitude > 90:
            raise ValueError("latitude must be between -90 and 90")

        self.__latitude = latitude

    @property
    def longitude(self):
        """Getter for longitude."""
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude):
        """Setter for longitude."""
        if not isinstance(longitude, (int, float)):
            raise TypeError("longitude must be an int or float")

        if longitude < -180 or longitude > 180:
            raise ValueError("longitude must be between -180 and 180")

        self.__longitude = longitude

    def add_review(self, review):
        """Add a review to the place."""
        from app.models.review import Review

        if not isinstance(review, Review):
            raise ValueError("review must be a Review instance")

        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        from app.models.amenity import Amenity

        if not isinstance(amenity, Amenity):
            raise ValueError("amenity must be an Amenity instance")

        self.amenities.append(amenity)
