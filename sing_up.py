import sqlite3
import os
from random import *
import string
import random


def create():

    try:

        ID = int(input("Enter your national ID : "))

        cr.execute("select id from customers")
        Ids = cr.fetchall() # select all ids from row
        lenth = len(Ids)
        i = 0
        while i < lenth:               # check if input id is exist in row
            if ID == (Ids[i][0]):     # Ith tuple in list and 0th in the tuple (the value of id)
                print ("this ID is already exist \nplease make sure from your ID")
                break
            i += 1
        #--------------------------------------------------------------------
        else:

            fullname = str(input("Enter your name : "))
            user = ''.join(fullname[:3]) + ''.join(str(randrange(1000)))  # creare randome user name by first 3 character of name
        #--------------------------------------------
            phone = int(input("Enter your phone number : "))
        #--------------------------------------------
            letters = string.ascii_lowercase  # all characters as lower case
            passw = ''.join(random.choice(letters) for i in range(3)) + ''.join(str(randrange(20)) for i in range(3)) # random password
            #--------------------------------------------------------------------
        # if customer need to add money

            print("Do you want to deposit an amount of money in your account?")
            print("1- Yes \n2- Not now")
            deposit = int(input("Enter choise : "))

            if deposit == 1: # add money
                print("Choose type of deposit account ")   # choise type of accont 
                print("1- Saving \n2- Current \n3- Fixed ")
                typ = int(input("Enter choise : "))

            #--------------------------------------------------------------------
                if typ ==1 :   # if type is saving 
                    print("Enter the amount of money to be deposited as integer number : ")
                    money = int(input())   # save the amount of money in this var to add in data base
                    the_type = "saving"    # type of accont to save in data base
                #--------------------------------------------

                if typ == 2:   # if type is current  
                    print("Enter the amount of money to be deposited as integer number : ")
                    money = int(input())   # 
                    the_type = "current"
                #--------------------------------------------

                elif typ == 3:  # if type is fixed will choise of type of fixed
                    print("Enter type of fixed")
                    print("1- Fixed for 1 year with a profit value of 10%")
                    print("2- Fixed for 2 year with a profit value of 25%")
                    print("3- Fixed for 3 year with a profit value of 40%")
                    type2 = int(input("Enter choise : "))

                    if type2 == 1 :
                        the_type = "Fixed for 1 year"  # type will be stored in data base
                        money = int(input("Enter the amount of money as integer number : "))

                    elif type2 == 2 : 
                        the_type = "Fixed for 2 year"
                        money = int(input("Enter the amount of money as integer number : "))

                    elif type2 == 3 : 
                        the_type = "Fixed for 3 year"
                        money = int(input("Enter the amount of money as integer number : "))

                    else: 
                        "invalid choise"
                        money = 0
                #--------------------------------------------
            #--------------------------------------------------------------------
            elif deposit == 2:  money = 0
            #--------------------------------------------------------------------
            else:
                print("invalid choice")
                money = 0

        #===================================================================================================================
            cr.execute(f"insert into customers values('{ID}', '{fullname}', '{phone}', '{user}','{passw}','{money}')")
            commit()

            print(f"hello {fullname} successfully registered \nyour user_name is >> {user} \nyour password is >> {passw}")

    except:
        print("there is an error in you data. please try again using correct data")
