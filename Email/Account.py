import sqlite3


def login(cur):
    # check if account is existed
    check_user_exist = "select * from Registrants where account='{}'"
    # ckeck if account match password
    check_user_sql = "select * from Registrants where account='{0}' and password='{1}'"
    # take out the account name
    get_account_name = "select Name from Registrants where account = '{}'"
    get_account_ID = "select ID from Registrants where account = '{}'"
    account = input('請輸入帳號 :')
    if(account == "End"):
        exit()
    password = input('請輸入密碼 :')
    existed = cur.execute(check_user_exist.format(account)).fetchone()
    corrcet = cur.execute(check_user_sql.format(account, password)).fetchone()

    if(existed == None):
        print("此帳號不存在")
        answer = input("要創建帳號嗎? Y/N \n")
        if(answer == 'Y'):
            create_account(cur)
        elif(answer == 'N'):
            return 0
        else:
            print("輸入錯誤，請重新嘗試")
        return 0
    elif(corrcet == None):
        print("錯誤的帳號或密碼")
        return 0
    elif(existed != None and corrcet != None):
        name = cur.execute(get_account_name.format(account)).fetchone()
        ID = cur.execute(get_account_ID.format(account)).fetchone()
        print("Welcome back", name[0])
        return ID[0]


def create_account(cur):
    check_if_account_existed = "select Account from Registrants where Account = '{}'"
    reg_success = False
    while(not reg_success):
        name = input("請輸入您的名字 :")
        account = input("請輸入您的帳號 :")
        check = cur.execute(
            check_if_account_existed.format(account)).fetchone()
        if(check == None):
            print("您可以使用這個帳號:)")
            cur.execute(
                "insert into Registrants(Name, Account, Password) values ('{}','{}', 'tmp')".format(name, account))
        else:
            print("此帳號已經註冊，請使用別的帳號")
            continue
        Password = input("請輸入您的密碼 :")
        cur.execute(
            "update Registrants set Password ='{1}' where Account = '{0}'".format(account, Password))
        reg_success = True
