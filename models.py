from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Modelo para Estados
class Status(Base):
    __tablename__ = "statuses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)  # Ejemplo: "Pendiente", "En progreso", "Completada"
    
    # Relación con Task
    tasks = relationship("Task", back_populates="status")

# Modelo para Tareas
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    status_id = Column(Integer, ForeignKey("statuses.id"))  # Relación con Status
    
    # Relación inversa
    status = relationship("Status", back_populates="tasks")

# Crear el motor de la base de datos
DATABASE_URL = "sqlite:///todo_app.db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
