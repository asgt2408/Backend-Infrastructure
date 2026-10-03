from fastapi import APIRouter, Depends, Request

from config import SERVICES
from proxy import forward_request

router = APIRouter()

@router.api_route(
   "/driver/{path:path}",
   methods=["GET","POST","PUT","DELETE"],
)

async def driver_gateway(
    path: str,
    request :  Request,
):
    return await forward_request(
        request=request,
        service_url=SERVICES["driver"],
        path = path,
    )