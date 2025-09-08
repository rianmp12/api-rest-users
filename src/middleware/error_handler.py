from fastapi import Request, Response
from fastapi.responses import JSONResponse
import traceback

async def catch_all_exceptions(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "data": None,
                "pagination": None,
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": "An unexpected error occurred",
                    "details": str(exc),
                },
            },
        )
