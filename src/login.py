from user import checkUserRoleAndRedirect, openUserFile
from main import home
import main
def register():
    userdb = openUserFile()
    username = input("Create username:")
    password = input("Create Password:")
    password1 = input("Confirm Password:")
    print("\n Enter 0 in both field to quit the program.")

    for user in userdb:
            if password != password1:
                print("Password don't match!")
                register()
            else:
                userdb = open("user.txt", "a")
                userdb.write(username + ". "+ password + "\n")
                print("successfully added new user!")



def access():
    userDb = openUserFile()
    username = input("Enter username:")
    password = input("Enter Password:")
    print("\n Enter 0 in both field to quit the program.")

    for user in userDb:
        if (username == str(user[0]) and password == str(user[1])):
            print("Login success")
            print("Hi, ", str(user[2]))
            checkUserRoleAndRedirect(user[2])
        elif username == str(0) and password == str(0):
            exit()
        else:
            return
            # will import home but circular dependency


