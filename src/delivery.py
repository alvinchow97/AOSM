# TODO FOURTH PRIORITY

# TODO FOLLOW THE RULE OF CRUD, CREATE/READ/UPDATE/DELETE

def createDelivery(orderId, user=""):
    orders = openDeliveryFile()
    highestId = 0
    for i in orders:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    deliveryString = "\n" + str(highestId) + ";" + "empty item description" + ";" + str(5) + ";" + str(5) + ";" + str(20)
    writeDeliveryFile(deliveryString)
    return None


def viewDelivery():
    # READ AND OPEN FILE OF DELIVERY
    # LIST IT OUT
    # ASK USER IF YOU WANT TO DO SUBSEQUENT ACTION, UPDATE DELIVERY MAN, UPDATE FEEDBACK ETC
    return None


def assignDeliveryStaff(deliveryId, userId):
    # READ AND OPEN FILE OF DELIVERY
    # READ AND OPEN FILE OF USER
    # LET THE USER KEY IN USERID
    # SEE IF THE USER EXIST IN THE FILE, IF NOT, THEN CALL THE USER TO KEY AGAIN OR QUIT
    # IF USER EXIST, UPDATE THE FILE
    return None


def createDeliveryFeedback(deliveryId, feedback):
    # READ AND OPEN FILE OF DELIVERY
    # FIND THE ROW OF DELIVERY INFO BASED ON THE DELIVERYID
    # WRITE INTO THE FILE AND SAVE THE FILE
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
