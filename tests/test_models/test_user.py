import unittest
from app.models.base import BaseModel
from app.models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            is_admin=True,
        )

    def test_user_creation(self):
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertTrue(self.user.is_admin)

    def test_default_is_admin(self):
        user = User(
            first_name="Jane", last_name="Doe", email="jane.doe@example.com"
        )
        self.assertFalse(user.is_admin)

    def test_user_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
