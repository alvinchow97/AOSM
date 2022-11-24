def Register():
    username = input("Please enter your ID: ")
    password = input("Please enter your Password: ")
    userType = input("Please enter User Type:")
    while True:
        UserType = input("Please enter user type (admin,staff,customer): ")
        if (userType =="admin" or userType =="staff" or userType =="customer"):
            break
    with open("user.txt","a") as fh:
        rec = username+","+password+","+customer+"\n"
        fh.write(rec)
