
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()

def use_account():

    os.system("clear")
    print("-"*50)

    acc_ID = int(input("Enter the account ID: "))

    try:  # this to check if ID is exist or not , if not not exist will be print error and move to main except
        cr.execute(f"select * from accounts where ID_acc = '{acc_ID}'")
        time.sleep(1)
        acc_data = cr.fetchall()

        for i in range(2):
            print(".")
            time.sleep(1)

        os.system("clear")
        print("-" * 50)

        print("\n1- withdrawal \n2- deposit \n3- transfer \n"
              "4- show details of account \n5- show history \n6- delete the account")

        transaction = int(input("Enter choice: "))
        time.sleep(1)

        if transaction == 1: print("withdrawal")
        elif transaction == 2: print("deposit")
        elif transaction == 3: print("transfer")
        elif transaction == 4: print("show details of account")
        elif transaction == 5: print("show history")
        elif transaction == 6: print(" delete the account")



    except:
        print("this ID is not exist \n1- try agian \n2- exit")
        try_again = int(input(">>: "))
        if try_again == 1 : use_account()
        else: raise
        time.sleep(1)







def edit_profile():
    print("edit function")


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
                    print("-" * 50)
                    time.sleep(1)
                    return 0
                    # return password_data[0]

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

def profile():
    try:
        os.system("clear")
        print("-"*50)
        for i in range(2):
            print(".")
            time.sleep(1)
        x = 'mso238'
        cr.execute(f"select * from customers where user_name = '{x}'")
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
            use_account()

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



if __name__ == '__main__':

    # if login():
    profile()
