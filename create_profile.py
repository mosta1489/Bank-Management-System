
from create_acc import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))

db = sqlite3.connect("data.db")
cr = db.cursor()

def commit():
    db.commit()
    db.close()


def create():

    global create
    os.system('clear')
    print("-"*50)

    print(
        '''
        Warning !!
        If you entered any wrong input or wrong data, Everything will be returned from the beginning 
        ''')
    print("-"*50)

    try:

        ID = int(input("Enter your national ID \n\n>>> "))

        time.sleep(1)
        os.system('clear')
        print("-"*50)

        cr.execute("select id from customers")
        Ids = cr.fetchall() # select all ids from row

        length = len(Ids)
        i = 0
        while i < length:               # check if input id is exist in row
            if ID == (Ids[i][0]):     # Ith tuple in list and 0th in the tuple (the value of id)
                print ("this ID is already exist. please make sure from your ID")
                print ("-"*50)

                raise
                # ^^^ this is deliberated error to exited from the function and move to except and call function from beginning

            i += 1
        #--------------------------------------------------------------------
        else:
            fullname = str(input("Enter your name \n\n>>> "))
            user = ''.join(fullname[:3]) + ''.join(str(random.randrange(1000)))  # create random user name by first 3 character of name
            
            time.sleep(1)
            os.system('clear')
            print("-"*50)     
            
            #--------------------------------------------
            phone = int(input("Enter your phone number \n\n>>> "))

            time.sleep(1)
            os.system('clear')
            print("-"*50)


            #--------------------------------------------
            letters = string.ascii_lowercase  # all characters as lower case
            passw = ''.join(random.choice(letters) for i in range(3)) + ''.join(str(random.randrange(20)) for i in range(3)) # random password
            
        #===================================================================================================================
        cr.execute(f"insert into customers values('{ID}', '{fullname}', '{phone}', '{user}','{passw}')")
        commit()

        print("please wait, your data are uploading now")

        for i in range(3):
            print(". ")
            time.sleep(1)
        
        print("-"*50)

        print(
            f"""
        hello {fullname} the registering has been successful
        
        your user_name is >> {user}
        
        your password is >> {passw}
        
            """)
        
        print("-"*50)
        print("-"*50)
        
        time.sleep(1)

        print("do you need create an account now?")
        print("1- Yes \n2- Not now")
        create = int(input("Enter choice : "))

        time.sleep(1)
        os.system('clear')
        print("-"*50)
        
        if create == 1:
            create_account(ID)
        else:
            return 0


    except:
        print("-"*50)
        print("-"*50)
        print("there is an error.please try again")
        print(".\n"*3)

        time.sleep(2)

        create()



if __name__ == '__main__':
    create()