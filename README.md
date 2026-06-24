# FastAPI Gemini Chatbot

An AI-powered chatbot backend built using **FastAPI** and **Google Gemini API**. The application exposes REST endpoints that allow users to interact with Gemini through a structured API while supporting multiple response modes and automatic API documentation using Swagger UI.

---

## Features

* AI-powered responses using Google Gemini 2.5 Flash
* FastAPI REST API architecture
* Interactive Swagger Documentation
* Modular project structure
* Environment variable configuration using `.env`
* Multiple response modes:

  * Normal
  * ELI5 (Explain Like I'm 5)
  * Professional
* Request validation using Pydantic
* Error handling for API failures

---

## Project Structure

```text
fastapi-gemini-chatbot/
│
├── main.py
├── requirements.txt
├── .env
│
├── routes/
│   └── chat.py
│
├── schemas/
│   └── chat_schema.py
│
├── services/
│   └── gemini_service.py
```

---

## Tech Stack

* Python
* FastAPI
* Google Gemini API
* Pydantic
* Uvicorn
* Python Dotenv

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "Welcome to Gemini Chatbot API"
}
```

### Chat Endpoint

```http
POST /chat
```

Request:

```json
{
  "message": "What is Machine Learning?",
  "mode": "eli5"
}
```

Response:

```json
{
  "status": "success",
  "reply": "Imagine teaching a robot by showing examples..."
}
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/FastAPI-Gemini-Chatbot.git
```

Navigate to the project folder:

```bash
cd FastAPI-Gemini-Chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
uvicorn main:app --reload
```

---

## Swagger Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

to test API endpoints directly through Swagger UI.

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

* Building REST APIs using FastAPI
* Integrating external AI services
* Managing API keys securely using environment variables
* Request validation using Pydantic models
* Organizing backend applications using a modular architecture
* Testing APIs using Swagger Documentation

---

## Future Enhancements

* Chat history support
* Conversation IDs
* Database integration
* User authentication
* Frontend integration with React
* Deployment on cloud platforms

```
```
