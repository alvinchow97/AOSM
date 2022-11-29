
def createDelivery(orderId,paymentId,user):
    deliveries = openDeliveryFile()
    highestId = 0
    for i in deliveries:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    deliveryString = "\n" + str(highestId) + ";" + str(orderId) + ";" + str(paymentId) + ";" + "" + ";" + str(user)
    writeDeliveryFile(deliveryString)
    return


def viewDelivery():
    deliveries = openDeliveryFile()
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Delivery                          ")
    for delivery in deliveries:
        deliveries = str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str("," + delivery[3]) + str(
            "," + delivery[4]) + str("," + delivery[5]) + "\n"
        print(deliveries)
    return


def searchDeliveryStaff():
    return


def assignDeliveryStaff(deliveryId, staffName):
    deliveryDb = openDeliveryFile()
    for delivery in deliveryDb:
        if (delivery[0] == deliveryId):
            delivery[5] = str(staffName)
    writeDeliveryFileByReplace(deliveryDb, 1)
    return


def createDeliveryFeedback(deliveryId, feedback):
    # READ AND OPEN FILE OF DELIVERY
    deliveries = open("db/delivery.txt", "r")
    # FIND THE ROW OF DELIVERY INFO BASED ON THE DELIVERYID
    printString = ""
    count = 0
    for delivery in deliveryId:
        ind = input("Use Delivery ID to search.")
    if ind == delivery[0]:
        printString = (
                    str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str("," + delivery[3]) + str(
                "," + delivery[4]) + "\n")
    print(printString)
    # WRITE INTO THE FILE AND SAVE THE FILE
    writeFileDb = open("db/delivery.txt", "a")
    newfeedback = input(delivery[3] + "Please give a feedback, 1 - 5")
    writeFileDb.write(printString)
    return None


def deleteDeliveryStaff():
    deliveries = open("db/delivery.txt", "r")
    index = 0
    # TODO replace the 1 with the orderId later
    for delivery in deliveries:
        if (delivery[0] == str(1)):
            delivery.pop(index)
        index = index + 1
    writeDeliveryFileByReplace(deliveries, 1)
    return deleteDeliveryStaff()


def openDeliveryFile():
    deliveries = []
    deliveryDb = db = open("db/delivery.txt", "r")
    for i in deliveryDb:
        deliveryId, orderId, paymentId, feedback, status, userId = i.split(";")
        deliveries.append([deliveryId, orderId, paymentId, feedback, status, userId])
    return deliveries


def writeDeliveryFile(writeFile):
    writeFileDb = open("db/delivery.txt", "a")
    writeFileDb.write(writeFile)
    return None


def writeDeliveryFileByReplace(writeDelivery, writeMode):
    writeFileDb = open("db/delivery.txt", "w")
    writeString = ""
    count = 0
    for payment in writeDelivery:
        if (writeMode == 1):
            writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                4] + ";" + payment[5]
        elif (writeMode == 2):
            if (count == 0):
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                    4] + ";" + payment[5] + "\n"
            else:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                    4] + ";" + payment[5]
        count = count + 1
    writeFileDb.write(writeString)


def modifyDeliveryStaff():
    return
