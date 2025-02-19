import unittest
from app.models.review import Review
from app.models.place import Place
from app.models.user import User


class TestReview(unittest.TestCase):

    def setUp(self):
        self.user = User(
            first_name="Test", last_name="User", email="humsuzdeb@wingaeb.no"
        )
        self.place = Place(
            title="Test Place",
            description="A place for testing",
            latitude=50.0,
            longitude=10.0,
            price=100,
            owner=self.user,
        )
        self.review = Review("Great place!", 5, self.place, self.user)

    def test_review_initialization(self):
        self.assertEqual(self.review.text, "Great place!")
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.place, self.place)
        self.assertEqual(self.review.user, self.user)

    def test_review_place_setter(self):
        new_place = Place(
            description="Another place for testing",
            latitude=40.0,
            longitude=20.0,
            owner=self.user,
            price=200,
            title="Another Test Place",
        )
        self.review.place = new_place
        self.assertEqual(self.review.place, new_place)

    def test_review_place_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.review.place = "Not a Place instance"

    def test_review_user_setter(self):
        new_user = User(
            first_name="New", last_name="User", email="zanifami@mepaluka.bb"
        )
        self.review.user = new_user
        self.assertEqual(self.review.user, new_user)

    def test_review_user_setter_invalid(self):
        with self.assertRaises(ValueError):
            self.review.user = "Not a User instance"


if __name__ == "__main__":
    unittest.main()
