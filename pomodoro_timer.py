import datetime
class PomoDoroTimer(object):
	def __init__(self):
		self.cycle_start = datetime.datetime.now()

	def start_timer(self, cycle_duration):
		"""Function starts a pomodoro timer and records the task title,
		and start_time and date.
		It also plays a sound bell at the end of a pomodoro cycle.

		"""
		print self.cycle_start
	 	end_of_cycle = self.config_time(cycle_duration)
	 	import time
		import sys
		for remaining in range(cycle_duration *60, 0, -1):
		    sys.stdout.write("\r")
		    sys.stdout.write("{:2d} seconds remaining.".format(remaining)) 
		    sys.stdout.flush()
		    time.sleep(1)
		if remaining is 1 and self.config_sound(True):
			sys.stdout.write("\rpomodoro cycle is over.......\n")
			import pygame
			pygame.init()
			pygame.mixer.music.load("bell.wav")
			pygame.mixer.music.play()
			pygame.event.wait()
		else:
			sys.stdout.write("\rpomodoro cycle is over but alarm is off\n")

	def config_time(self, cycle_duration):
		"""Function sets the time duration for a particular promodoro,
		if no time is given, then default time is used.

		"""
		self.cycle_start
		if cycle_duration:
			duration = datetime.timedelta(minutes = int(cycle_duration))	
			cycle_stop = self.cycle_start + duration
			return cycle_stop
		else:
			cycle_stop = self.cycle_start + datetime.timedelta(minutes = 25)
			self.default_time = cycle_stop
			return cycle_stop

	def config_short_break(self, shrt_break_duration):
		"""Function sets a short break in between a pomodoro task,
		if no time value is given, then the default time value is used.

		"""
		pass

	def config_long_break(self, lng_break_duration):
		"""Function sets the duration for the long break after a pomodoro
		task, if no time value is given, then default duration is used.
		"""
		pass

	def config_sound(self, toggle=False):
		"""Function turns sound notification on/off

		"""
		self.toggle = True
		return self.toggle

	def stop(self):
		"""Function marks the end of the current running pomodoro task;
		and marks the task as complete.

		"""
		pass

	def list_all(self, tasks_per_day, cycles):
		"""List all the pomodoro tasks done on a particular day,
		and details on how many pomodoro cycles spent on each task

		"""
		pass




my_pro = PomoDoroTimer()
print my_pro.start_timer(1)