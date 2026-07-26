from database import conn, cursor

def get_all_tasks():
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    col = ("id", "title", "done")
    task_list = []
    
    for val in rows:
        task = dict(zip(col, val))
        task_list.append(task)
    
    return task_list

def get_task_by_id(id: int):
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (id,))
    row = cursor.fetchone()
    col = ("id", "title", "done")

    if not row:
        return None

    task_result = dict(zip(col,row))
    return task_result

def create_task(tasks_data):
    cursor.execute("""
    INSERT INTO tasks(title, done)
    VALUES (%s, %s)
    RETURNING id
    """, (tasks_data.title, tasks_data.done))

    last_rowID = cursor.fetchone()[0]
    conn.commit()

    return get_task_by_id(last_rowID)

def update_task(id:int, task):
    cursor.execute("""
    UPDATE tasks
    SET title = %s, done = %s
    WHERE id = %s
    """, (task.title, task.done, id))

    if cursor.rowcount == 0:
        return None

    conn.commit()

    return get_task_by_id(id)

def delete_task(id):
    cursor.execute("""
    DELETE FROM tasks
    WHERE id = %s
    """, (id,))

    if cursor.rowcount == 0:
        return None

    conn.commit()
    return True

def check_db():
    try:
        cursor.execute("SELECT 1")
        result = cursor.fetchone()

        return result[0] == 1
    except Exception:
        return False