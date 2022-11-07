# TODO THIRD PRIORITY
# TODO Redefine {orderId,quantity, itemId, itemPrice, orderTotalPrice,status, user} to {orderId,quantity, itemId, orderTotalPrice, user}
# FOLLOW RULES OF CRUD, CREATE/READ/UPDATE/DELETE

def createPayment(orderId):
    payments = openPaymentFile()
    highestId = 0
    for i in payments:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    # TODO payment string below need redefine
    paymentString = "\n" + str(highestId) + ";" + "empty item description" + ";" + str(5) + ";" + str(5) + ";" + str(20)
    writePaymentFile(paymentString)
    return None


def viewPayment():
    # OPEN FILE AND READ FILE OF PAYMENT
    # LIST IT OUT
    return None


def deletePayment(paymentId):
    index = 0
    payments = openPaymentFile()
    # TODO replace the 1 with the orderId later
    for payment in payments:
        if (payment[0] == str(1)):
            payment.pop(index)
        index = index + 1
    writePaymentFileByReplace(payment, 1)
    return None


def openPaymentFile():
    payments = []
    paymentDb = db = open("db/payment.txt", "r")
    for i in paymentDb:
        paymentId, orderId, status = i.split(";")
        payments.append([paymentId, orderId, status])
    return payments


def writePaymentFile(writeFile):
    writeFileDb = open("db/payment.txt", "a")
    writeFileDb.write(writeFile)
    return None


def writePaymentFileByReplace(writePayment, writeMode):
    writeFileDb = open("db/payment.txt", "w")
    # TODO writeMode = 1/2, 1 no need + \n
    writeString = ""
    count = 0
    for payment in writePayment:
        if (writeMode == 1):
            writeString += payment[0] + ";" + payment[1] + ";" + payment[2]
        elif (writeMode == 2):
            if (count == 0):
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + "\n"
            else:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2]
        count = count + 1
    writeFileDb.write(writeString)


