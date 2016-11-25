###The Pomodoro Timer.
A  pomodoro timer is a timing technique that breaks down the timing of  a task into cycles, usually 25 minutes but the time can be adjusted. After every cycle an alarm goes off  to mark the end of cycle and timer goes into a short break, usually 5 minutes but adjustable too. A single task has typically 4 cycles, after which the timing is completed and a long break, 15 minutes is started. The application should allow the user to configure: The time for one cycle, the time for a short break, the length of short breaks between the cycles and the long break at end of cycle. It should also be able to receive a "Stop" command from the user to stop the timing if need be and also "List all" to show a list of all the tasks one and their timings.

###Installation
Clone into the repo:`https://github.com/Alweezy/bc-12-pomodoro-timer/tree/pomodoro-clean`
cd to `pomodoro-clean`

###Usage
create a virtual environment in your directory:`pomodoro-clean`
activavate the virtual environment and run `pomodorocli.py -i `to start the interactive command line interface.

###Requirements

```colorama==0.3.7
docopt==0.6.2
prettytable==0.7.2
pyfiglet==0.7.5
pygame==1.9.2b8
SQLAlchemy==1.1.4
termcolor==1.1.0
``` 

###Pending tasks
The `stop` command is not yet implemented. It will be available soon.
