#  Blog Generator

A simple blog generation API built with FastAPI, LangGraph, and OpenAI. It generates blog titles and content from a topic and can also route the output for a requested language such as French or Hindi.

## Features

- Generate blog content from a topic
- Support language-aware blog generation
- FastAPI endpoint for easy integration
- LangGraph-based workflow

## Tech Stack

- Python
- FastAPI
- LangGraph
- LangChain OpenAI
- Uvicorn

## Project Structure

- app.py: FastAPI entrypoint
- src/graphs/: LangGraph graph definitions
- src/nodes/: blog generation and translation logic
- src/states/: state schema for the workflow

## Environment Variables

Create a .env file in the project root with:

```env
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
```

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run the API

```bash
python app.py
```

The API will start on:

```text
http://127.0.0.1:8000
```

## API Endpoint

### POST /blogs

Request body:

```json
{
  "topic": "Agentic AI",
  "language": "french"
}
```

Example with curl:

```bash
curl -X POST http://127.0.0.1:8000/blogs \
  -H "Content-Type: application/json" \
  -d '{"topic": "Agentic AI", "language": "french"}'
```

## LangGraph Studio

You can also run the LangGraph app locally with:

```bash
langgraph dev
```

## useCase

- The project currently uses OpenAI for generation and translation.
- If you want the output in a specific language, pass the language in the request payload.


<img width="1877" height="778" alt="image" src="https://github.com/user-attachments/assets/239ad5c4-56d5-4046-9068-edfa1cbec89d" />
