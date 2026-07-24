from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT 0
    )
""")

cursor.execute("SELECT COUNT(*) FROM tasks")

count = cursor.fetchone()[0]

if count == 0:
    cursor.execute("""
    INSERT INTO tasks(title, done)
    VALUES ("Finish Claude 101 Anthropic Course", 0)
    """)
    cursor.execute("""
    INSERT INTO tasks(title, done)
    VALUES ("Finish Backend Assignment 1: Building First CRUD API", 0)
    """)
    cursor.execute("""
    INSERT INTO tasks(title, done)
    VALUES ("Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup", 0)
    """)
conn.commit()

class TaskModel(BaseModel):
    title: str
    done: bool

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
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    col = ("id", "title", "done")
    task_list = []

    for val in rows:
        task = dict(zip(col, val))
        task_list.append(task)

    return task_list



@app.get("/tasks/{id}")
def return_task(id: int):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (id,))
    row = cursor.fetchone()
    col = ("id", "title", "done")

    if not row:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Task with {id} not found"
            )
    task_result = dict(zip(col,row))
    return task_result

    

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(tasks_data: TaskModel):
    cursor.execute("""
    INSERT INTO tasks(title, done)
    VALUES (?, ?)
    """, (tasks_data.title, tasks_data.done))
    last_rowID = cursor.lastrowid
    conn.commit()

    return return_task(last_rowID)

@app.put("/tasks/{id}")
def update_task(id: str, task:TaskModel):
    for index, existing_task in enumerate(tasks_list):
        if existing_task["id"] == id:
            updated_task = {"id": id, **task.model_dump()}

            tasks_list[index] = updated_task

            return updated_task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Task with {id} not found"
    )

@app.delete("/tasks/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: str):
    for index, existing_task in enumerate(tasks_list):
        if existing_task["id"] == id:
            tasks_list.pop(index)
            return
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Task with {id} not found"
    )