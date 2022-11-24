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
    payments = openPaymentFile()
    paymentLocated = []

    for i in payments:
        if (i[0] == str(1)):
            paymentLocated = i
    paymentByOrderId = paymentLocated[2]
    paymentString = "\n" + str(highestId) + ";" + str(1) + ";" + str(1) + ";" + str(
        paymentByOrderId * 1) + ";" + "NEW" + ";" + str(1)
    writePaymentFile(paymentString)
    return None


def viewPayment():
    # OPEN FILE AND READ FILE OF PAYMENT
    payments = openPaymentFile()
    # LIST IT OUT
    print("                               View Payment                      ")
    for payment in payments:
        payments = str(payment[0]) + str("," + payment[1]) + str("," + payment[2]) + str("," + payment[3]) + "\n"
        print(payments)
    return None


def viewPaymentByPaymentId():
    #OPEN FILE AND READ FILE OF PAYMENT
    payments = openPaymentFile()
    # DESIGN UI INTERFACE
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                   This is Payment List                       ")

    # FIND THE ROW OF DATA USING ORDERID
    for payment in payments:
        payment[1] = PaymentByPaymentId
        PaymentByPaymentId = int(payment[1]) + str(";" + payment[2]) + "\n"
        print(PaymentByPaymentId)
    # IF PRESS BACK, THEN BACK TO PARENT MENU
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


# TODO MISC put test function under here
viewPayment()