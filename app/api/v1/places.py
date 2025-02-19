from app import facade
from flask_restx import Namespace, Resource, fields

api = Namespace("places", description="Place operations")

# Define the models for related entities
amenity_model = api.model(
    "Amenity",
    {
        "id": fields.String(description="Amenity ID"),
        "name": fields.String(description="Name of the amenity"),
    },
)

user_model = api.model(
    "User",
    {
        "id": fields.String(description="User ID"),
        "first_name": fields.String(description="First name of the owner"),
        "last_name": fields.String(description="Last name of the owner"),
        "email": fields.String(description="Email of the owner"),
    },
)

review_model = api.model(
    "Review",
    {
        "id": fields.String(description="Review ID"),
        "text": fields.String(description="Text of the review"),
        "rating": fields.Integer(description="Rating of the place (1-5)"),
        "user_id": fields.String(description="ID of the user"),
    },
)

# Define the place model for input validation and documentation
place_model = api.model(
    "Place",
    {
        "title": fields.String(
            required=True, description="Title of the place"
        ),
        "description": fields.String(description="Description of the place"),
        "price": fields.Float(required=True, description="Price per night"),
        "latitude": fields.Float(
            required=True, description="Latitude of the place"
        ),
        "longitude": fields.Float(
            required=True, description="Longitude of the place"
        ),
        "owner_id": fields.String(
            required=True, description="ID of the owner"
        ),
        "owner": fields.Nested(user_model, description="Owner details"),
        "amenities": fields.List(
            fields.String, description="List of amenities ID's"
        ),
        "reviews": fields.List(
            fields.String, description="List of reviews ID's"
        ),
    },
)


@api.route("/")
class PlaceList(Resource):
    @api.expect(place_model, validate=True)
    @api.response(201, "Place successfully created")
    @api.response(400, "Invalid input data")
    @api.response(400, "Owner not found")
    def post(self):
        """Register a new place"""
        place_data = api.payload

        existing_owner = facade.get_user(place_data["owner_id"])

        if not existing_owner:
            return {"error": "Owner not found"}, 400

        place_data["owner"] = existing_owner
        place_data.pop("owner_id")
        amenities = place_data.pop("amenities", [])
        reviews = place_data.pop("reviews", [])

        new_place = facade.create_place(place_data)

        for amenity in amenities:
            exists = facade.get_amenity_by_name(amenity)

            if not exists:
                new_amenity = facade.create_amenity({"name": amenity})
                new_place.add_amenity(new_amenity)
            else:
                new_place.add_amenity(amenity)

        for review_data in reviews:
            review = facade.create_review(review_data)

            new_place.add_review(review)

        return {
            "id": new_place.id,
            "title": new_place.title,
            "description": new_place.description,
            "price": new_place.price,
            "latitude": new_place.latitude,
            "longitude": new_place.longitude,
            "owner": {
                "id": new_place.owner.id,
                "first_name": new_place.owner.first_name,
                "last_name": new_place.owner.last_name,
                "email": new_place.owner.email,
            },
            "amenities": [
                {"id": amenity.id, "name": amenity.name}
                for amenity in new_place.amenities
            ],
        }, 201

    @api.response(200, "List of places retrieved successfully")
    def get(self):
        """Retrieve a list of all places"""
        places = facade.get_all_places()

        return [
            {
                "id": place.id,
                "title": place.title,
                "description": place.description,
                "price": place.price,
                "latitude": place.latitude,
                "longitude": place.longitude,
                "owner": {
                    "id": place.owner.id,
                    "first_name": place.owner.first_name,
                    "last_name": place.owner.last_name,
                    "email": place.owner.email,
                },
                "amenities": [
                    {"id": amenity.id, "name": amenity.name}
                    for amenity in place.amenities
                ],
            }
            for place in places
        ]


@api.route("/<place_id>")
class PlaceResource(Resource):
    @api.response(200, "Place details retrieved successfully")
    @api.response(404, "Place not found")
    def get(self, place_id):
        """Get place details by ID"""
        place = facade.get_place(place_id)

        if not place:
            return {"error": "Place not found"}, 404

        return {
            "id": place.id,
            "title": place.title,
            "description": place.description,
            "price": place.price,
            "latitude": place.latitude,
            "longitude": place.longitude,
            "owner": {
                "id": place.owner.id,
                "first_name": place.owner.first_name,
                "last_name": place.owner.last_name,
                "email": place.owner.email,
            },
            "amenities": [
                {"id": amenity.id, "name": amenity.name}
                for amenity in place.amenities
            ],
        }

    @api.expect(place_model)
    @api.response(200, "Place updated successfully")
    @api.response(404, "Place not found")
    @api.response(400, "Invalid input data")
    def put(self, place_id):
        """Update a place's information"""
        place_data = api.payload

        existing_place = facade.get_place(place_id)

        if not existing_place:
            return {"error": "Place not found"}, 404

        existing_owner = facade.get_user(place_data["owner_id"])

        if not existing_owner:
            return {"error": "Owner not found"}, 400

        place_data["owner"] = existing_owner
        place_model.pop("owner_id")

        updated_place = facade.update_place(existing_place, place_data)

        return {
            "id": updated_place.id,
            "title": updated_place.title,
            "description": updated_place.description,
            "price": updated_place.price,
            "latitude": updated_place.latitude,
            "longitude": updated_place.longitude,
            "owner": {
                "id": updated_place.owner.id,
                "first_name": updated_place.owner.first_name,
                "last_name": updated_place.owner.last_name,
                "email": updated_place.owner.email,
            },
            "amenities": [
                {"id": amenity.id, "name": amenity.name}
                for amenity in updated_place.amenities
            ],
        }
