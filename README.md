# Name Roulette
A simple command line program which randomly selects a name from a list.

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
![Downloads](https://img.shields.io/github/downloads/joiellantero/name-roulette/total?style=flat-square)

## Features

1. Read `.csv` and `.txt` files.
2. Settings
   
    | Flags        | Desciption     |
    |--------------|----------------|
    | `--repeat`   | With flag: select a random name (without removing it from the list) forever. <br> Without flag: select a random name (and remove it from the list) until the list is empty. |
    | `--display`  | Show the list of names. |

## Getting Started

> Prerequisite: Python 3 must be installed.

- Download the latest release or clone the repository
  
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

    ```shell
    python3 name-roulette.py <fileName> <flags>
    python3 name-roulette.py name.csv --repeat --display
    ```

## Author

- Joie Llantero

## License

- [MIT license](http://opensource.org/licenses/mit-license.php)
