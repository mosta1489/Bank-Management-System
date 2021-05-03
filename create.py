import sqlite3
import os
from random import *
import string
import random
import json
import datetime
from os import *
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))
db = sqlite3.connect("data.db")
cr = db.cursor()

def commit():
    db.commit()
    db.close()


def create():

    print(
        '''
        Warning !!
        If you entered any wrong input or wrong data, Everything will be returned from the beginning 
        ''')
    print("-"*50)

    try:

        ID = int(input("Enter your national ID \n\n>>> "))

        time.sleep(1)
        system('clear')
        print("-"*50)

        cr.execute("select id from customers")
        Ids = cr.fetchall() # select all ids from row
        lenth = len(Ids)
        i = 0
        while i < lenth:               # check if input id is exist in row
            if ID == (Ids[i][0]):     # Ith tuple in list and 0th in the tuple (the value of id)
                print ("this ID is already exist. please make sure from your ID")
                print ("-"*50)

                error 
                # ^^^ this is deliberated error to exite from the function and move to except and call function from beginning  

            i += 1
        #--------------------------------------------------------------------
        else:
            fullname = str(input("Enter your name \n\n>>> "))
            user = ''.join(fullname[:3]) + ''.join(str(randrange(1000)))  # creare randome user name by first 3 character of name
            
            time.sleep(1)
            system('clear')
            print("-"*50)     
            
            #--------------------------------------------
            phone = int(input("Enter your phone number \n\n>>> "))

            time.sleep(1)
            system('clear')
            print("-"*50)


            #--------------------------------------------
            letters = string.ascii_lowercase  # all characters as lower case
            passw = ''.join(random.choice(letters) for i in range(3)) + ''.join(str(randrange(20)) for i in range(3)) # random password
            
            # ===============================  Type of account ============================================
            print("Enter the type of account \n------------------")
            print("1- Fixed for 1 year the profits value is 10% ")
            print("2- Fixed for 2 year the profits value is 25% ")
            print("3- Saving without profits \n")

            typ = int(input("Enter choise : "))

            time.sleep(1)
            system('clear')
            print("-"*50)


            if typ == 1 or typ == 2:
                print(
                    f"""
                In this account the profits of money will added after {typ} year from the date that you will deposit the money.
                After this year, the profits value will be added in you accoun and you can take it.
                In the event that you withdrew your money before the year, no profits will be added to the money
                After this year the profits adding will be stoped, you can renew your deposit
                """)
                
                print("1- I agree \n2- exit")
                m = int(input("Enter choise : "))
                if m != 1:  error

                if typ == 1: the_type = "Fixed 1 year"
                
                elif typ == 2: the_type = "Fixed 2 year"

            elif typ == 3:
                print(
                f"""
                In this account you will save your money without profits.
                You can add or withdrew money any time from any ATM 
                """)

                print("1- I agree \n2- exit")
                m = int(input("Enter choise : "))
                if m != 1:  error

                the_type = "Saving"

            else : error

        
        ID_acc = randrange(10000)  # ID of account will be added in data base

        # ==================== if customer need to add money ============================================
        
        time.sleep(1)
        system('clear')
        print("-"*50)
        
        print("\n Do you want to deposit an amount of money in your account?")
        print("1- Yes \n2- Not now")
        deposit = int(input("Enter choise : "))
        
        time.sleep(1)
        system('clear')
        print("-"*50)

        #-------------------------------------------------------------------------
        if deposit == 1: # add money
            money = int(input("Enter the amount of money as integer number \n\n>>> "))

            time.sleep(1)

            if money != 0:
                the_date = datetime.datetime.now()
                date_time= the_date.strftime("%d/%B/%Y") + " at " + the_date.strftime("%I:%M %p")

                #-------------------------save history in json file----------------------------------------

                open_json_r = open("history.json","r")
                data = json.load(open_json_r)

                data[str(ID_acc)] = {}
                #--------------------first key in dictionary acc_ID will be history --------------------
                data[str(ID_acc)]["history"] = [f"added {money}$ at {date_time}"]

                #----------------get the time that add mony to be calaculate the time that will be added the profits----------------
                
                month = int(the_date.strftime("%-m"))
                day = int(the_date.strftime("%-d"))
                total_minutes = int(the_date.strftime("%-I"))*60 + int(the_date.strftime("%-M"))  # this to calculate the time that will added profits after it
                
                #--------------------second key in dictionary acc_ID will be time and date of deposit --------------------
                data[str(ID_acc)]["date_time"] = [month, day,total_minutes]
                
                open_json_w = open("history.json","w")
                json.dump(data,open_json_w,indent = 2)

        #-------------------------------------------------------
        elif deposit == 2: money = 0
        #--------------------------------------------------------------------
        else:
            print("invalid choice")
            money = 0

        cr.execute(f"insert into accounts values('{ID_acc}', '{the_type}','{money}','{0}')")

        #===================================================================================================================
        cr.execute(f"insert into customers values('{ID}', '{fullname}', '{phone}', '{user}','{passw}','{ID_acc}')")
        commit()

        system('clear')
        print("-"*50)
        time.sleep(1)
        print("please wait, your data are uploading now")

        for i in range(3):
            print(". ")
            time.sleep(1)
        
        print("-"*50)

        print(
            f"""
        hello {fullname} the registering has been succesfully
        
        your user_name is >> {user}
        
        your password is >> {passw}
        
        the ID of your account is >> {ID_acc}
            """)
        
        print("-"*50)


    except:
        print("-"*50)
        print("-"*50)
        print("there is an error.please try again")
        print(".\n"*3)

        time.sleep(2)

        create()



if __name__ == '__main__':
    create()