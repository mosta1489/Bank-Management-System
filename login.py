
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()


#=========================================---start withdrawal ---=======================================================

def withdrawal(ID_account):
    global withdrawal_input
    time.sleep(1)
    os.system("clear")
    print("-" * 50)
    cr.execute(f"select * from accounts where ID_acc = {ID_account}")
    acc_data = cr.fetchall()

    try:

        # -------------------------- if acc is Fixed --------------------------------------------------------
        if acc_data[0][1] == "Fixed 1 year" or acc_data[0][1] == "Fixed 2 year":
            time.sleep(1)
            print("warning !! \nthis is fixed account if you if you withdrawal money, you will lose the profits \n")
            print("1- continue \n2- exit")
            choice = input("Enter choice: ")

            if choice != "1" : raise Exception

            time.sleep(1)
            os.system("clear")
            print("-" * 50)

            print("All money will be withdrawn from the account now\n1- continue \n2- exit")
            choice = input("Enter choice: ")

            if choice != "1": raise Exception
            for _ in range(2):
                print(".")
                time.sleep(1)

            # ---------------------- edit money in data bas -----------------------------------

            cr.execute(f"update accounts set money = {0} where ID_acc = {ID_account}")
            cr.execute(f"update accounts set profits = {0} where ID_acc = {ID_account}")
            commit_close()

            # ----------------------------------------------------------------------------------
            withdrawal_input = acc_data[0][2] # for use in history file

        #--------------------------------------------------------------------------------------------------------


        # -------------------------- if acc is saving --------------------------------------------------------

        elif acc_data[0][1] == "Saving":
            withdrawal_input = int(input("Enter the amount of money that you need to withdrawal: \n>>> "))
            if withdrawal_input < acc_data[0][2]:
                time.sleep(1)
                os.system("clear")
                print("-" * 50)
                print("please wait")
                for _ in range(2):
                    print(".")
                    time.sleep(1)

                #---------------------- edit money in data bas -----------------------------------
                new_money = acc_data[0][2] - withdrawal_input
                cr.execute(f"update accounts set money = {new_money} where ID_acc = {ID_account}")
                commit_close()
                # ----------------------------------------------------------------------------------
            else:
                for _ in range(2):
                    print(".")
                    time.sleep(1)
                print("This amount cannot be withdrawn.\n")
                raise Exception
        #------------------------- add history in json file ----------------------------------------
        the_date = datetime.datetime.now()
        date_time = the_date.strftime("%d/%B/%Y") + " at " + the_date.strftime("%I:%M %p")

        new_history = f"{withdrawal_input}$ was withdrawn  at {date_time}"

        open_json_r = open("history.json", "r")
        json_data = json.load(open_json_r)
        json_data[str(ID_account)]["history"].append(new_history)

        open_json_w = open("history.json", "w")
        json.dump(json_data, open_json_w, indent = 2)
        # ------------------------------------------------------------------------
        print("done")


    except ValueError:
        print("failed. try again..")
        time.sleep(1)
        for _ in range(2):
            print(".")
            time.sleep(1)
        raise

    except Exception:
        time.sleep(1)
        raise

#================================ ---end withdrawal ---=================================================================


# ================================ ---start use_account ---=================================================================

def use_account(owner_ID):

    os.system("clear")
    print("-"*50)


    try:  # this to check if ID is exist or not , if not not exist will be print error and move to main except

        acc_ID_input = int(input("Enter the account ID: "))

        cr.execute(f"select ID_acc from accounts where owner = '{owner_ID}'")
        IDs = cr.fetchall()
        length = len(IDs)
        i = 0
        while i < length:
            if acc_ID_input == IDs[i][0]:
                break
            i += 1
        else:
            print("You do not have an account with this ID")
            raise


        cr.execute(f"select * from accounts where ID_acc = '{acc_ID_input}'")
        time.sleep(1)
        acc_data = cr.fetchall()
        for i in range(2):
            print(".")
            time.sleep(1)

        os.system("clear")
        print("-" * 50)

        print("\n1- withdrawal \n2- deposit \n3- transfer \n"
              "4- show details of account \n5- show history \n6- delete the account \n")

        transaction = int(input("Enter choice: "))
        time.sleep(1)

        # to do

        if transaction == 1: withdrawal(acc_ID_input)
        elif transaction == 2: print("deposit")
        elif transaction == 3: print("transfer")
        elif transaction == 4: print("show details of account")
        elif transaction == 5: print("show history")
        elif transaction == 6: print(" delete the account")



    except:
        os.system("clear")
        print("1-use account \n2- back")
        x = input(">>>: ")
        if x == "1":
            use_account(owner_ID)
            time.sleep(1)
        else: raise

#================================ ---end use_account ---=================================================================


#================================ ---start edit_profile ---=================================================================

def edit_profile():
    print("edit function")

#================================ ---end edit_profile ---=================================================================


#================================ ---start profile ---=================================================================

def profile():
    try:
        os.system("clear")
        print("-"*50)
        for i in range(2):
            print(".")
            time.sleep(1)
        os.system("clear")
        cr.execute(f"select * from customers where user_name = '{user_input}'")
        data = cr.fetchall()
        name = data[0][1].split()
        print(f"hello {name[0]} in our bank \nby this profile you can control in your bank accounts ")
        print("-"*50)

        ID_owner = data[0][0]

        print(f"your ID is '{ID_owner}'")
        print("-"*50)

        time.sleep(1)
        print("1- enter to an account \n2- create a new account \n3- edit my profile")
        choice = int(input("Enter choice: "))

        if choice == 1:   # enter to an account
            time.sleep(1)
            use_account(ID_owner)

        elif choice == 2:
            create_account(ID_owner)

        elif choice == 2:
            edit_profile()

        else:
            print("Invalid choice. try again..")
            time.sleep(1)
            raise

    except:
        profile()

#================================ ---end profile ---=================================================================


#================================ ---start login ---=================================================================

def login():
    try:
        os.system('clear')
        print("-"*50)
        time.sleep(1)

        global user_input
        user_input = input("User Name : ")

        cr.execute("select user_name from customers")
        users = cr.fetchall()
        length = len(users)

        i = 0
        while i < length:
            if user_input == users[i][0]:
                time.sleep(1)
                password_input = str(input("Password : "))
                cr.execute(f"select password from customers where user_name = '{user_input}'")
                password_data = cr.fetchone()

                for i in range(2):
                    print(".")
                    time.sleep(1)
                if password_input == password_data[0]:
                    print("Login successful")
                    # print("-" * 50)
                    # time.sleep(1)
                    profile()
                    return 0

                else:
                    time.sleep(1)
                    print("wrong password \ntry agian...")
                    print("-" * 50)
                    for i in range(2):
                        print(".")
                        time.sleep(1)
                    raise
            i += 1

        else:
            print("this user is not exist \ntry agian...")
            print("-"*50)
            for i in range(2):
                print(".")
                time.sleep(1)
            raise

    except:
        os.system('clear')
        login()

#================================ ---end login ---=================================================================


if __name__ == '__main__':

    login()
    # profile()
    # use_account()
    # withdrawal(1450)