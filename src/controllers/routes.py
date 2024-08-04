from fastapi import APIRouter
from . import dashboard_controller, user_controller


router = APIRouter()

router.include_router(dashboard_controller.routes, prefix="/dashboard")
router.include_router(user_controller.routes, prefix="/users")
