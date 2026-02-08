from app.db.session import engine, Base

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = FastAPI(
    title="Ratyny API",
    description="Backend for Ratyny - A community-based business rating platform",
    version="0.1.0",
)

# CORS Middleware setup
origins = [
    "http://localhost",
    "http://localhost:8000",
    "*" # For mobile development, often helpful to allow all, strictly configure for prod
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.api.v1.api import api_router

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Ratyny API"}
