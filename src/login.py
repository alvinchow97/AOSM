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
    db = openUserFile()
    username = input("Enter username:")
    password = input("Enter Password:")

    if not len(username or password) < 1:
        d = []
        f = []
        for i in db:
            a, b, c = i.split(";")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[username]:
                try:
                    if password == data[username]:
                        print("Login success")
                        print("Hi, ", username)
                    else:
                        print("Invalid username or password")
                except:
                    print("Incorrect password or username")
            else:
                print("Username doesn't exist")
        except:
            print("Login error")
    else:
        print("Please enter a value")

def openUserFile():
    userDb = db = open("db/user.txt", "r")
    return userDb
def home(option=None):
    option = input("Login | Signup:")
    if option == "Login":
        access()
    elif option == "Signup":
        register()
    else:
        print("Invalid option!")

# TODO MISC put test function under here
