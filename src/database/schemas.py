from pydantic import BaseModel
from typing import Union


class ItemBase(BaseModel):
    title: str
    description: Union[str,  None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    password: str


class User(BaseModel):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
