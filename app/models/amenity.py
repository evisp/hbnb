from app.models.base import BaseModel


class Amenity(BaseModel):
    name: str

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
