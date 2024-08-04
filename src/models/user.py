import uuid
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(type=str)
    email: str = Field(type=str)
    password: str = Field(type=str)

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "name": "Jhon Doe",
                "email": "jhondoe@exemple.com",
                "password": "as4d56sa4da56d4"
            }
        }
