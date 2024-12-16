from models import SessionLocal, Task, Status
from sqlalchemy.orm import joinedload

def get_tasks():
    session = SessionLocal()
    tasks = session.query(Task).options(joinedload(Task.status)).all()
    results = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "status": task.status.name if task.status else None,
        }
        for task in tasks
    ]
    session.close()
    return results


def add_task(title, description="", status_name="Pendiente"):
    session = SessionLocal()
    status = session.query(Status).filter(Status.name == status_name).first()
    if not status:
        raise ValueError(f"El estado '{status_name}' no existe.")
    new_task = Task(title=title, description=description, status=status)
    session.add(new_task)
    session.commit()
    session.close()

def update_task_status(task_id, status_name):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    status = session.query(Status).filter(Status.name == status_name).first()
    if task and status:
        task.status = status
        session.commit()
    session.close()

def update_task(task_id, title, description, status_name):
    session = SessionLocal()
    status = session.query(Status).filter(Status.name == status_name).first()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task and status:
        task.title = title
        task.description = description
        task.status_id = status.id
        session.commit()
    session.close()
    

def delete_task(task_id):
    session = SessionLocal()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
