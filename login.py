
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()


def login():
    try:
        os.system('clear')
        print("-"*50)
        time.sleep(1)
        
        user_input = str(input("User Name : "))

        cr.execute("select user_name from customers")
        users = cr.fetchall()
        lenth = len(users)

        i = 0
        while i < lenth:
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
                    return password_data[0]

                else:
                    time.sleep(1)
                    print("wrong password \ntry agian...")
                    print("-" * 50)
                    time.sleep(1)
                    raise
            i += 1

        else:
            print("this user is not exist \ntry agian...")
            print("-"*50)
            time.sleep(1.5)
            raise

    except:
        os.system('clear')
        login()

def profile(passw):

    os.system("clear")
    print("-"*50)
    for i in range(2):
        print(".")
        time.sleep(1)

    cr.execute(f"select * from customers where password = '{passw}'")
    data = cr.fetchall()
    print(data)

    print(f"hello {data[0][1]} in our pank \nby this profile you can control in your bank accounts ")
    print("-"*50)

    print(f"your ID is '{data[0][0]}'")
    print("-"*50)

    time.sleep(1)
    print("1- enter to an account \n2- create a new account \n3- edit my profile")




if __name__ == '__main__':

    x = login()
    print(x)
    if x:
        profile(x)
