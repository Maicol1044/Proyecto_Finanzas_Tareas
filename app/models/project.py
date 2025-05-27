# app/models/project.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=True)

    # Relación con tareas (relación inversa en task.py)
    tasks = relationship("Task", back_populates="project", cascade="all, delete-orphan")
