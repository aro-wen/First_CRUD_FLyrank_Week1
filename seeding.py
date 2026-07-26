from database import conn, cursor

def seed_tasks():
    cursor.execute("SELECT COUNT(*) FROM tasks")

    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("""
        INSERT INTO tasks(title, done)
        VALUES ('Finish Claude 101 Anthropic Course', FALSE)
        """)
        cursor.execute("""
        INSERT INTO tasks(title, done)
        VALUES ('Finish Backend Assignment 1: Building First CRUD API', FALSE)
        """)
        cursor.execute("""
        INSERT INTO tasks(title, done)
        VALUES ('Finish AI Fluency Assignment 1: AI Workflow Audit and Tool Setup', FALSE)
        """)
    conn.commit()