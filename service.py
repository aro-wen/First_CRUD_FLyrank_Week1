import repository as repository

def get_all_tasks():
    return repository.get_all_tasks()

def get_task_by_id(id:int):
    return repository.get_task_by_id(id)

def create_task(task_data):
    return repository.create_task(task_data)

def update_task(id:int, task):
    return repository.update_task(id, task)

def delete_task(id:int):
    return repository.delete_task(id)

def check_db():
    return repository.check_db()