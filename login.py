
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()


#================================ ---start withdrawal ---===============================================================

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

            if choice != "1" : raise

            time.sleep(1)
            os.system("clear")
            print("-" * 50)

            print("All money will be withdrawn from the account now\n1- continue \n2- exit")
            choice = input("Enter choice: ")

            if choice != "1": raise
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

            if withdrawal_input != 0 and withdrawal_input < acc_data[0][2]:
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
                time.sleep(1)
                raise
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


    except:
        os.system("clear")
        print("1- try again \n0- back")
        choice = input(">>>: ")
        if choice == "1":
            withdrawal(ID_account)
            time.sleep(1)
        else: raise Exception

#================================ ---end withdrawal ---=================================================================

#================================ ---end add_profits ---================================================================

def add_profits(ID_account):

    cr.execute(f"select * from accounts where ID_acc = {ID_account}")
    data_acc = cr.fetchall()
    type = data_acc[0][1]


    if type != "Saving":

        open_js_r = open("history.json", "r")
        date_time = json.load(open_js_r)

        history_date = date_time[str(ID_account)]["date_time"]

        the_date = datetime.datetime.now()

        month = int(the_date.strftime("%-m"))
        day = int(the_date.strftime("%-d"))
        total_minutes = int(the_date.strftime("%-I")) * 60 + int(the_date.strftime("%-M"))

        if month < history_date[0]:
            if day < history_date[1]:
                if total_minutes - history_date[2] >= 60:
                    pass
                else:
                    return 0

        money = data_acc[0][2]

        global the_profits
        if type == "Fixed 1 year":
            the_profits = money * .1
        elif type == "Fixed 2 year":
            the_profits = money * 2.5

        cr.execute(f"update accounts set profits = {the_profits} where ID_acc = {ID_account}")
        commit_close()

# ================================ ---end add_profits ---===============================================================

# ================================ ---start show details of account ---=================================================

def show_details(ID_account):
    os.system("clear")
    print("-"*50)
    print("wait...")
    time.sleep(1)
    for _ in range(2):
        print(".")
        time.sleep(1)
    os.system("clear")
    print("-"*50)

    cr.execute(f"select * from accounts where ID_acc = {ID_account}")
    data_base = cr.fetchall()
    print(f"the ID of account is >>> {ID_account}")
    print("-"*50)
    time.sleep(1)

    print(f"the ID of owner of this account is >>> {data_base[0][4]}")
    print("-"*50)
    time.sleep(1)

    print(f" the type of account is >>> {data_base[0][1]}")
    print("-"*50)
    time.sleep(1)

    print(f" you have>>> {data_base[0][2]}$ in this account")
    if data_base[0][1] != "Saving":
        profits = data_base[0][3]
        if profits == 0:
            print("profits have not been added yet")
        else:
            print(f"the profits of account is >>> {profits}")
    print("-"*50)
    time.sleep(1)
    
    inp = input("press any key to back:  ")
    if inp:
        raise Exception

# ================================ ---end show details of account ---===================================================

# ================================ --- start show_history ---===========================================================

def show_history(ID_account):
    time.sleep(1)
    os.system("clear")
    print("-"*50)
    time.sleep(1)

    history_data = json.load(open("history.json", "r"))
    
    print_data = history_data[str(ID_account)]["history"]

    print(" Transactions history \n")
    time.sleep(1)
    for i in print_data:
        print(f">> {i}\n")
        time.sleep(1)

# ================================ --- end show_history ---=============================================================

# ================================ ---start use_account ---=============================================================

def use_account(owner_ID):

    os.system("clear")
    print("-"*50)

    try:

        acc_ID_input = int(input("Enter the account ID: "))

        db2 = sqlite3.connect("data.db")
        cr2 = db2.cursor()
        cr2.execute(f"select ID_acc from accounts where owner = '{owner_ID}'")
        IDs = cr2.fetchall()
        length = len(IDs)
        i = 0
        while i < length:
            if acc_ID_input == IDs[i][0]:
                break
            i += 1
        else:
            print("\nYou do not have an account with this ID")
            time.sleep(1)
            raise

        add_profits(acc_ID_input)

        cr2.execute(f"select * from accounts where ID_acc = '{acc_ID_input}'")
        acc_data = cr2.fetchall()

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
        elif transaction == 4: show_details(acc_ID_input)
        elif transaction == 5: show_history(acc_ID_input)
        elif transaction == 6: print(" delete the account")
        else: raise


    except Exception:
        use_account(owner_ID)

    except:
        os.system("clear")
        print("1-try again \n2- back")
        choice = input(">>>: ")
        if choice == "1":
            use_account(owner_ID)
            time.sleep(1)
        else: raise Exception

#================================ ---end use_account ---================================================================

#================================ ---start edit_profile ---=============================================================

def edit_profile():
    print("edit function")

#================================ ---end edit_profile ---===============================================================

#================================ ---start profile ---==================================================================

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


    except Exception:
        time.sleep(1)
        profile()

    except:
        os.system("clear")
        print("1-try again \n2- back")
        choice = input(">>>: ")
        if choice == "1":
            profile()
            time.sleep(1)
        else: raise Exception

#================================ ---end profile ---====================================================================

#================================ ---start login ---====================================================================

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


    except Exception:
        time.sleep(1)
        login()

    except:
        os.system("clear")
        print("1-try again \n2- back")
        choice = input(">>>: ")
        if choice == "1":
            login()
            time.sleep(1)
        else: raise Exception

#================================ ---end login ---======================================================================


if __name__ == '__main__':
    pass
    login()
    # profile()
    # use_account(500)
    # withdrawal(1450)
    # show_details(1450)
    # add_profits(2301)
    # show_history(259)