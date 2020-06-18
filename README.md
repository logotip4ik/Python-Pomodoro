# Python Pomodoro
Simple python implementation of pomodoro. In future will be added way more functionality.

## Instalation

1. Firstly install dependencies:
    ```bash
    pip install py-notifier win10toast pyfiglet
    ```
2. Then clone this repository:
    ```bash
    git clone https://github.com/logotip4ik/Python-Pomodoro.git
    ```

## Usage
Usage is very simple:
```bash
python pomodoro.py --help
usage: pomodoro.py [-h] [-r [RELAX]] [min]

Process time to work

positional arguments:
  min                   Time to work(default is 25 min)

optional arguments:
  -h, --help            show this help message and exit
  -r [RELAX], --relax [RELAX]
                        Time to relax(default is 5 min)
```

if you does not provide any argument timer will start with 25 min. and 5 min. for rest. You can provide custom time to work simply passsing ineteger after the ``pomodoro.py`` and custom time for break provides with ``-r`` or ``--relax`` argument, like that ``pomodoro.py -r 10``

## What I learned
* New build in functions
* How to send desktop notification in python

## Licence
[MIT](https://choosealicense.com/licenses/mit/)
