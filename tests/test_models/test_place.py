import unittest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review
from app.models.amenity import Amenity


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User(
            first_name="Test", last_name="User", email="ovolumu@ciwjiuge.gh"
        )
        self.place = Place(
            title="Test Place",
            description="A place for testing",
            price=100,
            latitude=50.0,
            longitude=10.0,
            owner=self.user,
        )

    def test_initialization(self):
        self.assertEqual(self.place.title, "Test Place")
        self.assertEqual(self.place.description, "A place for testing")
        self.assertEqual(self.place.price, 100)
        self.assertEqual(self.place.latitude, 50.0)
        self.assertEqual(self.place.longitude, 10.0)
        self.assertEqual(self.place.owner, self.user)
        self.assertEqual(self.place.reviews, [])
        self.assertEqual(self.place.amenities, [])

    def test_owner_setter(self):
        new_user = User(
            first_name="New", last_name="User", email="mizuc@suku.lt"
        )
        self.place.owner = new_user
        self.assertEqual(self.place.owner, new_user)
        with self.assertRaises(ValueError):
            self.place.owner = "Not a User"

    def test_price_setter(self):
        self.place.price = 200
        self.assertEqual(self.place.price, 200)
        with self.assertRaises(TypeError):
            self.place.price = "Not a number"
        with self.assertRaises(ValueError):
            self.place.price = -100

    def test_latitude_setter(self):
        self.place.latitude = 40.0
        self.assertEqual(self.place.latitude, 40.0)
        with self.assertRaises(TypeError):
            self.place.latitude = "Not a number"
        with self.assertRaises(ValueError):
            self.place.latitude = -100.0
        with self.assertRaises(ValueError):
            self.place.latitude = 100.0

    def test_longitude_setter(self):
        self.place.longitude = 20.0
        self.assertEqual(self.place.longitude, 20.0)
        with self.assertRaises(TypeError):
            self.place.longitude = "Not a number"
        with self.assertRaises(ValueError):
            self.place.longitude = -200.0
        with self.assertRaises(ValueError):
            self.place.longitude = 200.0

    def test_add_review(self):
        review = Review(
            place=self.place, text="Great place!", rating=5, user=self.user
        )
        self.place.add_review(review)
        self.assertIn(review, self.place.reviews)
        with self.assertRaises(ValueError):
            self.place.add_review("Not a Review")

    def test_add_amenity(self):
        amenity = Amenity(name="WiFi")
        self.place.add_amenity(amenity)
        self.assertIn(amenity, self.place.amenities)
        with self.assertRaises(ValueError):
            self.place.add_amenity("Not an Amenity")


if __name__ == "__main__":
    unittest.main()
