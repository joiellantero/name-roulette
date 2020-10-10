from cowsay import *
import random
import itertools
import threading
import time
import sys
import os

name = []
again = 0
sleep_time = 1

# loading animation
def loading_animation():
    done = False

    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rchoosing someone... ' + c)
            sys.stdout.flush()
            time.sleep(0.1)

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(sleep_time)
    done = True

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_names():
    i = 0
    # take all the names
    print("Please enter all the names then type 'done' when you're finished.")
    while (i != 'done'):
        i = input('Enter name: ')
        if i != 'done':
            name.append(i)

def repeat():
    again = input("Again? [y/n]: ")
    if ((again == 'y' or again == 'Y') and len(name)!=0):
        return
    else:
        while again != 'n' and again != 'y':
            print("Choices: y for yes or n for no.")
            again = input("Again? [y/n]: ")
        if (again == 'n'):
            print("Program ended")
            sys.exit(0)
        elif (again == 'y' or again == 'Y') and len(name)==0:
            print("No more names to choose from")
            sys.exit(0)
        else:
            return

def repeat_forever():
    get_names()
    # choose a random name from list name
    while (True):
        chosen_name = random.choice(name)

        # clear terminal
        clear_terminal()

        # do loading animation
        loading_animation()

        # clear terminal
        clear_terminal()

        # display the chosen name
        print(dragon(chosen_name))
        repeat()

def repeat_until_last():
    get_names()
    # choose a random name from list name
    while (True):
        chosen_name = random.choice(name)

        # clear terminal
        clear_terminal()

        # do loading animation
        loading_animation()

        # clear terminal
        clear_terminal()

        # display the chosen name
        print(dragon(chosen_name))
        name.remove(chosen_name)
        repeat()

print("Commands:\n1 - repeat until last person\n2 - repeat forever")
cmd = input("choice [1/2]: ")

# repeat until last person
if (int(cmd) == 1):
    repeat_until_last()
# repeat forever
elif (int(cmd) == 2):
    repeat_forever()
# error handling for invalid input
else:
    print("Error: Invalid Choice!")
