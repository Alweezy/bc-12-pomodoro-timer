import datetime
import pygame
import time
import sys
import execution_modules
class PomoDoroTimer(object):
	def __init__(self):
		self.cycle_length = 25
		self.short_break_length = 5
		self.long_break_length = 15
		self.sound = True

	def start(self, task_name):
		"""Function starts a pomodoro timer and records the task title,
		and start_time and date.
		It also plays a sound bell at the end of a pomodoro cycle.

		"""
		for cycles in range(4):
			execution_modules.cycle(self.cycle_length)
			print "*************************************"
			if cycles < 4:
				execution_modules.short_break(self.short_break_length)
				print "************************************"
		execution_modules.long_break(selfh	.long_break_length)
		print "End of task !"


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
