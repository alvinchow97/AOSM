from menu import adminMenu, staffMenu, customerMenu



def checkUserRoleAndRedirect(role):
    if role == "admin":
        adminMenu()
    elif role == "staff":
        staffMenu()
    elif role == "customer":
        customerMenu()


def openUserFile():
    # DO THE OPEN FILE READ FILE ACTION HERE
    users = []
    userDb = db = open("db/user.txt", "r")
    for i in userDb:
        username, password, role = i.split(";")
        users.append([username.strip(), password.strip(), role.strip()])
    # THEN REPLACE THE COMMENT ABOVE
    # RETURN WHAT INSIDE THE FILE
    return openUserFile()


