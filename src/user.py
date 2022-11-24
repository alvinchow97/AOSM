from menu import openUserFile

def checkUserRoleAndRedirect(username):
    userdb = openUserFile()
    #username is parameter of a function
    for user in userdb:
        open("user.txt")
    if(username == user[0]):
        if(user[2] == "admin"):
            adminMenu()
        elif(user[2] == "staff"):
            staffMenu()
        elif(user[2] == "customer"):
            customerMenu()

# TODO MISC put test function under here
