
from create_acc import *

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit_close():
    db.commit()
    db.close()


def login():
    user_input = str(input("User Name : "))
    password_input = str(input("Password : "))

    cr.execute("select user_name from customers")
    users = cr.fetchall()

    lenth = len(users)
    i = 0
    while i < lenth:
        if user_input == users[i][0]:

            cr.execute(f"select password from customers where user_name = '{user_input}'")
            password_data = cr.fetchone()

            if password_input == password_data[0]:
                print("Login successful")
            else:
                print("wrong password")


            break
        i += 1

    else:
        print("this user is not exist")



if __name__ == '__main__':
    login()
