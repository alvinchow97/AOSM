from order import openOrderFile
from main import customerHome
from delivery import createDelivery


def createPayment(orderId, paymentAmount,user):
    payments = openPaymentFile()
    orders = openOrderFile()
    highestId = 0
    status = "incomplete"
    orderCost = 0
    for order in orders:
        if order[0] == str(orderId):
            orderCost = order[3]
    totalBalance = int(orderCost) - int(paymentAmount)
    if totalBalance == 0:
        status = "completed"
    for i in payments:
        if int(i[0]) > highestId:
            highestId = int(i[0])
    highestId = highestId + 1
    paymentString = "\n" + str(highestId) + ";" + str(orderId) + ";" + str(status) + ";" + str(user)
    writePaymentFile(paymentString)
    createDelivery(orderId,highestId,user)
    fakeAction = input("Payment and Delivery created successfully ! Press any Key to go back")
    customerHome()
    return


def viewPayment():
    # TODO Decorate
    payments = openPaymentFile()
    print("                               View Payment                      ")
    for payment in payments:
        payments = str(payment[0]) + str("," + payment[1]) + str("," + payment[2]) + str("," + payment[3]) + "\n"
        print(payments)
    return


def viewPaymentByPaymentId(paymentId):
    payments = openPaymentFile()
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                   Search Payment Details                   ")
    print(" PaymentId| OrderId| Status| UserId")
    for payment in payments:
        if payment[0] == str(paymentId):
            paymentString = str(payment[0] + "                    " + payment[1] + "                    " + payment[
                2] + "                    " + payment[3])
            print(paymentString)
        else:
            print("Payment ID not available")
    return


def deletePayment(paymentId):
    index = 0
    payments = openPaymentFile()
    for payment in payments:
        if payment[0] == str(1):
            payment.pop(index)
        index = index + 1
    writePaymentFileByReplace(payment, 1)
    return


def openPaymentFile():
    payments = []
    paymentDb = db = open("db/payment.txt", "r")
    for i in paymentDb:
        paymentId, orderId, status,userId = i.split(";")
        payments.append([paymentId, orderId, status,userId])
    return payments


def writePaymentFile(writeFile):
    writeFileDb = open("db/payment.txt", "a")
    writeFileDb.write(writeFile)
    return


def writePaymentFileByReplace(writePayment, writeMode):
    writeFileDb = open("db/payment.txt", "w")
    writeString = ""
    count = 0
    for payment in writePayment:
        if writeMode == 1:
            writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3]
        elif (writeMode == 2):
            if count == 0:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[3] + "\n"
            else:
                writeString += payment[0] + ";" + payment[1] + ";" + payment[2] + ";" + payment[2]
        count = count + 1
    writeFileDb.write(writeString)
    return
