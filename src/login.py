from user import checkUserRoleAndRedirect, openUserFile, createUser, writeUserFileByReplace

from main import home
import os

def register():

    userDb = openUserFile()
    username = input("Create username:")
    for user in userDb:
        if user[0] == username:
            os.system('cls')
            print("Username exist")
            register()
            return
    password = input("Create Password:")
    password1 = input("Confirm Password:")
    if password != password1:
        print("Password not match, please try again")
        register()
        return
    createUser(username, password)
    os.system('cls')
    print("User created successfully... Returning to login page")
    home()
    return


def access():

    userDb = openUserFile()
    print("\nEnter 0 in both field to quit the program.")
    username = input("Enter username:")
    password = input("Enter Password:")
    trueFindFlag = False
    for user in userDb:
        if username == str(user[0]) and password == str(user[1]):
            print("Login success")
            print("Hi, ", str(user[2]))
            trueFindFlag = True
            checkUserRoleAndRedirect(user[0], user[2])
        elif username == str(0) and password == str(0):
            exit()
    if not trueFindFlag:
        print("Invalid username")
        access()
    return
