from models import Base, engine, SessionLocal, Status, Task

# Inicializar la base de datos con datos ficticios
def initialize_database():
    session = SessionLocal()
    
    # Crear estados por defecto
    status_pending = Status(name="Pendiente")
    status_in_progress = Status(name="En progreso")
    status_completed = Status(name="Completada")
    session.add_all([status_pending, status_in_progress, status_completed])
    session.commit()

    # Crear tareas ficticias
    tasks = [
        Task(title="Comprar víveres", description="Comprar pan, leche y huevos", status=status_pending),
        Task(title="Revisar correo", description="Responder emails pendientes", status=status_in_progress),
        Task(title="Hacer ejercicio", description="Correr 5 km en el parque", completed=True, status=status_completed),
        Task(title="Preparar informe", description="Escribir el informe semanal para el equipo", status=status_pending),
        Task(title="Comprar kit de aseo", description="Comprar crema dental y enjuage", status=status_pending),
        Task(title="Revisar tareas de la U", description="Estudiar termodinamica", status=status_in_progress),
        Task(title="Correr", description="Correr 5 km en el parque", completed=True, status=status_completed),
        Task(title="Escribir ensayo", description="Escribir el ensayo semanal para el equipo", status=status_pending),
    ]
    session.add_all(tasks)
    session.commit()

    print("Base de datos inicializada con datos ficticios.")
    session.close()

def view_data():
    session = SessionLocal()
    tasks = session.query(Task).all()
    for task in tasks:
        print(f"Tarea: {task.title}, Estado: {task.status.name}, Completada: {task.completed}")
    session.close()



if __name__ == "__main__":
    Base.metadata.drop_all(engine)  # Elimina todas las tablas existentes (opcional)
    Base.metadata.create_all(engine)  # Crea las tablas desde cero
    initialize_database()
    view_data()
