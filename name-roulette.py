import cowsay
import itertools
import threading
import time
import sys
import os
import argparse
import pandas as pd

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
    time.sleep(1)
    done = True

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_choose_again():
    again = input("Choose again? [Y/N]: ")
    if (again == 'y' or again == 'Y'):
        return
    elif again == 'n' or again == 'N':
        print("\nProgram ended.")
        sys.exit(0)
    else:
        print("Invalid input: type Y for yes or N for no.")
        ask_choose_again()

def draw_name(df, amount, repeat, display):
    while not df.empty:
        clear_terminal()
        loading_animation()
        clear_terminal()
        chosen_name = []
        for i in range(0, amount):
            if df.empty:
                break
            chosen_name.append(df.loc[df.sample().index[0], 'Names'])
            if not repeat:
                df = df[df["Names"].str.contains(chosen_name[i])==False]
        if display and not df.empty:
            print(df)
        cowsay.tux(', '.join(chosen_name))
        print('')
        ask_choose_again()
    else:
        print("\nProgram Ended.\nList of names is now empty.")
        sys.exit(0)

def get_names(filename):
    try:
        names_df = pd.read_csv(filename, sep=",", header=None, names=["Names"])
        names_df['Names'] = names_df['Names'].astype('string')
        return names_df
    except FileNotFoundError:
        print(f"\nFile '{filename}' does not exist.")
        if filename[-4:] != '.csv' and filename[-4:] != '.txt':
            print(f"Please include file type, e.g., {filename}.txt or {filename}.csv.")
        sys.exit(0)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Name Roulette v2.0.0. A random picker for names. A digital terminal script based on the game spin the bottle.')

    parser.add_argument(
        'file', 
        metavar='filename', 
        type=str, 
        help='Files accepted are csv and txt files. Add the filename of the text or csv file containing the names as an argument, e.g., fileName.csv. Each name should be entered in a new line. You may refer to the README.md to see more examples.'
    )

    parser.add_argument(
        'amount',
        metavar='amount',
        nargs='?',
        default=1,
        type=int,
        help='The number of people to be chosen randomly.'
    )

    parser.add_argument(
        '--repeat', 
        action="store_true", 
        required=False,
        help='Loop through the names of the players forever. Not including the --repeat flag will remove the player from the list once they are chosen.'
    )

    parser.add_argument(
        '--display', 
        action="store_true", 
        required=False,
        help='Show the list of names.'
    )

    args = parser.parse_args()
    draw_name(get_names(args.file), args.amount, args.repeat, args.display)