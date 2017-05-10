"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    amity create_room <room_type> <room_name>
    amity add_person <first_name> <last_name> (Fellow|Staff) [wants_accommodation]
    amity reallocate_person <person_identifier> <new_room_name>
    amity load_people
    amity print_allocations [-o=filename]
    amity print_unallocated [-o=filename]
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity print_room <room_name>
    amity (-i | --interactive)
    amity (-h | --help | --version)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from app.amity import Amity


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


amity = Amity()


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to my amity space allocation program!' \
        + ' (type help for a list of commands.)'
    prompt = '(Amity Space Allocation) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_names>"""
        room_type = args["<room_type>"]
        room_names = args["<room_names>"]
        amity.create_room(room_type, room_names)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> <designation> <wants_accommodation>"""

        first_name = args["<first_name>"] + ''
        last_name = args["<last_name>"]
        designation = args["<designation>"]
        wants_accommodation = args["<wants_accommodation>"]

        amity.add_person(first_name, last_name, designation, wants_accommodation)

    # @docopt_cmd
    # def do_reallocate_office(self, args):
    #     """Usage: reallocate_person <person_identifier> <new_room_name>"""
    #
    #     amity.reallocate_office(args)

    # @docopt_cmd
    # # def do_load_people(self, args):
    #     """Usage: load_people"""
    #
    #     amity.load_people(args)
    #
    # @docopt_cmd
    # def do_load_state(self, args):
    #     """Usage: load_state <sqlite_database>"""
    #
    #     amity_database.load_state(args)
    #
    # @docopt_cmd
    # def do_save_state(self, args):
    #     """Usage: save_state [--db=sqlite_database]"""
    #
    #     amity_database.save_state({"--db": 'amity.db'})
    #
    # @docopt_cmd
    # def do_print_allocations(self, args):
    #     """Usage: print_allocations [-o=filename]"""
    #
    #     print(Amity().print_allocations(args))
    #
    # def do_print_unallocated(self, args):
    #     """Usage: print_unallocated [-o=filename]"""
    #
    #     print(Amity().print_unallocated(arg))
    #
    # @docopt_cmd
    # def do_print_room(self, args):
    #     """Usage: pprint_room <room_name>"""
    #
    #     print(Amity().print_room(args))
    # def do_quit(self, args):
    #     """Quits out of Interactive Mode."""
    #
    #     # print(amity_db.save_state({"--db": 'amity.db'}))
    #     print('Thank You!')
    #     exit()


# print(amity_db.load_state({"<sqlite_database>": 'amity.db'}))
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
