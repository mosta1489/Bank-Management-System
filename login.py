
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()

def use_account():
    pass

def edit_profile():
    pass


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

        cr.execute(f"select * from customers where user_name = '{user_input}'")
        data = cr.fetchall()
        name = data[0][1].split()
        print(f"hello {name[0]} in our bank \nby this profile you can control in your bank accounts ")
        print("-"*50)

        print(f"your ID is '{data[0][0]}'")
        print("-"*50)

        time.sleep(1)
        print("1- enter to an account \n2- create a new account \n3- edit my profile")
        choice = int(input("Enter choice: "))

        if choice == 1:   # enter to an account
            time.sleep(1)
            os.system("clear")
            print("-"*50)
            acc_ID = int(input("Enter the account ID: "))

            try:   # this to check if ID is exist or not , if not not exist will be print error and move to main except
                cr.execute(f"select * from account where ID_acc = '{acc_ID}'")
                acc_data = cr.fetchall()

                time.sleep(1)
                use_account()


            except:
                print("this ID is not exist. try again..")
                time.sleep(1)
                raise


            use_account()

        elif choice == 2:
            create_account()

        elif choice == 2:
            edit_profile()

        else:
            print("Invalid choice. try again..")
            time.sleep(1)
            raise

    except:
        profile()



if __name__ == '__main__':

    if login():
        profile()
