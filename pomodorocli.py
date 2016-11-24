#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    my_program start <task_title>
    my_program configtime <duration_in_minutes>
    my_program configlongbreak <duration_in_minutes>
    my_program configshortbreak <duration_in_minutes>
    my_program configsound <off/on>
    my_program listall <>
    my_program list

    my_program (-i | --interactive)
    my_program (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from pomodoro_timer_confs import PomoDoroTimer

pomodoro = PomoDoroTimer()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my interactive program!' \
        + ' (type help for a list of commands.)'
    prompt = 'pomodoro_timer: > '

    file = None

    @docopt_cmd
    def do_start(self, arg):
        """Usage: start <task_title>"""
        title = arg['<task_title>']
        pomodoro.start(title)

    @docopt_cmd
    def do_configtime(self, arg):
        """Usage: configtime <duration_in_minutes>"""
        duration = arg['<duration_in_minutes>']
        pomodoro.config_time(duration)

    @docopt_cmd
    def do_configshortbreak(self, arg):
        """Usage: configshortbreak <duration_in_minutes>"""
        duration = arg['<duration_in_minutes>']
        pomodoro.config_short_break(duration)

    @docopt_cmd
    def do_configlongbreak(self, arg):
        """Usage: configlongbreak <duration_in_minutes> """
        duration = arg['<duration_in_minutes>']
        pomodoro.config_long_break(duration)


    @docopt_cmd
    def do_configsound(self, arg):
        """Usage: configsound <off/on> """
        sound = arg['<off/on>']
        pomodoro.config_sound(sound)


    @docopt_cmd
    def do_listall(self, arg):
        """Usage: listall """
        pomodoro.list_all()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

#opt = docopt(__doc__, sys.argv[1:])

MyInteractive().cmdloop()

#print(opt)
