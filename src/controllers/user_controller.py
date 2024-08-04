from fastapi import Depends, HTTPException, APIRouter
from src.database import crud, schemas
from sqlalchemy.orm import Session
from ..database.db_config import get_db_connection



routes = APIRouter()


@routes.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db_connection)):
    db_user = crud.get_user_by_email(db, email=user.email)
    
    raise HTTPException(status_code=400, detail="Email already registered")
    
    user_created = crud.create_user(db=db, user=user)
    print("user_created", user_created)
    return user_created


@routes.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@routes.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db_connection)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@routes.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db_connection)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@routes.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db_connection)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items