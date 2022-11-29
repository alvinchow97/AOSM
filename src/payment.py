

def createPayment(orderId, paymentAmount):
    payments = openPaymentFile()
    highestId = 0

    for i in payments:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
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
    payments = openPaymentFile()
    print("                               View Payment                      ")
    for payment in payments:
        payments = str(payment[0]) + str("," + payment[1]) + str("," + payment[2]) + "\n"
        print(payments)
    return None


def viewPaymentByPaymentId(paymentId):
    payments = openPaymentFile()
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                   Search Payment Details                   ")
    for payment in payments:
        if(payment[0] == str(paymentId)):
            paymentString = payment[0] + " " + payment[1] + " " + payment[2]
            print(paymentString)
        else:
            print("Payment ID not available")
    return


def deletePayment(paymentId):
    index = 0
    payments = openPaymentFile()
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