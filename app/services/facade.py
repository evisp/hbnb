from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review
from app.models.user import User
from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id: str) -> User | None:
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email: str) -> User | None:
        return self.user_repo.get_by_attribute("email", email)

    def get_users(self) -> list[User]:
        return self.user_repo.get_all()

    def update_user(self, user: User, user_data: dict) -> User:
        user.update(user_data)
        return user

    # -------------------------------------------

    def create_amenity(self, amenity_data: dict) -> Amenity:
        amenity = Amenity(**amenity_data)

        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id: str) -> Amenity | None:
        return self.amenity_repo.get(amenity_id)

    def get_amenity_by_name(self, name: str) -> Amenity | None:
        return self.amenity_repo.get_by_attribute("name", name)

    def get_all_amenities(self) -> list[Amenity]:
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity: Amenity, amenity_data: dict) -> Amenity:
        amenity.update(amenity_data)
        return amenity

    # -------------------------------------------

    def create_place(self, place_data: dict) -> Place:
        place = Place(**place_data)
        self.place_repo.add(place)

        return place

    def get_place(self, place_id: str) -> Place | None:
        return self.place_repo.get(place_id)

    def get_all_places(self) -> list[Place]:
        return self.place_repo.get_all()

    def update_place(self, place: Place, place_data: dict) -> Place:
        place.update(place_data)
        return place

    # -------------------------------------------

    def create_review(self, review_data: dict) -> Review:
        review = Review(**review_data)
        self.review_repo.add(review)

        return review

    def get_review(self, review_id: str) -> Review | None:
        return self.review_repo.get(review_id)

    def get_all_reviews(self) -> list[Review]:
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return self.review_repo.get_by_attribute("place_id", place_id)

    def update_review(self, review, review_data):
        review.update(review_data)
        return review

    def delete_review(self, review):
        self.review_repo.delete(review)
        return True
