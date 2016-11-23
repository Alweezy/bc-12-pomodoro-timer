import datetime
import pygame
import time
import sys
class PomoDoroTimer(object):
	def __init__(self):
		pass

	def start_timer(self, task_name):
		"""Function starts a pomodoro timer and records the task title,
		and start_time and date.
		It also plays a sound bell at the end of a pomodoro cycle.

		"""
		task = str(raw_input("Enter the name of your task: "))
		if task:
			try:
				task_name = task.upper()
				task_time = datetime.datetime.now().time()
				task_date = datetime.date.today()
				print task_time
			except ValueError:
				print "every task should have a name"

				return ""
	def config_time(self, cycle_duration):
		"""Function sets the time duration for a particular promodoro cycle,
		if no time is given, then default time is used.

		"""
		settings = raw_input("Enter time for a pomodoro cycle?[y/n]:")
		cycle_settings = settings.lower()
		if settings == "":
			print "The default duration [25] will be used...."
			cycle_duration == 25;
			return cycle_duration
		if settings:
			duration = raw_input("Specify duration in minutes: ")
			try:
				cycle_duration = (int(duration))
				return cycle_duration
			except ValueError:
				print "Invalid inputs, try again"

	def config_short_break(self, shrt_break_duration):
		"""Function sets a short break in between a pomodoro task,
		if no time value is given, then the default time value is used.

		"""
		settings = raw_input("Enter time for a short break?[y/n]:")
		brk_settings = settings.lower()
		if settings == "":
			print "The default duration [5] will be used...."
			shrt_break_duration == 5;
			return shrt_break_duration
		if settings:
			duration = raw_input("Specify duration in minutes: ")
			try:
				shrt_break_duration = (int(duration))
				return shrt_break_duration
			except ValueError:
				print "Invalid inputs, try again"
		

	def config_long_break(self, lng_break_duration):
		"""Function sets the duration for the long break after a pomodoro
		task, if no time value is given, then default duration is used.
		"""
		settings = raw_input("Enter time for a long break?[y/n]:")
		brk_settings = settings.lower()
		if settings == "":
			print "The default duration [15] will be used...."
			lng_break_duration == 5;
			return lng_break_duration
		if settings:
			duration = raw_input("Specify duration in minutes: ")
			try:
				lng_break_duration = (int(duration))
				return lng_break_duration
			except ValueError:
				print "Invalid inputs, try again"
		
	def config_sound(self, toggle):
		"""Function turns sound notification on/off

		"""
		settings = raw_input("Do you want turn Alarm audio ON? [y/n] ")
		toggle_settings = settings.lower()
		if settings == "":
			print "The default, [OFF] will be used...."
			toggle = False			
			return toggle
		if settings:
			toggle = True
			return toggle

my_pro = PomoDoroTimer()
print my_pro.start_timer(1)