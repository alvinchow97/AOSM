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
    userString = str(username) + ";" + str(password) + ";" + "customer"
    writeUserFile(userString)
    return

def createDeliveryStaff(username):
    userString = "\n" + str(username) + ";" + str(1234) + ";" + "staff"
    writeUserFile(userString)
    return

def viewDeliveryStaff():
    userDb = openUserFile()
    for user in userDb:
        if(user[2] == "staff"):
            staffString = user[0] + " " + user[1] + " " + user[2]
            print(staffString)
    return

def deleteUser(deleteUserName):
    index = 0
    users = openUserFile()
    for user in users:
        if (user[0] == str(deleteUserName)):
            users.pop(index)
        index = index + 1
    writeUserFileByReplace(users,2)
    return None
def writeUserFile(writeFile):
    writeFileDb = open("db/user.txt", "a")
    writeFileDb.write(writeFile)
    return

def writeUserFileByReplace(users, writeMode):
    writeFileDb = open("db/user.txt", "w")
    writeString = ""
    count = 0
    for user in users:
        if (writeMode == 1):
            writeString += user[0] + ";" + user[1] + ";" + user[2]
        elif (writeMode == 2):
            if (count == 0):
                writeString += user[0] + ";" + user[1] + ";" + user[2] + "\n"
            else:
                writeString += user[0] + ";" + user[1] + ";" + user[2] + "\n"
        count = count + 1
    writeFileDb.write(writeString)

