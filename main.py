from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Task Manager API",
    description="A simple Task Manager built with FastAPI",
    version="1.0.0"
)

# In-memory storage
tasks = []
task_counter = 1


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TaskResponse(Task):
    id: int


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to Task Manager API! Visit /docs for documentation."}


@app.get("/tasks", response_model=List[TaskResponse], tags=["Tasks"])
def get_tasks():
    """Get all tasks"""
    return tasks


@app.get("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def get_task(task_id: int):
    """Get a single task by ID"""
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.post("/tasks", response_model=TaskResponse, status_code=201, tags=["Tasks"])
def create_task(task: Task):
    """Create a new task"""
    global task_counter
    new_task = {"id": task_counter, **task.dict()}
    tasks.append(new_task)
    task_counter += 1
    return new_task


@app.put("/tasks/{task_id}", response_model=TaskResponse, tags=["Tasks"])
def update_task(task_id: int, updated: Task):
    """Update an existing task"""
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[i] = {"id": task_id, **updated.dict()}
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    """Delete a task"""
    global tasks
    original_len = len(tasks)
    tasks = [t for t in tasks if t["id"] != task_id]
    if len(tasks) == original_len:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": f"Task {task_id} deleted successfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
