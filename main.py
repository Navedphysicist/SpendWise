from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import auth, income, expense, balance

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SpendWise API",
    description="A personal finance management API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(income.router)
app.include_router(expense.router)
app.include_router(balance.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to SpendWise API"} 