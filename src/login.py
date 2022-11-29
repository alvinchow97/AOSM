from user import checkUserRoleAndRedirect, openUserFile

def register():
    db = openUserFile()
    username = input("Create username:")
    password = input("Create Password:")
    password1 = input("Confirm Password:")
    d = []
    f = []
    for i in db:
        a, b, c = i.split(";")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    if password != password1:
        print("Password don't match!")
        register()
    else:
        if username in d:
            print("Username already exist")
            register()
        else:
            db = open("database.txt", "a")
            db.write(username + ", " + password + "\n")
            print("Successfully added new user!")


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


