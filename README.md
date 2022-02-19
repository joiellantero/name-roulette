```text
 ________   ________  _____ ______   _______           ________  ________  ___  ___  ___       _______  _________  _________  _______      
|\   ___  \|\   __  \|\   _ \  _   \|\  ___ \         |\   __  \|\   __  \|\  \|\  \|\  \     |\  ___ \|\___   ___\\___   ___\\  ___ \     
\ \  \\ \  \ \  \|\  \ \  \\\__\ \  \ \   __/|        \ \  \|\  \ \  \|\  \ \  \\\  \ \  \    \ \   __/\|___ \  \_\|___ \  \_\ \   __/|    
 \ \  \\ \  \ \   __  \ \  \\|__| \  \ \  \_|/__       \ \   _  _\ \  \\\  \ \  \\\  \ \  \    \ \  \_|/__  \ \  \     \ \  \ \ \  \_|/__  
  \ \  \\ \  \ \  \ \  \ \  \    \ \  \ \  \_|\ \       \ \  \\  \\ \  \\\  \ \  \\\  \ \  \____\ \  \_|\ \  \ \  \     \ \  \ \ \  \_|\ \ 
   \ \__\\ \__\ \__\ \__\ \__\    \ \__\ \_______\       \ \__\\ _\\ \_______\ \_______\ \_______\ \_______\  \ \__\     \ \__\ \ \_______\
    \|__| \|__|\|__|\|__|\|__|     \|__|\|_______|        \|__|\|__|\|_______|\|_______|\|_______|\|_______|   \|__|      \|__|  \|_______|
```

# Name Roulette

A simple command line program that randomly selects a name from a list.

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Features

1. Randomly choose a name from a `.csv` or `.txt` file.
2. Settings

    | Positional Arguments        | Desciption     |
    |--------------|----------------|
    | filename     | A `.csv` or `.txt` file containing the list of names. The names should be separated by new line. See [Names Database](#names-database) for examples.|
    | amount       | The number of random people to be chosen in one go.|

    | Optional Arguments        | Desciption     |
    |--------------|----------------|
    | `--repeat`   | With flag: select a random name (without removing it from the list) forever. <br> Without flag (default): select a random name (and remove it from the list) until the list is empty. |
    | `--display`  | Show the list of names. |
    | `--cowsay`  | Show chosen name/s with cowsay illustration. |

## Getting Started

> Prerequisite: Python 3 must be installed.

- Download the latest [release](https://github.com/joiellantero/name-roulette/releases/tag/v2.1.0) or clone the repository
  
    ```shell
    git clone https://github.com/joiellantero/name-roulette.git
    ```

- Navigate to the directory of the project.
- Create a virtual environment.

    ```shell
    virtualenv env
    ```

- Activate the virtual environment.

    > for macOS and linux

    ```shell
    source env/bin/activate
    ```

    > for windows

    ```shell
    Scripts/activate.bat
    ```

- Install the dependencies

    ```shell
    pip install -r requirements.txt
    ```

- Run the program

    > Format: `python3 name-roulette.py <fileName> <amount> <flags>`

    ```shell
    python3 name-roulette.py names.csv 3 --cowsay
    ```

## Names Database

The names to be used in the program are read from either a `.csv` or `.txt` file. This repository includes examples of the files mentioned. Proper formatting should be followed in creating these files. 

An example formatting for the `.csv` file is shown below. Notice that there is no column name and each name is entered in a new row under one column.

> names.csv

```text
eren
mikasa
armin
levi
hange
erwin
sasha
jean
```

An example formatting for the `.txt` file. Notice that each name is entered in a new line.

> names.txt

```text
connie
historia
annie
reiner
pieck
falco
```

## The Future

- I am currently developing an open-source website version of this and I will make the repository public once I finish it. I'm building it using ReactJS and Tailwind CSS. 

## Author

- Joie Llantero

## License

- [MIT license](http://opensource.org/licenses/mit-license.php)
