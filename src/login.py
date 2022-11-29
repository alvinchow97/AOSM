from user import checkUserRoleAndRedirect, openUserFile, createUser

def register():
    userDb = openUserFile()
    username = input("Create username:")
    password = input("Create Password:")
    password1 = input("Confirm Password:")
    if password != password1:
        return
    for user in userDb:
        if(user[1] == username):
            print("Username exist")
            return
    createUser(username,password)
    return


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
            access()


