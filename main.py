from fastapi import FastAPI, HTTPException, status
import repository as repository
import service
from models import TaskModel

app = FastAPI()

@app.get("/")
async def root():
    return { "name": "Task API", 
            "version": "1.0", 
            "endpoints": ["/tasks"] }

@app.get("/health")
def health():
    return {"status": "Ok"}

@app.get("/tasks")
def return_task_list():
    return service.get_all_tasks()


@app.get("/tasks/{id}")
def return_task(id: int):
    task = service.get_task_by_id(id)

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with {id} not found"
        )
    return task

    

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(tasks_data: TaskModel):
    task = service.create_task(tasks_data)
    return task

@app.put("/tasks/{id}")
def update_task(id: int, task:TaskModel):
    task = service.update_task(id, task)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with {id} not found"
        )
    return task

    

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int):
    task  = service.delete_task(id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Task with {id} not found"
        )
