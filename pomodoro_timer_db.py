from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PomodoroList(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True)
	task_name = Column(String(40), nullable=False)
	cycles = Column(Integer, nullable=False)
	task_date = Column(DateTime, default=datetime.now())
	
	def __init__(self, task_name, cycles,task_date):
		self.task_name = task_name
		self.cycles = cycles
		self.task_date = task_date

engine = create_engine('sqlite:///all_tasks.db')
Base.metadata.create_all(engine)

