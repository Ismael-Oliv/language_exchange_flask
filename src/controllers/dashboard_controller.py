from fastapi import APIRouter, Request, Response



routes = APIRouter(prefix="/home")


@routes.get("/")
async def index(request: Request,  response: Response):
    pass