from user import checkUserRoleAndRedirect, openUserFile, createUser, writeUserFileByReplace

from main import home
import os

def register():
    # TODO Decorate
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
        return
    createUser(username, password)
    os.system('cls')
    print("User created successfully... Returning to login page")
    home()
    return


def access():
    # TODO Decorate
    userDb = openUserFile()
    username = input("Enter username:")
    password = input("Enter Password:")
    print("\n Enter 0 in both field to quit the program.")
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
