from fastapi import FastAPI, Request, Response
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse
from src.database import models
from src.database.db_config import SessionLocal, engine
from src.controllers.routes import router

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    request.state.db.rollback()
    return JSONResponse({"error": str(exc.detail)}, status_code=exc.status_code)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        request.state.db.begin()
        print("Started process")
        response = await call_next(request)
        print("Process committed")
        request.state.db.commit()

    except Exception as E:
        print("Exception", E)
        request.state.db.rollback()

    finally:
        request.state.db.close()

    return response


app.include_router(router=router)
