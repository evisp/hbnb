from app.models.base import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    is_admin: bool

    def __init__(self, first_name, last_name, email, is_admin=False) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
