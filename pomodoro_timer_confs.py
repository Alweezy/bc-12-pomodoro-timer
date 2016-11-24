import datetime
import pygame
import time
import sys
import execution_modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pomodoro_timer_db import PomodoroList, Base
from prettytable import PrettyTable

engine = create_engine('sqlite:///all_tasks.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class PomoDoroTimer(object):
	def __init__(self):
		self.cycle_length = 25
		self.short_break_length = 5
		self.long_break_length = 15
		self.sound = True
		self.cycles = 4
		self.task_name = ""

	def start(self, task_name):
		"""Function starts a pomodoro timer and records the task title,
		and start_time and date.
		It also plays a sound bell at the end of a pomodoro cycle.

		"""
		self.task_name = task_name
		session.add(PomodoroList(self.task_name, self.cycles))
		session.commit()
		for cycles in range(1, 5):
			execution_modules.cycle(self.cycle_length)
			if cycles < 4:
				execution_modules.short_break(self.short_break_length)
				print ("\n")
				execution_modules.bell(self.sound)
				print "************************************ \n"
				print "Going back to task, cycle" + " " + str(cycles + 1)

		execution_modules.long_break(self.long_break_length)
		print "End of task !"
		return ''

	def config_time(self, cycle_length):
		"""Function sets the time duration for a particular promodoro cycle,
		if no time is given, then default time is used.

		"""
		if cycle_length:
			try:
				self.cycle_length = int(cycle_length)
			except ValueError:
				print 'Only integers accepted'
		return 

	def config_short_break(self, short_break_length):
		"""Function sets a short break in between a pomodoro task,
		if no time value is given, then the default time value is used.

		"""
		if short_break_length:
			try:
				self.short_break_length = int(short_break_length)
			except ValueError:
				print 'Only integers accepted'
		return 

	def config_long_break(self, long_break_length):
		"""Function sets the duration for the long break after a pomodoro
		task, if no time value is given, then default duration is used.
		"""
		if long_break_length:
			try:
				self.long_break_length = int(long_break_length)
			except ValueError:
				print 'Only integers accepted'
		return 

		
	def config_sound(self, sound):
		"""Function turns sound notification on/off

		"""
		if sound.capitalize() == 'True':
			self.sound = True
		elif sound.capitalize() == 'False':
			self.sound = False
		else:
			print 'Only bool variable, i.e True or False'
		return

	def list_all(self):
		"""Function lists all tasks in the database
		"""
		list_entries = session.query(PomodoroList).all()
		data_table = PrettyTable(['Task_id', 'Task_name', 'No._of_cycles', 'Task_Date'])
		for row in list_entries:
			get_id = row.id
			get_cycles = row.cycles
			get_date = row.task_date
			get_task_name = row.task_name
			data_table.add_row((get_id, get_task_name, get_cycles, get_date))
		print data_table

