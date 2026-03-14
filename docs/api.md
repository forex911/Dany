# API Reference

The Dany Template backend exposes a RESTful API.

## Base URL

By default, the backend runs at `http://localhost:5000`

## Endpoints

### 1. Health Check
Checks if the API is currently running and responsive.

- **Method**: `GET`
- **Route**: `/health`

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Dany API is healthy and running",
  "version": "1.0.0"
}
```

### 2. Process Media
Initiates a media processing request. *(Note: Returns simulated mock data).*

- **Method**: `POST`
- **Route**: `/process`
- **Content-Type**: `application/json`

**Request Body:**
```json
{
  "url": "https://example.com/media/123",
  "format": "mp4" // optional
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "data": {
    "title": "Example Media Title",
    "duration": "03:45",
    "source_url": "https://example.com/media/123",
    "simulated": true,
    "disclaimer": "This is a simulated response. Real extraction logic is removed."
  }
}
```

**Response (400 Bad Request):**
```json
{
  "status": "error",
  "message": "URL is required"
}
```
