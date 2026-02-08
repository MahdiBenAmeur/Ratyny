# Ratyny Frontend

This is the mobile application for Ratyny, built with Flutter.

## Tech Stack

-   **Framework:** Flutter (Dart)
-   **Design:** Material Design 3
-   **State Management:** Riverpod
-   **Routing:** GoRouter
-   **HTTP Client:** Dio

## Project Structure

```
frontend/
├── lib/
│   ├── main.dart       # Entry point
│   ├── src/
│   │   ├── app.dart    # App widget
│   │   ├── core/       # Theme, Router
│   │   ├── features/   # Feature-based organization (Auth, Home, etc.)
│   │   └── services/   # API services
└── pubspec.yaml        # Dependencies
```

## Setup & Installation

1.  **Prerequisites:**
    -   Ensure the [Flutter SDK](https://docs.flutter.dev/get-started/install) is installed and in your PATH.
    -   An Android Emulator or physical device connected via USB.

2.  **Install Dependencies:**
    Run this command in the `frontend/` directory:
    ```bash
    flutter pub get
    ```

3.  **Generate Platform Folders (if missing):**
    If `android/` or `ios/` folders are missing, run:
    ```bash
    flutter create .
    ```

## Running the App

To run the app on your connected device or emulator:

```bash
flutter run
```

*Note: Make sure the Backend server is running. If using an Android Emulator, the backend URL in `lib/src/services/api_service.dart` is set to `10.0.2.2` to access the host machine's localhost.*
