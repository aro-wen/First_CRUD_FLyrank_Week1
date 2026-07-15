from fastapi import FastAPI, HTTPException, status

tasks_list = [{
    "id" : "001",
    "title" : "Finish Claude 101 Anthropic Course",
    "done" : False
},
{
    "id" : "002",
    "title" : "Finish Backend Assignment 1: Building First CRUD API",
    "done" : False
},
{
    "id" : "003",
    "title" : "Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup ",
    "done" : False
}
]

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
    return tasks_list

@app.get("/tasks/{id}")
def return_task(id: str):
    for task in tasks_list:
        if task["id"] == id:
            return task
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Task with {id} not found"
    )

