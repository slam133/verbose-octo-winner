# WeChat Mini Program Backend

This is a FastAPI backend for a WeChat Mini Program. It includes user registration, authentication, user information retrieval, and more.

## Features

- User registration
- User authentication
- Retrieve user information
- Update user information
- Delete user information
- Token-based authentication (JWT)
- Secure password hashing

## Project Structure

wechat_backend/
│
├── app/
│ ├── init.py
│ ├── main.py
│ ├── models.py
│ ├── schemas.py
│ ├── crud.py
│ ├── database.py
│ ├── dependencies.py
│ ├── routers/
│ │ ├── init.py
│ │ ├── users.py
│ │ ├── auth.py
│ └── core/
│ ├── init.py
│ ├── config.py
│ ├── security.py
│
├── tests/
│ ├── init.py
│ ├── test_main.py
│ ├── test_users.py
│ ├── test_auth.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/slam133/verbose-octo-winner/wechat_backend.git
    cd wechat_backend
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables**:

    Create a `.env` file in the project root directory with the following content:

    ```env
    DATABASE_URL=sqlite:///./test.db
    SECRET_KEY=your_secret_key
    ```

5. **Run the application**:

    ```sh
    uvicorn app.main:app --reload
    ```

    The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /`: Welcome message
- `POST /users/`: Create a new user
- `GET /users/{user_id}`: Get a user by ID
- `PUT /users/{user_id}`: Update a user by ID
- `DELETE /users/{user_id}`: Delete a user by ID
- `POST /auth/login`: Authenticate a user and get a token

## Running Tests

To run the tests, use:

```sh
pytest

