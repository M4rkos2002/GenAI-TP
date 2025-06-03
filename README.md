# GenAI-TP
AI Agent for Slogan and Name Generation

## Description
An AI-powered service that generates creative slogans and names using OpenAI's language models.

## Prerequisites
- Docker and Docker Compose
- OpenAI API Key

## Setup
1. Clone the repository
```bash
git clone <repository-url>
cd GenAI-TP
```

2. Create a `.env` file in the root directory:
```bash
echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
```
Replace `your_openai_api_key_here` with your actual OpenAI API key.

## Running the Application
1. Build and start the Docker container:
```bash
docker compose up -d --build
```

2. Verify the service is running:
```bash 
curl http://localhost:8000/api/v1/status
```

## API Documentation
Once the service is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Available Endpoints
- `GET /api/v1/status`: Check API status and response time

## Development
The project uses:
- FastAPI for the web framework
- OpenAI's API for AI text generation
- Docker for containerization

## Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)

## Project Structure
```
GenAI-TP/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── build/
│   │   └── builder/
│   ├── service/
│   │   └── LLmService.py
│   └── main.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```
