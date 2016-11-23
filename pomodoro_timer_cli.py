from pomodoro_timer import PomoDoroTimer

def cli_main():
	commands = PomoDoroTimer()
	while True:
		print('\n')
		print('            WELCOME TO POMODORO TIMER')
		print('            -------------------------')
		print('            what do you want to do?:\n')
		print('        1. Start Pomodoro\n        2. Configure Pomodoro Cycle Length\n'
	          '        3. Configure Intercycles Break Length\n        4. Configure Long Break\n'
	          '        5. Configure Cycle Alarm ON/OFF\n        6. STOP\n'
	          '        7. list all tasks\n        8. Exit\n')

		selection = raw_input("Enter an option here: ")
		if selection == "1":
			commands.start_timer()
		elif selection == "2":
			cycle_duration = raw_input("Enter the Cycle Duration or press ENTER to use default(25):")
			if cycle_duration == '':
				cycle_duration = 25
				commands.start_timer(int(cycle_duration))
			elif cycle_duration:
				try:
					commands.start_timer(int(cycle_duration))
				except ValueError:
					print "Invalid format."
		elif selection == "3":
			break_len = raw_input("Enter the desired break length or press ENTER to use default(5): ")
			shrt_break_duration = break_len
			if break_len == "":
				shrt_break_duration = 5
				commands.config_short_break(int(shrt_break_duration))
			elif shrt_break_duration:
				try:
					commands.config_short_break(int(shrt_break_duration))
				except ValueError:
					print "Invalid format."






if __name__ == '__main__':cli_main()














# def main():
#     tasks = ToDo()
#     while True:
#         print('\n')
#         print('                 WELCOME TO YOUR TO DO APP')
#         print('                 -------------------------')
#         print('            Select a choice from the list given below\n')
#         print('        1. Add task\n        2. Move todo task to doingn\n'
#               '        3. Move doing task to Done\n        4. List todo tasks\n'
#               '        5. list doing tasks\n        6. List done tasks\n'
#               '        7. list all tasks\n        8. Exit\n')
#         choice = input('        Please Enter your choice: ')
#         if choice == '1':
#             task_name = input('     Enter name of the task: ')
#             task_desc = input('     Enter Task Description: ')
#             tasks.to_do(task_name, task_desc)
#         elif choice == '2':
#             print('   Select the task from list below ')
#             print(tasks.list_todo())
#             print('\n')
#             task = int(input('  Enter task id of the selected task: '))
#             tasks.doing(task, True)
#         elif choice == '3':
#             print('   Select the task from list below ')
#             print(tasks.list_doing())
#             print('\n')
#             task = int(input('  Enter task id of the selected task: '))
#             tasks.done(task, True)
#         elif choice == '4':
#             print(tasks.list_todo())
#         elif choice == '5':
#             print(tasks.list_doing())
#         elif choice == '6':
#             print(tasks.list_done())
#         elif choice == '7':
#             print(tasks.list_all())
#         elif choice == '8':
#             break
#         else:
#             print('Invalid Choice, please try again')

# if __name__ == '__main__':main()