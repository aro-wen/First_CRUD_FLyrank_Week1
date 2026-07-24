# 🚀 Task API - FlyRank Backend Assignment (BE-02)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![FlyRank](https://img.shields.io/badge/FlyRank-BE--02-orange)

A simple CRUD (Create, Read, Update, Delete) REST API built using **FastAPI**, **Python**, and **SQLite**.

This project was developed as part of the **FlyRank AI Internship – Backend AI Engineering Track (Week 2 Assignment)** to demonstrate backend development fundamentals, REST API design, HTTP methods, status codes, request validation, SQL operations, database integration, and interactive API documentation through Swagger UI.

---

# 📖 Assignment Overview

The goal of this assignment was to build a task management API while transitioning from temporary in-memory storage to persistent database storage.

The API supports the four core CRUD operations:

- Create tasks
- Read tasks
- Update tasks
- Delete tasks

The previous implementation stored tasks inside a Python list. This assignment replaces the in-memory storage layer with a real SQLite database while keeping the API endpoints unchanged.

The main backend concept demonstrated in this project:

> **APIs describe what an application does. Databases describe where application data is stored.**

The client does not need to know whether the data comes from memory or a database.

---

# 🛠️ Technologies Used

| Technology   | Purpose                          |
| ------------ | -------------------------------- |
| Python 3.10+ | Programming Language             |
| FastAPI      | Backend Web Framework            |
| Pydantic     | Request Validation               |
| SQLite       | Persistent Database Storage      |
| sqlite3      | Python SQLite Database Interface |
| Uvicorn      | ASGI Development Server          |
| Swagger UI   | Interactive API Documentation    |

---

# 🗄️ Database Implementation

This project uses **SQLite** as the database layer.

SQLite was chosen because:

- ✅ Zero installation required
- ✅ No database server setup needed
- ✅ Entire database exists in a single file
- ✅ Data survives server restarts
- ✅ Lightweight and suitable for small applications

The database file:

```text
tasks.db
```

is automatically created when the application starts for the first time.

The database contains one table:

```text
tasks
```

with the following structure:

| Column | Type                |
| ------ | ------------------- |
| id     | INTEGER PRIMARY KEY |
| title  | TEXT                |
| done   | BOOLEAN             |

The `tasks.db` file is usually added to `.gitignore` because:

- Database files contain local application data
- Each developer should generate their own database locally
- Repository clones should start with a fresh database

---

# 🧠 Implementation Process

The project was developed incrementally following the assignment stages.

---

## Stage 0: Create SQLite Database

Replaced the Python list storage with SQLite.

Implemented:

- Automatic database creation
- Table creation
- Initial seed data insertion only when the table is empty

Database initialization:

```sql
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT 0
);
```

The database is stored inside:

```text
tasks.db
```

---

# Stage 1: Read Operations Using SQL

Replaced Python list searching with SQL queries.

Retrieve all tasks:

```sql
SELECT * FROM tasks;
```

Retrieve a single task:

```sql
SELECT * FROM tasks WHERE id = ?;
```

The API continues supporting:

- Get all tasks
- Get task by ID
- 404 errors for missing tasks

---

# Stage 2: Create Operation Using SQL

Replaced list append operations with database insertion.

Implemented:

```sql
INSERT INTO tasks(title, done)
VALUES (?, ?);
```

New tasks are now permanently stored and remain available after restarting the server.

---

# Stage 3: Update and Delete Operations Using SQL

Replaced Python list modification with SQL commands.

## Update Task

```sql
UPDATE tasks
SET title = ?, done = ?
WHERE id = ?;
```

## Delete Task

```sql
DELETE FROM tasks
WHERE id = ?;
```

The API behavior remained unchanged while the storage layer changed.

---

# Stage 4: Exploring SQLite

The database was manually inspected using **DB Browser for SQLite**.

The following SQL operations were tested:

- Retrieve all tasks
- Filter completed tasks
- Update database records
- Delete database records

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/task-api.git

cd task-api
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install "fastapi[standard]"
```

---

# 🚀 Running the Project

Start the FastAPI development server:

```bash
fastapi dev main.py --port 8000
```

When the application starts:

- SQLite database is created automatically
- `tasks.db` is generated if it does not exist
- Seed tasks are inserted only when the database is empty

Server runs at:

```text
http://127.0.0.1:8000
```

---

# 📋 Available API Endpoints

| Method | Endpoint      | Description     |
| ------ | ------------- | --------------- |
| GET    | `/`           | API Information |
| GET    | `/health`     | Health Check    |
| GET    | `/tasks`      | Get All Tasks   |
| GET    | `/tasks/{id}` | Get Single Task |
| POST   | `/tasks`      | Create Task     |
| PUT    | `/tasks/{id}` | Update Task     |
| DELETE | `/tasks/{id}` | Delete Task     |

---

# 📦 Sample Response

## GET `/tasks`

Example response:

```json
[
  {
    "id": 1,
    "title": "Finish Claude 101 Anthropic Course",
    "done": false
  },
  {
    "id": 2,
    "title": "Finish Backend Assignment 1: Building First CRUD API",
    "done": false
  },
  {
    "id": 3,
    "title": "Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup",
    "done": false
  }
]
```

---

# 🔍 Example cURL Request

## Create a Task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Study FastAPI\",\"done\":false}"
```

Example Response:

```http
HTTP/1.1 201 Created
```

```json
{
  "id": 4,
  "title": "Study FastAPI",
  "done": false
}
```

---

# 📑 Swagger UI Documentation

FastAPI automatically generates interactive API documentation through OpenAPI.

Access Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Screenshots:

## Swagger UI

![Swagger UI](docs/SwaggerUI.png)

## Return All Tasks

![Return All Tasks](docs/Return_all_tasks.png)

## Return Single Task

![Return Task](docs/Return_task.png)

## Create Task

![Create Task](docs/Create_task.png)

## Update Task

![Update Task](docs/Update_task.png)

## Delete Task

![Delete Task](docs/Delete_task.png)

---

# 🗃️ Database View

The SQLite database was inspected using **DB Browser for SQLite**.

The screenshot below shows the generated database file and stored task records.

![SQLite Database View](docs/SQLite_Database.png)

---

# 🔎 Example SQL Query (Stage 4)

One SQL query executed manually inside DB Browser for SQLite:

```sql
SELECT * FROM tasks;
```

Example output:

| id  | title                                                | done |
| --- | ---------------------------------------------------- | ---- |
| 1   | Finish Claude 101 Anthropic Course                   | 0    |
| 2   | Finish Backend Assignment 1: Building First CRUD API | 0    |
| 3   | Finish AI Fluency Assignment 1                       | 0    |

This confirmed that the API and database were using the same persistent data source.

---

# ⚠️ Current Limitations

Although this project now uses persistent storage, it is still designed as a learning project.

Current limitations:

- SQLite is not intended for large production workloads
- No authentication or authorization system
- No database migration system
- Direct SQL queries instead of ORM

Future improvements:

- PostgreSQL integration
- SQLAlchemy or SQLModel ORM
- Authentication system
- Automated testing
- Cloud deployment

---

# ✅ Requirements Checklist

- [x] FastAPI server running locally
- [x] Root endpoint
- [x] Health endpoint
- [x] Read all tasks
- [x] Read single task
- [x] Create task
- [x] Update task
- [x] Delete task
- [x] HTTP status code handling
- [x] 404 error handling
- [x] Request validation using Pydantic
- [x] Swagger UI documentation
- [x] SQLite database integration
- [x] Persistent data storage
- [x] SQL CRUD operations

---

# 🎯 Learning Outcomes

Through this assignment I learned:

- How REST APIs work
- CRUD operations using HTTP methods
- HTTP status codes
- Path parameters
- Request validation using Pydantic
- Error handling using HTTPException
- FastAPI routing
- Swagger/OpenAPI documentation
- SQL fundamentals
- SQLite database management
- Connecting APIs with databases
- Database persistence concepts
- Separation between API design and storage implementation

---

# 👩‍💻 Author

**Leila Arowen A. Dumindin**

BS Computer Engineering  
Pamantasan ng Lungsod ng Maynila (PLM)

FlyRank AI Internship – Backend AI Engineering Track
