# SpendWise API

A personal finance management API built with FastAPI and SQLAlchemy.

## Features

- User authentication (signup/login) with JWT tokens
- Income management (CRUD operations)
- Expense management (CRUD operations)
- Balance calculations
- SQLite database for data persistence

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Interactive API documentation (Swagger UI): `http://localhost:8000/docs`
- Alternative API documentation (ReDoc): `http://localhost:8000/redoc`

## API Endpoints

### Authentication
- POST `/auth/signup` - Create a new user account
- POST `/auth/login` - Login and get access token

### Incomes
- POST `/incomes` - Create a new income
- GET `/incomes` - List all incomes
- GET `/incomes/{income_id}` - Get a specific income
- PATCH `/incomes/{income_id}` - Update an income
- DELETE `/incomes/{income_id}` - Delete an income
- GET `/incomes/total/amount` - Get total income amount

### Expenses
- POST `/expenses` - Create a new expense
- GET `/expenses` - List all expenses
- GET `/expenses/{expense_id}` - Get a specific expense
- PATCH `/expenses/{expense_id}` - Update an expense
- DELETE `/expenses/{expense_id}` - Delete an expense
- GET `/expenses/total/amount` - Get total expense amount

### Balance
- GET `/balance/total` - Get total balance (income - expenses)

## Security

- All endpoints except `/auth/signup` and `/auth/login` require authentication
- Passwords are hashed using bcrypt
- JWT tokens are used for authentication
- CORS is enabled for all origins (configurable for production)

## Development

The project structure follows a modular design:
- `models/` - SQLAlchemy models
- `schemas/` - Pydantic schemas
- `routers/` - FastAPI route handlers
- `database.py` - Database configuration
- `auth_utils.py` - Password hashing utilities
- `token.py` - JWT token utilities
- `dependencies.py` - Common dependencies 