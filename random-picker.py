from cowsay import *
import random
import itertools
import threading
import time
import sys
import os

name = []
i = 0
again = 0
sleep_time = 1

# loading animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rchoosing someone... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

# take all the names
while (i != 'done'):
    i = input('Enter name: ')
    if i != 'done':
        name.append(i)

# choose a random name from list name
while (True):
    chosen_name = random.choice(name)

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # do loading animation
    done = False

    t = threading.Thread(target=animate)
    t.start()

    #long process here
    time.sleep(sleep_time)
    done = True

    # clear terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # display the chosen name
    print(dragon(chosen_name))
    again = input("Again? [y/n]: ")
    if (again == 'y' or again == 'Y'):
        continue
    else:
        break
