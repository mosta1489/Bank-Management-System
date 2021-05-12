import sqlite3
from os import *
from random import *
import string
import random
import json
import datetime
import time
import os
from create_profile import *
from login import *


def front_end():
    print("\n             #####  Customer Account Bank Management System  #### \n ")
    print("                      1- Login")
    print("                      2- Create a profile \n")
    inp = int(input("                      Choice : "))

    if inp == 1:
        login()

    elif inp == 2:
        create()

    else:
        print("invalid input ")



front_end()

