import time
import sys
def cycle(length):
	for rem_time in range(length, 0, -1):
		sys.stdout.write("\r")
		sys.stdout.write("{:2d} seconds remaining.".format(rem_time))
		sys.stdout.flush()
		time.sleep(1)

def short_break(length):
	for rem_time in range(length, 0, -1):
		sys.stdout.write("\r")
		sys.stdout.write("{:2d} seconds remaining.".format(rem_time))
		sys.stdout.flush()
		time.sleep(1)

def long_break(length):
	for rem_time in range(length, 0, -1):
	    sys.stdout.write("\r")
	    sys.stdout.write("{:2d} seconds remaining.".format(rem_time))
	    sys.stdout.flush()
	    time.sleep(1)

def bell(play_sound):
	pygame.init()
	pygame.mixer.music.load("bell_true.mp3")
	pygame.mixer.music.play()
	time.sleep(4)
