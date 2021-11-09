import sqlite3
import time
get_User_Name = "select Name from Registrants where ID = '{}'"


def sendmail(cur, login_ID):

    Title = input("Title :")
    Receiver = input("Receiver :")
    Content = input("Content :")
    User = cur.execute(get_User_Name.format(login_ID)).fetchone()

    # insert all the data to the table
    cur.execute("insert into Email_system(user_ID , sender, title, receiver, content) values ('{0}','{1}','{2}','{3}','{4}')".format(
        login_ID, User[0], Title, Receiver, Content))


def check_pre_mail(cur, login_ID):
    check_mail = "select title, sender, content, Email_ID from Email_system where receiver = '{}'and New_mail = 0"
    User = cur.execute(get_User_Name.format(login_ID)).fetchone()

    # puts all the tuble where New_mail = 1 and receiver ID is correct into list
    receiver = cur.execute(check_mail.format(User[0])).fetchall()
    Email_num = len(receiver)
    # if empty retrun
    if(len(receiver) == 0):
        print("No previous Email...")
        print("loading", end='')
        for i in range(6):
            print(".", end='')
            time.sleep(0.4)
        print("\n")
        return

    print("You have ", len(receiver), "previous Emails.")
    for i in range(Email_num):
        print(i+1, ")Title :", receiver[i][0])
        print("   From ", receiver[i][1])
    print("==================================")
    print("Which one do you want to read?")
    print("press a number to open it", end='')
    input_num = int(input("Input a Number :"))
    # check which email you wanna read
    while(input_num > Email_num or input_num <= 0):
        print("Error input")
        input_num = int(input("Input a Number :"))
    print("==================================")
    print("Tilte : ", receiver[input_num-1][0])
    print("Send By : ", receiver[input_num-1][1])
    print("Content : ", receiver[input_num-1][2])
    print("==================================")
    print("loading", end='')
    for i in range(6):
        print(".", end='')
        time.sleep(0.4)
    print("\n")


def check_new_mail(cur, login_ID):

    check_mail = "select title, sender, content, Email_ID from Email_system where receiver = '{}'and New_mail = 1"
    User = cur.execute(get_User_Name.format(login_ID)).fetchone()

    # puts all the tuble where New_mail = 1 and receiver ID is correct into list
    receiver = cur.execute(check_mail.format(User[0])).fetchall()
    Email_num = len(receiver)
    # if empty retrun
    if(len(receiver) == 0):
        print("No new Email...")
        print("loading", end='')
        for i in range(6):
            print(".", end='')
            time.sleep(0.4)
        print("\n")
        return

    print("You have ", Email_num, "New Emails.")
    for i in range(Email_num):
        print(i+1, ")Title :", receiver[i][0])
        print("   From", receiver[i][1])
    print("==================================")
    print("Which one do you want to read?")
    print("press a number to open it")
    input_num = int(input("Input a Number :"))
    # check which email you wanna read
    while(input_num > Email_num or input_num <= 0):
        print("Error input")
        input_num = int(input("Input a Number :"))
    print("==================================")
    print("Tilte : ", receiver[input_num-1][0])
    print("Send By : ", receiver[input_num-1][1])
    print("Content : ", receiver[input_num-1][2])
    print("==================================")
    # after reading update the New_mail to false
    cur.execute("update Email_system set New_mail = 0 where Email_ID = '{}'".format(
        receiver[input_num-1][3]))
    print("loading", end='')
    for i in range(6):
        print(".", end='')
        time.sleep(0.4)
    print("\n")


def delete_Email(cur, login_ID):
    # select all the title,sender,and other tags into a matrix
    check_mail = "select title, sender, New_mail, Email_ID from Email_system where receiver = '{}'"
    User = cur.execute(get_User_Name.format(login_ID)).fetchone()
    receive_mail = cur.execute(check_mail.format(User[0])).fetchall()
    receive_mail_length = len(receive_mail)
    # if mailbox is empty
    if(receive_mail_length == 0):
        print("Whoops!!Your Email box is empty...How lonely you are?")
        print("loading", end='')
        for i in range(6):
            print(".", end='')
            time.sleep(0.4)
        print("\n")
        return
    # if mailbox is not empty
    print("==================================")
    print("You have ", receive_mail_length, "Emails.")
    print("Whick Email do you want to delete?")
    for i in range(len(receive_mail)):
        print(i+1, ")Tilte : ", receive_mail[i][0])
        print("   From : ", receive_mail[i][1])
        if (receive_mail[i][2] == 1):
            print("   New Email.")
            print("You should check out the content before delete it.")
        elif(receive_mail[i][2] == 0):
            print("   Old Email.")
    print("==================================")
    delete_num = int(input("Input a number :"))
    # check which email you wanna delete
    while(delete_num > receive_mail_length or delete_num <= 0):
        print("Error input")
        input_num = int(input("Input a Number :"))
    print("Email has been delete.")
   # delete the mail you select
    cur.execute("delete from Email_system where Email_ID = '{}'".format(
        receive_mail[delete_num-1][3]))
    print("loading", end='')
    for i in range(6):
        print(".", end='')
        time.sleep(0.4)
    print("\n")


def log_out(cur):
    pass
