# FastAPI Task Manager

A simple REST API built with FastAPI to manage tasks. Deploy-ready for DigitalOcean App Platform.

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root welcome message |
| GET | `/tasks` | List all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open http://localhost:8000/docs for the interactive API docs.

## Deploy to DigitalOcean

See the deployment guide for step-by-step instructions.
