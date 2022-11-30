from order import deleteOrder
def createDelivery(orderId, paymentId, user):
    deliveries = openDeliveryFile()
    highestId = 0
    for i in deliveries:
        if int(i[0]) > highestId:
            highestId = int(i[0])
    highestId = highestId + 1
    deliveryString = "\n" + str(highestId) + ";" + str(orderId) + ";" + str(
        paymentId) + ";" + "" + ";" + "NEW" + ";" + str(user)
    writeDeliveryFile(deliveryString)
    return


def viewDelivery():
    # TODO Decorate
    deliver11ies = openDeliveryFile()
    deliveryString = ""
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Delivery                          ")
    for delivery in deliveries:
        deliveryString += str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str(
            "," + delivery[3]) + str(
            "," + delivery[4]) + str("," + delivery[5]) + "\n"
        print(deliveryString)
    return


def viewDeliveryByUser(user):
    # TODO Decorate
    deliveries = openDeliveryFile()
    deliveryString = ""
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Delivery                          ")
    for delivery in deliveries:
        if delivery[5].strip() == user:
            deliveryString += str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str(
                "," + delivery[3]) + str(
                "," + delivery[4]) + str("," + delivery[5]) + "\n"
    print(deliveryString)
    return

def viewDeliveryByUnassigned():
    # TODO Decorate
    deliveries = openDeliveryFile()
    deliveryString = ""
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Delivery                          ")
    for delivery in deliveries:
        if delivery[5] == "":
            deliveryString += str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str(
                "," + delivery[3]) + str(
                "," + delivery[4]) + str("," + delivery[5]) + "\n"
    print(deliveryString)
    return


def updateDeliveryStatus(deliveryId, status):
    deleteOrderFlag = False
    orderIDRelated = 0
    if status == str(1):
        status = "Ongoing"
    elif status == str(2):
        status = "Pending"
    elif status == str(3):
        status = "Onhold"
    elif status == str(4):
        status = "Done"
        deleteOrderFlag = True
    else:
        status = "NEW"
    deliveries = openDeliveryFile()
    for delivery in deliveries:
        if delivery[0] == deliveryId:
            delivery[4] = status
            orderIDRelated = delivery[1]
    writeDeliveryFileByReplace(deliveries, 1)
    if deleteOrderFlag:
        deleteOrder(orderIDRelated)
        print("Order regarding to Delivery ID" + deliveryId + " is deleted")
    return


def searchDeliveryStaff():
    return


def assignDeliveryStaff(deliveryId, staffName):
    deliveryDb = openDeliveryFile()
    for delivery in deliveryDb:
        if delivery[0] == deliveryId:
            delivery[5] = str(staffName)
    writeDeliveryFileByReplace(deliveryDb, 1)
    return


def createDeliveryFeedback(deliveryId, feedback):
    deliveries = openDeliveryFile()
    for delivery in deliveries:
        if delivery[0] == deliveryId:
            delivery[3] = feedback
    writeDeliveryFileByReplace(deliveries, 1)
    return


def deleteDeliveryStaff():
    deliveries = open("db/delivery.txt", "r")
    index = 0
    # TODO replace the 1 with the orderId later
    for delivery in deliveries:
        if delivery[0] == str(1):
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
        if writeMode == 1:
            writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                4] + ";" + payment[5]
        elif (writeMode == 2):
            if count == 0:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                    4] + ";" + payment[5] + "\n"
            else:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + ";" + payment[
                    4] + ";" + payment[5]
        count = count + 1
    writeFileDb.write(writeString)
    writeFileDb.close()


def modifyDeliveryStaff():
    return
