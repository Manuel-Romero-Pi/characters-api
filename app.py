from fastapi import FastAPI
from routes import items

app = FastAPI(
    title="Items API",
    description="API REST for characters. Allows to get, add and delete items stored in memory.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(items.router)


@app.get("/", tags=["Root"])
async def root():
    """
    Root endpoint
    
    Returns API information and links to documentation
    """
    return {
        "message": "Welcome to Items API",
        "description": "API REST for characters",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
async def health():
    """
    Health check endpoint
    
    Returns API health status
    """
    return {"status": "healthy"}

