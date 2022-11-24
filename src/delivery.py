# TODO FOURTH PRIORITY

# TODO FOLLOW THE RULE OF CRUD, CREATE/READ/UPDATE/DELETE

def createDelivery(orderId, user=""):
    orders = openDeliveryFile()
    highestId = 0
    for i in orders:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    deliveryString = "\n" + str(highestId) + ";" + "staff name" + str(highestId) + ";" + str(5) + ";" + str(5) + ";" + str(20)
    writeDeliveryFile(deliveryString)
    return main


def viewDelivery():
    # READ AND OPEN FILE OF DELIVERY
    deliveries = openDeliveryFile()
    # LIST IT OUT
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Delivery                          ")
    for delivery in deliveries:
        deliveries = str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str("," + delivery[3]) + str("," + delivery[4]) + "\n"
        print(deliveries)
    # ASK USER IF YOU WANT TO DO SUBSEQUENT ACTION, UPDATE DELIVERY MAN, UPDATE FEEDBACK ETC
    print("1. Add new delivery staff")
    print("2. Update delivery staff")
    print("3. Add delivery staff feedback")
    opt = input("Please enter your choice: ")
    if (opt == "1"):
        assignDeliveryStaff()
    elif (opt == "2"):
        createDeliveryFeedback()
    return viewDelivery


def assignDeliveryStaff(deliveryId, userId):
    # READ AND OPEN FILE OF DELIVERY
    delivery = openDeliveryFile()
    # READ AND OPEN FILE OF USER
    db = openUserFile()
    # LET THE USER KEY IN USERID
    flg = -1
    username = input("Enter your username:")
    password = input("Enter your Password:")
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
    # SEE IF THE USER EXIST IN THE FILE, IF NOT, THEN CALL THE USER TO KEY AGAIN OR QUIT
    # IF USER EXIST, UPDATE THE FILE
    return flg


def createDeliveryFeedback(deliveryId, feedback):
    # READ AND OPEN FILE OF DELIVERY
    deliveries = open("db/delivery.txt", "r")
    # FIND THE ROW OF DELIVERY INFO BASED ON THE DELIVERYID
    printString = ""
    count = 0
    for delivery in deliveryId:
            ind = input("Use Delivery ID to search.")
    if ind == delivery[0] :
        printString = (str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str("," + delivery[3]) + str("," + delivery[4]) + "\n")
    print(printString)
    # WRITE INTO THE FILE AND SAVE THE FILE
    writeFileDb = open("db/delivery.txt", "a")
    newfeedback = input(delivery[3] + "Please give a feedback, 1 - 5")
    writeFileDb.write(writeFile)
    return None


def openDeliveryFile():
    deliveries = []
    deliveryDb = db = open("db/delivery.txt", "r")
    for i in deliveryDb:
        deliveryId, orderId, paymentId, feedback, status = i.split(";")
        deliveries.append([deliveryId, orderId, paymentId, feedback, status])
    return deliveries

def writeDeliveryFile(writeFile):
    writeFileDb = open("db/delivery.txt", "a")
    writeFileDb.write(writeFile)
    return None


def writeDeliveryFileByReplace(writeDelivery, writeMode):
    writeFileDb = open("db/payment.txt", "w")
    # TODO writeMode = 1/2, 1 no need + \n
    writeString = ""
    count = 0
    for payment in writeDelivery:
        if (writeMode == 1):
            writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[4] + ";"
        elif (writeMode == 2):
            if (count == 0):
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[4] + "\n"
            else:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[4]
        count = count + 1
    writeFileDb.write(writeString)

def openUserFile():
    userDb = db = open("db/user.txt", "r")
    return userDb


# TODO MISC, put test function here to try
viewDelivery()