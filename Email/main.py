import Account as account
import sqlite3
import Email_system as ES

end = False


def GUI(cur, login_ID):
    global end

    while(True):
        print("   ▄███████▄    ▄████████    ▄█   ▄█▄  ▄██████▄  ")
        print("  ███    ███   ███    ███   ███ ▄███▀ ███    ███")
        print("  ███    ███   ███    █▀    ███▐██▀   ███    ███ ")
        print("  ███    ███  ▄███▄▄▄      ▄█████▀    ███    ███ ")
        print("▀█████████▀  ▀▀███▀▀▀     ▀▀█████▄    ███    ███ ")
        print("  ███          ███    █▄    ███▐██▄   ███    ███")
        print("  ███          ███    ███   ███ ▀███▄ ███    ███")
        print(" ▄████▀        ██████████   ███   ▀█▀  ▀██████▀ ")
        print("\n")
        print("Welcome back to Peko_Mail")
        print("What do you want to do today?")
        print("==================================")
        print("Press 【1】 to send a PekoEmail")
        print("Press 【2】 to check previous PekoMails")
        print("Press 【3】 to check the new PekoEmails")
        print("Press 【4】 to delete PekoEmails")
        print("Press 【5】 to log out")
        print("Press 【6】 to exit")
        print("==================================")
        number = input()
        if number == '1':
            ES.sendmail(cur, login_ID)
            conn.commit()
        elif number == '2':
            ES.check_pre_mail(cur, login_ID)
        elif number == '3':
            ES.check_new_mail(cur, login_ID)
            conn.commit()
        elif number == '4':
            ES.delete_Email(cur, login_ID)
            conn.commit()
        elif number == '5':

            return 0
        elif number == '6':
            end = True
            return 0
        else:
            print("Input Error...Please input again")


if __name__ == '__main__':
    conn = sqlite3.connect('C:\\Users\\User\\Desktop\\python\\登入系統.db')
    cur = conn.cursor()
    login_ID = 0
    # end the progress
    while(not end):
        # log_in
        while(not login_ID):
            login_ID = account.login(cur)
        login_ID = GUI(cur, login_ID)

    conn.commit()
    conn.close()
