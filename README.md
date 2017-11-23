[![Build Status](https://travis-ci.org/wanjiku-carol/cp1-amity.svg?branch=ch-remove-unneccessary-packages)](https://travis-ci.org/wanjiku-carol/cp1-amity)

# **AMITY SPACE ALLOCATION APPLICATION**
This is a software that allows for allocation of space to people.

Create a new directory and clone the repository:

> mkdir amity_allocation

> cd amity_allocation

> git clone https://github.com/wanjiku-carol/cp1-amity.git

> cd cp1-amity

Install the requirements

> pip install -r requirements.txt

Run the app

> python docopt_file.py -i

**Features and Usage**

A user can be able to:
1. Create a room and either classify it as an office or living space ```<create_room>```.
2. Add people into the system and classify a person as either a fellow or staff```<person_name> <FELLOW|STAFF>```.
3. Allocate living space to fellows should they want some```[wants_accommodation]```.
4. Allocate office space to a person in the database, whether or a fellow.
5. Re-allocate space to a person```reallocate_person <person_identifier> <new_room_name>```.
6. Load people from a text file into the system a and allocate them rooms```load_people```.
7. Print a list of allocations and those unallocated onto the screen```print_allocations``` & ```print_unallocated```.
8. View a list of people in a room ```print_room```.
9. Save all the data in an SQLite database ```save_state ```.
10. Load data from the database ```load_state```.
