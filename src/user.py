from menu import adminHome, staffMenu, customerHome


def checkUserRoleAndRedirect(role):
    if role == "admin":
        adminHome()
    elif role == "staff":
        staffMenu()
    elif role == "customer":
        customerHome()


def openUserFile():
    users = []
    userDb = db = open("db/user.txt", "r")
    for i in userDb:
        username, password, role = i.split(";")
        users.append([username.strip(), password.strip(), role.strip()])
    return users

def createUser(username, password):
    userDb = openUserFile()
    highestId = 0

    for i in userDb:
        if (int(i[0]) > highestId):
            highestId = int(i[0])

    highestId = highestId + 1
    userString = highestId + ";" + str(username) + ";" + str(password) + ";" + "customer"
    writeUserFile(userString)
    return

def writeUserFile(writeFile):
    writeFileDb = open("db/user.txt", "a")
    writeFileDb.write(writeFile)
    return

