import argparse
import time
import pyfiglet
import os
from pynotifier import Notification

def main(min, rel):
    min *= 60
    rel = 1 * 60
    while True:
        work = min
        break_ = rel
        Notification("Time to work⚒", "Timer is starting now", 10).send()
        while work:
            mins, secs = divmod(work, 60)
            os.system("CLS")
            print(pyfiglet.figlet_format("{:02d}:{:02d}".format(mins, secs), justify='center', font='big'))
            time.sleep(1)
            work -= 1
        Notification("You can relax now!🥞", "Ok your time is up, just relax☺", 10).send()
        while break_:
            mins, secs = divmod(break_, 60)
            os.system("CLS")
            print(pyfiglet.figlet_format("{:02d}:{:02d}".format(mins, secs), justify='center', font='big'))
            time.sleep(1)
            break_ -= 1




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process time to work")
    parser.add_argument('min', type=int, nargs='?', default=25, help='Time to work(default is 25 min)')
    parser.add_argument('-r', '--relax', type=int, nargs='?', default=5, help='Time to relax(default is 5 min)')
    args = parser.parse_known_args()[0]
    try:
        main(args.min, args.relax)
    finally:
        exit("\nBye, have a good day!")
