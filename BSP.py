import sqlite3


menu = """
Choose an option
    1.Open new Account
    2.Withdrawal
    3.Deposit
    4.Close An Account
    5.Show all Accounts
    6.Quit"""

def deposit(accnum,amount):
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    cursor.execute(f"SELECT * FROM AccDetails WHERE accnum={accnum} ")
    row = cursor.fetchone()
    updated_amount = row[3]+amount
    cursor.execute(f"UPDATE AccDetails SET Balance={updated_amount} WHERE accnum={accnum}")
    connection.commit()
    connection.close() 

def withdraw(acc_num,amount):
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    cursor.execute(f"SELECT * FROM AccDetails WHERE accnum={acc_num} ")
    row = cursor.fetchone()
    updated_amount = row[3]-amount
    cursor.execute(f"UPDATE AccDetails SET Balance={updated_amount} WHERE accnum={acc_num}")
    connection.commit()
    connection.close() 


def create_table():
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS AccDetails(accnum integer PRIMARY KEY,fname text,lname text,Balance INTEGER)")
    connection.commit()
    connection.close()

def write(fname,lname,bal):
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    cursor.execute("INSERT INTO AccDetails(fname,lname,Balance) VALUES(?,?,?)",(fname,lname,bal))
    connection.commit()
    connection.close()


def format_data(data):
    accdet = [{"Account number ":row[0],"First Name ":row[1],"Last Name ":row[2],"Balance ":row[3]} for row in data]
    for i in accdet:
        print(i)


def extractAccDetails():
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    lst = cursor.execute("SELECT * FROM AccDetails")
    l = cursor.fetchall()
    connection.close()
    format_data(l)


def closeAcc(num):
    connection = sqlite3.connect("Accounts.db")
    cursor =  connection.cursor()
    cursor.execute(f"DELETE FROM AccDetails WHERE accnum={num}")
    connection.commit()
    connection.close()

user_input = 0

create_table()

while (user_input != 6):
    print(menu)
    user = int(input("Enter your choice : "))
    user_input = user
    if (user_input == 1):
        fname = input("Enter first name : ")
        lname = input("Enter last name : ")
        bal = int(input("Enter initial balance : "))
        write(fname,lname,bal)
        print("\n")
        print("Congratulation ! Account Created")
        print(f"First Name : {fname}")
        print(f"Last Name  :  {lname}")
        print(f"Balance : {bal}")
    elif (user_input == 5):
        extractAccDetails()
    elif (user_input == 4):
        accnum = int(input("Enter account number : "))
        closeAcc(accnum)
    elif (user_input == 2):
        acc_num = int(input("Enter account no : "))
        amount = int(input("Enter amount : "))
        withdraw(acc_num,amount)
    elif (user_input == 3):
        accountnumber = int(input("Enter account no : "))
        money = int(input("Enter amount : "))
        deposit(accountnumber,money)
    else:
        if (user_input != 6):
            print("Invalid option !")
        

