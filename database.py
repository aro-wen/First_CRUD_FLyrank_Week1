import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS tasks(
#     id INTEGER PRIMARY KEY,
#     title TEXT NOT NULL,
#     done BOOLEAN DEFAULT 0
#     )
# """)

# cursor.execute("SELECT COUNT(*) FROM tasks")

# count = cursor.fetchone()[0]

# if count == 0:
#     cursor.execute("""
#     INSERT INTO tasks(title, done)
#     VALUES ("Finish Claude 101 Anthropic Course", 0)
#     """)
#     cursor.execute("""
#     INSERT INTO tasks(title, done)
#     VALUES ("Finish Backend Assignment 1: Building First CRUD API", 0)
#     """)
#     cursor.execute("""
#     INSERT INTO tasks(title, done)
#     VALUES ("Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup", 0)
#     """)
# conn.commit()