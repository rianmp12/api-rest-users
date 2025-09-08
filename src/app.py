import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.routers.users import router as users_router
from src.middleware.error_handler import catch_all_exceptions

load_dotenv()

app = FastAPI(title="Users API", version="1.0.0")

origins = (os.getenv("CORS_ORIGINS") or "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins if o.strip()],
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    from time import perf_counter
    t0 = perf_counter()
    response = await call_next(request)
    dt = (perf_counter() - t0) * 1000
    print(f"{request.method} {request.url.path} -> {response.status_code} {dt:.1f}ms")
    return response

app.middleware("http")(catch_all_exceptions)

# Routers
app.include_router(users_router)

def run():
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("src.app:app", host="0.0.0.0", port=port, reload=True)

if __name__ == "__main__":
    run()
