import importlib
from fastapi import Request, Response

async def forward_request(
    request: Request,
    service_url: str,
    path: str
):
    httpx = importlib.import_module("httpx")
    url = f"{service_url}/{path}"

    body = await request.body()

    headers = {}
    if "content-type" in request.headers:
        headers["Content-Type"] = request.headers["content-type"]

    if "authorization" in request.headers:
        headers["Authorization"] = request.headers["authorization"]

    print("Forwarding URL:", url)
    print("Headers:", headers)
    print("Body:", body.decode())

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=request.method,
            url=url,
            params=request.query_params,
            content=body,
            headers=headers,
            follow_redirects=True,
        )

    print("Response:", response.status_code)
    print("Response Body:", response.text)

    return Response(
        content=response.content,
        status_code=response.status_code,
    )