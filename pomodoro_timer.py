import datetime
class PomoDoroTimer(object):
	def __init__(self):
		pass

	def start_timer(self, cycle_duration):
		"""Function starts a promodoro timer and records the task title,
		and start_time and date.
		It also plays a sound bell at the end of a promodoro cycle.

		"""
	 	end_of_cycle = self.config_time(cycle_duration)
		#return end_of_cycle


	def config_time(self,cycle_duration):
		"""Function sets the time duration for a particular promodoro,
		if no time is given, then default time is used.

		"""
		cycle_start = datetime.datetime.now()
		if cycle_duration:	
			cycle_stop = cycle_start + datetime.timedelta(minutes = int(cycle_duration))
			return cycle_stop
		else:
			cycle_stop = cycle_start + datetime.timedelta(minutes = 25)
			self.default_time = cycle_stop
			return cycle_stop

	def config_short_break(self, shrt_break_duration):
		"""Function sets a short break in between a promodoro task,
		if no time value is given, then the default time value is used.

		"""
		pass

	def config_long_break(self, lng_break_duration):
		"""Function sets the duration for the long break after a promodoro
		task, if no time value is given, then default duration is used.
		"""
		pass

	def config_sound(self, toggle):
		"""Function turns sound notification on/off

		"""	
		pass

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
print my_pro.start_timer(2)