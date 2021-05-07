import sqlite3
import os
import string
import random
import json
import datetime
import time

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def create_account(id_owner):

    global the_type
    try:
        os.system('clear')
        print("-"*50)
        
        print("Enter the type of account \n------------------")
        print("1- Fixed for 1 year the profits value is 10% ")
        print("2- Fixed for 2 year the profits value is 25% ")
        print("3- Saving without profits \n")

        typ = int(input("Enter choice : "))

        time.sleep(1)
        os.system('clear')
        print("-"*50)


        if typ == 1 or typ == 2:
            print(
                f"""
            In this account the profits of money will added after {typ} year from the date that you will deposit the money
            After this year, the profits value will be added in you account and you can take it.
            In the event that you withdrew your money before the year, no profits will be added to the money
            After this year the profits adding will be stop, you can renew your deposit
            """)
            
            print("1- I agree \n2- exit")
            m = int(input("Enter choice : "))
            if m == 1: 
                if typ == 1: the_type = "Fixed 1 year"
                elif typ == 2: the_type = "Fixed 2 year"

            elif m == 2:  return 0
            
            else: raise
            
        elif typ == 3:
            print("""
            In this account you will save your money without profits.
            You can add or withdrew money any time from any ATM 
            """)

            print("1- I agree \n2- exit")
            m = int(input("Enter choice : "))
            if m == 1:
                the_type = "Saving"

            elif m == 2:  return 0

            else: raise

        else : raise

        ID_acc = random.randrange(10000)  # ID of account will be added in data base

        # ==================== if customer need to add money ============================================

        time.sleep(1)
        os.system('clear')
        print("-"*50)

        print("\n Do you want to deposit an amount of money in your account?")
        print("1- Yes \n2- Not now")
        deposit = int(input("Enter choice : "))

        time.sleep(1)
        os.system('clear')
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

                #----------------get the time that add money to be calculates the time that will be added the profits----------------
                
                month = int(the_date.strftime("%-m"))
                day = int(the_date.strftime("%-d"))
                total_minutes = int(the_date.strftime("%-I"))*60 + int(the_date.strftime("%-M"))  # this to calculate the time that will added profits after it
                
                #--------------------second key in dictionary acc_ID will be time and date of deposit --------------------
                data[str(ID_acc)]["date_time"] = [month, day,total_minutes]
                
                open_json_w = open("history.json","w")
                json.dump(data,open_json_w,indent = 2)

        #-------------------------------------------------------
        elif deposit == 2: 
            money = 0
            time.sleep(1)
            return 0
        #--------------------------------------------------------------------
        else:
            print("invalid choice")
            money = 0
            return 0

        os.system('clear')
        print("-"*50)
        print('please wait, your data are uploading now')

        for i in range(2):
            print(".")
            time.sleep(1)

        db2 = sqlite3.connect("data.db")
        cr2 = db2.cursor()
        cr2.execute(f"insert into accounts values('{ID_acc}', '{the_type}','{money}','{0}','{id_owner}')")
        db2.commit()
        db2.close()

        print("done")
        print("creating account has been successfully")

    except:

        os.system('clear')
        print("-"*50)
        print('there is an error, try again')

        for i in range(2):
            print(".")
            time.sleep(1)

        create_account(id_owner)


if __name__ == "__main__":

    x = int(input(" : "))
    create_account(x)
