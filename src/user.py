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


