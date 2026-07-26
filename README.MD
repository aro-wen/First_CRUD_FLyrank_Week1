# 🚀 Task API - FlyRank Backend Assignment (BE-03)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL-blue)
![Docker](https://img.shields.io/badge/Containerized-Docker-2496ED)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-yellow)
![FlyRank](https://img.shields.io/badge/FlyRank-BE--03-orange)

A RESTful CRUD (Create, Read, Update, Delete) API built using **FastAPI**, **PostgreSQL**, **Docker**, and **Python**.

This project was developed as part of the **FlyRank AI Internship – Backend AI Engineering Track (Week 3 Assignment)** to demonstrate database containerization, PostgreSQL integration, environment variable management, SQL persistence, layered backend architecture, and API health monitoring.

---

# 📖 Assignment Overview

The goal of this assignment was to migrate an existing FastAPI application from SQLite to PostgreSQL while preserving the API contract and endpoint behavior.

The application supports:

- Create tasks
- Read tasks
- Update tasks
- Delete tasks

The migration demonstrates a key backend engineering principle:

> APIs define what an application does. Databases define where application data is stored.

By separating API routes, business logic, and database access into different layers, the application can change its storage implementation without affecting the API interface.

---

# 🏗️ Project Architecture

The project follows a layered backend architecture:

```text
Client
  ↓
FastAPI Routes
  ↓
Service Layer
  ↓
Repository Layer
  ↓
PostgreSQL Database
```

### Layer Responsibilities

| Layer      | Responsibility                     |
| ---------- | ---------------------------------- |
| Routes     | Handle HTTP requests and responses |
| Services   | Application and business logic     |
| Repository | Database queries and persistence   |
| Database   | PostgreSQL connection management   |

This separation allows the database implementation to change while keeping the API endpoints unchanged.

---

# 🛠️ Technologies Used

| Technology     | Purpose                       |
| -------------- | ----------------------------- |
| Python 3.10+   | Programming Language          |
| FastAPI        | Backend Web Framework         |
| Pydantic       | Request Validation            |
| PostgreSQL     | Relational Database           |
| Psycopg        | PostgreSQL Driver             |
| Docker         | Containerization              |
| Docker Compose | Multi-container Management    |
| Python Dotenv  | Environment Variable Loading  |
| Swagger UI     | Interactive API Documentation |

---

# 🗄️ PostgreSQL Database

This project uses PostgreSQL running inside a Docker container.

Benefits:

- Persistent data storage
- Production-grade relational database
- SQL standards compliance
- Isolated development environment
- Easy onboarding for other developers

Database schema:

```sql
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

The application stores task records in a PostgreSQL database named:

```text
tasks_db
```

---

# 🐳 Docker Setup

PostgreSQL is containerized using Docker Compose.

```yaml
services:
  db:
    image: postgres:15-alpine
    ports:
      - "5432:5432"
```

Benefits of containerization:

- No local PostgreSQL installation required
- Consistent environment across machines
- Simplified project setup
- Easy database recreation
- Persistent storage through Docker volumes

---

# 🔐 Environment Variables

Database credentials are managed using environment variables.

Example:

```env
POSTGRES_DB=tasks_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres123
DATABASE_URL=postgres://postgres:postgres123@localhost:5432/tasks_db
```

The project includes:

```text
.env.example
```

The actual:

```text
.env
```

file is excluded from version control to prevent exposing credentials.

---

# 📝 Database Initialization

Database creation is automated through:

```text
sql/init.sql
```

Contents:

```sql
CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);
```

The initialization script is mounted into PostgreSQL through:

```yaml
volumes:
  - ./sql/init.sql:/docker-entrypoint-initdb.d/init.sql
```

This allows the database schema to be automatically created when PostgreSQL starts for the first time.

---

# 🌱 Seed Data

The application automatically inserts example tasks when the database is empty.

Seed tasks:

- Finish Claude 101 Anthropic Course
- Finish Backend Assignment 1: Building First CRUD API
- Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup

The seeding process only runs when:

```sql
SELECT COUNT(*) FROM tasks;
```

returns:

```text
0
```

This prevents duplicate seed records.

---

# ❤️ Health Check Endpoint

The project includes a database-aware health check.

Endpoint:

```http
GET /health
```

The endpoint verifies PostgreSQL connectivity using:

```sql
SELECT 1;
```

Example response:

```json
{
  "status": "ok",
  "db": "ok"
}
```

This confirms that:

- FastAPI is running
- PostgreSQL is reachable
- SQL queries can be executed successfully

Health checks like this are commonly used in production deployments and monitoring systems.

---

# 🧠 Migration from SQLite to PostgreSQL

A major objective of this assignment was migrating the storage layer from SQLite to PostgreSQL.

Changes made:

| SQLite              | PostgreSQL           |
| ------------------- | -------------------- |
| sqlite3             | psycopg              |
| tasks.db file       | PostgreSQL container |
| ? placeholders      | %s placeholders      |
| lastrowid           | RETURNING id         |
| Local database file | Dockerized database  |

The API endpoints remained unchanged throughout the migration.

This demonstrates the value of the Repository Pattern and separation of concerns.

---

# 📂 Project Structure

```text
task-api/
│
├── data/
├── docs/
├── sql/
│   └── init.sql
│
├── database.py
├── repository.py
├── service.py
├── seeding.py
├── models.py
├── main.py
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
```

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

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install fastapi[standard]
pip install psycopg[binary]
pip install python-dotenv
```

---

## Configure Environment Variables

Create:

```text
.env
```

based on:

```text
.env.example
```

---

# 🚀 Running the Project

## Start PostgreSQL

```bash
docker compose up -d
```

Verify container:

```bash
docker ps
```

---

## Start FastAPI

```bash
fastapi dev main.py
```

Application URL:

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

# 📦 Example Response

## GET `/tasks`

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

## Create Task

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Study PostgreSQL\",\"done\":false}"
```

Example Response:

```json
{
  "id": 4,
  "title": "Study PostgreSQL",
  "done": false
}
```

---

# 📑 Swagger UI Documentation

FastAPI automatically generates OpenAPI documentation.

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

# 🗃️ PostgreSQL Verification

The database was verified through PostgreSQL and Docker.

Commands used:

```sql
\dt
```

```sql
SELECT * FROM tasks;
```

These confirmed:

- Table creation
- Seed data insertion
- Successful PostgreSQL connectivity

---

# ⚠️ Current Limitations

Current limitations:

- No authentication or authorization
- No automated testing suite
- No database migration tooling
- Direct SQL queries instead of ORM
- Single PostgreSQL instance

Future improvements:

- SQLAlchemy or SQLModel
- JWT Authentication
- Unit and Integration Testing
- CI/CD Pipeline
- Cloud Deployment
- Redis Caching
- Database Migrations with Alembic

---

# ✅ Requirements Checklist

- [x] FastAPI server
- [x] PostgreSQL integration
- [x] Dockerized database
- [x] Environment variable configuration
- [x] Database initialization script
- [x] Automatic seed data
- [x] Health check endpoint
- [x] Read all tasks
- [x] Read single task
- [x] Create task
- [x] Update task
- [x] Delete task
- [x] HTTP status handling
- [x] Request validation
- [x] Swagger UI documentation
- [x] Persistent storage using Docker volumes

---

# 🎯 Learning Outcomes

Through this assignment I learned:

- PostgreSQL fundamentals
- Docker and Docker Compose
- Environment variable management
- Database containerization
- Repository pattern
- Layered backend architecture
- SQL CRUD operations
- Database initialization scripts
- Health check endpoints
- Database persistence using volumes
- Migrating applications from SQLite to PostgreSQL
- Separation of concerns in backend systems

---

# 👩‍💻 Author

**Leila Arowen A. Dumindin**

BS Computer Engineering
Pamantasan ng Lungsod ng Maynila (PLM)

FlyRank AI Internship – Backend AI Engineering Track
