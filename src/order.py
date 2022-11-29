from item import openItemFile, updateItemStockQuantity, writeItemFileByReplace


def createOrder(itemId, quantity):
    orders = openOrderFile()
    highestId = 0

    for i in orders:
        if (int(i[0]) > highestId):
            highestId = int(i[0])

    highestId = highestId + 1

    items = openItemFile()
    itemLocated = []
    # TODO replace the 1 with item id later
    for i in items:
        if (i[0] == str(1)):
            itemLocated = i
    unitPriceByItemId = itemLocated[2]
    orderString = "\n" + str(highestId) + ";" + str(1) + ";" + str(1) + ";" + str(
        unitPriceByItemId * 1) + ";" + "NEW" + ";" + str(1)
    writeOrderFile(orderString)
    updateItemStockQuantity(1, 3)
    return None


def deleteOrder(orderId):
    index = 0
    orders = openOrderFile()
    for order in orders:
        if (order[0] == str(1)):
            orders.pop(index)
        index = index + 1
    writeOrderFileByReplace(orders, 1)
    return None


def editOrderByQuantity(orderId, newQuantity):
    orders = openOrderFile()
    items = openItemFile()
    for order in orders:
        if (order[0] == str(1)):
            for item in items:
                if (item[0] == order[1]):
                    order[3] = str(int(2) * int(item[2]))
                    if(int(2) > int(order[2])):
                        item[4] = str(int(item[4]) + -(int(2) - int(order[2])))
                    else:
                        item[4] = str(int(item[4]) + int(order[2]) - int(4))
            order[2] = str(2)
    writeOrderFileByReplace(orders, 1)
    writeItemFileByReplace(items, 1)
    return None


def viewOrder():
    orders = openOrderFile()
    orderString = ""
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Order                         ")
    for order in orders:
        orderString += order[0] + " " + order[1]  + " " + order[2] + " " + order[3] + " " + order[4] + " " + order[5] + "\n" #customer order
    print(orderString)
    return None


def viewOrderByOrderId(orderId):
    orders = openOrderFile()
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                   Search Order Details                       ")
    for order in orders:
        if(order[0] == str(orderId)):
            orderString = order[0] + " " + order[1] + " " + order[2] + " " + order[3] + " " + order[4] + " " + order[5]
            print(orderString)
        else:
            print("Order ID not available")
    return


def openOrderFile():
    orders = []
    orderDb = db = open("db/order.txt", "r")
    for i in orderDb:
        orderId, itemId, quantity, orderTotalPrice, status, user = i.split(";")
        orders.append([orderId, itemId, quantity, orderTotalPrice, status, user])
    return orders


def writeOrderFile(writeFile):
    writeFileDb = open("db/order.txt", "a")
    writeFileDb.write(writeFile)
    return None


def writeOrderFileByReplace(writeOrder, writeMode):
    writeFileDb = open("db/order.txt", "w")
    writeString = ""
    count = 0
    for order in writeOrder:
        if (writeMode == 1):
            writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + order[5]
        elif (writeMode == 2):
            if (count == 0):
                writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + \
                               order[5] + "\n"
            else:
                writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + \
                               order[5]
        count = count + 1
    writeFileDb.write(writeString)

