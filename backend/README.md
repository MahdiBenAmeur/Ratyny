# Ratyny Backend

This is the backend API for the Ratyny platform, a community-based business rating system.

## Tech Stack

-   **Language:** Python 3.11+
-   **Framework:** FastAPI
-   **Server:** Uvicorn
-   **Database:** PostgreSQL (Async)
-   **ORM:** SQLAlchemy 2.0
-   **Authentication:** JWT (JSON Web Tokens)

## Project Structure

```
backend/
├── app/
│   ├── api/            # API endpoints
│   ├── core/           # Config and security
│   ├── db/             # Database session and base models
│   ├── models/         # SQLAlchemy models
│   ├── schemas/        # Pydantic schemas
│   └── main.py         # Application entry point
├── requirements.txt    # Python dependencies
└── .env                # Environment variables (create this)
```

## Setup & Installation

1.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

2.  **Activate the Virtual Environment:**
    -   Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   Mac/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the `backend/` directory (same level as `requirements.txt`).
    Example content:
    ```ini
    POSTGRES_SERVER=localhost
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=ratyny
    POSTGRES_PORT=5432
    SECRET_KEY=your_super_secret_key
    ```
    *Note: Ensure you have a PostgreSQL database named `ratyny` created.*

## Running the Server

Start the development server with hot-reload:

```bash
uvicorn app.main:app --reload
```

The API will be available at: `http://localhost:8000`
Interactive API Docs: `http://localhost:8000/docs`
