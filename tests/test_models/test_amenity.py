import unittest
from app.models.amenity import Amenity
from app.models.base import BaseModel


class TestAmenity(unittest.TestCase):
    def test_amenity_initialization(self):
        amenity = Amenity(name="Pool")
        self.assertEqual(amenity.name, "Pool")

    def test_amenity_inheritance(self):
        amenity = Amenity(name="WiFi")
        self.assertTrue(isinstance(amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
