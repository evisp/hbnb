from app import create_app, facade
from app.models.user import User
import unittest


class TestUserAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.facade = facade

    def test_get_users(self):
        response = self.client.get("/api/v1/users/")
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        user_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com",
        }
        response = self.client.post("/api/v1/users/", json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["first_name"], "Jane")
        self.assertEqual(response.json["last_name"], "Doe")
        self.assertEqual(response.json["email"], "jane.doe@example.com")

    def test_get_user_by_id(self):
        user = self.facade.create_user(
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "email": "alice.smith@example.com",
            }
        )

        response = self.client.get(f"/api/v1/users/{user.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["first_name"], "Alice")
        self.assertEqual(response.json["last_name"], "Smith")
        self.assertEqual(response.json["email"], "alice.smith@example.com")

    def test_update_user(self):
        user = self.facade.create_user(
            {
                "first_name": "Bob",
                "last_name": "Brown",
                "email": "bob.brown@example.com",
            }
        )
        updated_data = {
            "first_name": "Robert",
            "last_name": "Brown",
            "email": "bob.brown@example.com",
        }
        response = self.client.put(
            f"/api/v1/users/{user.id}", json=updated_data
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["first_name"], "Robert")
        self.assertEqual(response.json["last_name"], "Brown")
        self.assertEqual(response.json["email"], "bob.brown@example.com")

    def test_user_not_found(self):
        response = self.client.get("/api/v1/users/999")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["error"], "User not found")


if __name__ == "__main__":
    unittest.main()
