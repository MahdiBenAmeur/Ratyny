# Ratyny

**Ratyny** is a Tunisian community-based rating platform designed to help users evaluate businesses—especially online sellers—by sharing ratings, experiences, and incident reports. Its primary goal is to reduce scams and misleading business practices by providing transparent, user-driven feedback.

## Core Features

-   **Community-Driven Ratings:** Users rate businesses on a 1-5 star scale.
-   **Incident Reporting:** Users can post reports about scams or bad experiences with proof (media).
-   **Business Discovery:** Search for businesses by name, link, or location.
-   **Trust Score:** Users have an internal trust score to ensure platform integrity.
-   **Read-Only Access:** Non-registered users can browse content; interaction requires an account.

## Tech Stack

### Frontend (Mobile App)
-   **Framework:** Flutter (Dart)
-   **Design:** Material Design 3
-   **State Management:** Riverpod
-   **Routing:** GoRouter

### Backend (API)
-   **Language:** Python 3.11+
-   **Framework:** FastAPI
-   **Database:** PostgreSQL (Async via SQLAlchemy)
-   **Authentication:** JWT (JSON Web Tokens)

## Getting Started

This repository is divided into two main parts:

-   **[Backend](./backend/README.md):** The REST API server.
-   **[Frontend](./frontend/README.md):** The Flutter mobile application.

Please refer to the README files in each directory for specific setup and installation instructions.

## License

[MIT](LICENSE)
