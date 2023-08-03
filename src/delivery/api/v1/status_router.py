from fastapi import APIRouter
from src.delivery.api.v1.status_response import StatusResponse

status_router = APIRouter()


@status_router.get("/api/v1/status", response_model=StatusResponse)
def status() -> StatusResponse:
    return StatusResponse(ok=True)
