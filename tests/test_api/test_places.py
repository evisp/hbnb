from app import create_app, facade
import unittest
import json


class TestPlacesAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.facades = facade
        self.headers = {"Content-Type": "application/json"}

    def test_create_place(self):
        owner = self.facades.create_user(
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
            }
        )

        place_data = {
            "title": "Test Place",
            "description": "A nice place to stay",
            "price": 100.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": owner.id,
        }
        response = self.client.post(
            "/api/v1/places/",
            data=json.dumps(place_data),
            headers=self.headers,
        )

        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["owner"]["id"], owner.id)
        self.assertEqual(response.json["title"], place_data["title"])
        self.assertEqual(
            response.json["description"], place_data["description"]
        )
        self.assertEqual(response.json["price"], place_data["price"])
        self.assertEqual(response.json["latitude"], place_data["latitude"])
        self.assertEqual(response.json["longitude"], place_data["longitude"])
        self.assertEqual(response.json["owner"]["id"], place_data["owner_id"])

    def test_get_all_places(self):
        response = self.client.get("/api/v1/places/")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_get_place_by_id(self):
        place_id = "place123"
        response = self.client.get(f"/api/v1/places/{place_id}")
        if response.status_code == 200:
            self.assertIn("id", response.json)
        else:
            self.assertEqual(response.status_code, 404)

    def test_update_place(self):

        owner = self.facades.create_user(
            {
                "first_name": "John",
                "last_name": "Doe",
                "email": "john.doe@example.com",
            }
        )

        place = self.facades.create_place(
            {
                "title": "Test Place",
                "description": "A nice place to stay",
                "price": 100.0,
                "latitude": 40.7128,
                "longitude": -74.0060,
                "owner": owner,
            }
        )

        update_data = {
            "title": "Updated Place",
            "description": "An updated description",
            "price": 150.0,
            "latitude": 40.7128,
            "longitude": -74.0060,
            "owner_id": owner.id,
        }
        response = self.client.put(
            f"/api/v1/places/{place.id}",
            data=json.dumps(update_data),
            headers=self.headers,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("id", response.json)


if __name__ == "__main__":
    unittest.main()
