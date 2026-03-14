# Dany - Media Processing Architecture Template

> **Disclaimer:** This repository is for **educational and architectural demonstration purposes only**. It does NOT contain any real downloading functionality, scraper logic, DRM bypassing code, or code that violates the Terms of Service of platforms like YouTube, Spotify, etc.

## 📖 Overview

**Dany** is a clean, open-source template demonstrating the system design, backend structure, API routes, and frontend integration of a media processing service. 

It serves as a foundation or showcase for how a modern, decoupled web architecture can handle client requests, route them through a REST API to backend services, and return processed data formats cleanly.

**Key exclusions:**
- 🚫 **No real downloading functionality**
- 🚫 **No platform extraction/scraping logic**
- 🚫 **No Terms of Service violations**

All business logic where media is normally "processed" has been replaced with professional placeholder comments and mock JSON responses.

## 🏗 Architecture

The system follows a standard client-server architecture pattern:

1. **Frontend:** A minimal, responsive vanilla HTML/JS/CSS client.
2. **Backend API:** A `Flask`-based RESTful application handling incoming requests.
3. **Services:** Decoupled service layers (`media_service.py`) representing where business logic would live.

For more details, see [Architecture Documentation](docs/architecture.md).

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dany-template.git
   cd dany-template
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Start the backend development server:
   ```bash
   python backend/app.py
   ```
   The backend will be available at `http://127.0.0.0:5000`.

2. Open the frontend:
   Simply open `frontend/index.html` in your web browser.

## 📚 Documentation

- [System Architecture](docs/architecture.md)
- [API Reference](docs/api.md)

## 🤝 Contributing

Contributions are welcome for improving the template architecture, documentation, and overall structure. Please do **not** submit PRs containing real downloading code.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
