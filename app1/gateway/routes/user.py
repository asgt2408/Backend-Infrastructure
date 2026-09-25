from fastapi import APIRouter, Depends, Request

from config import SERVICES
from proxy import forward_request

router = APIRouter()

@router.api_route(
   "/users/{path:path}",
   methods=["GET","POST","PUT","DELETE"],
)

async def user_gateway(
    path: str,
    request :  Request,
):
    return await forward_request(
        request=request,
        service_url=SERVICES["user"],
        path = path,
    )