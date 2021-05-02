
from create import *
from login import *


def front_end():
    print("\n             #####  Customer Account Bank Management System  #### \n ")
    print("                      1- Login")
    print("                      2- Create An Account \n")
    inp = int(input("                      Choise : "))

    if inp == 1:
        login()

    elif inp == 2:
        create()

    else:
        print("invalid input ")



front_end()

