# TODO SECOND PRIORITY
# TODO Redefine {orderId,quantity, itemId, itemPrice, orderTotalPrice, user} to {orderId,quantity, itemId, orderTotalPrice, user}
# FOLLOW RULES OF CRUD, CREATE/READ/UPDATE/DELETE
from item import openItemFile, updateItemStockQuantity, writeItemFileByReplace


def createOrder(order):
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
    # FINAL STEP, CALL ITEM updateStockQuantityByReduce to reduce the stock quantity
    updateItemStockQuantity(1, 3)
    return None


def deleteOrder(orderId):
    index = 0
    orders = openOrderFile()
    # TODO replace the 1 with the orderId later
    for order in orders:
        if (order[0] == str(1)):
            orders.pop(index)
        index = index + 1
    writeOrderFileByReplace(orders, 1)
    return None


def editOrderByQuantity(orderId, newQuantity):
    orders = openOrderFile()
    items = openItemFile()
    # TODO replace 1 with orderId, and 2 with newQuantity (4 places)
    for order in orders:
        if (order[0] == str(1)):
            for item in items:
                if (item[0] == order[1]):
                    # update the orderTotalPrice
                    order[3] = str(int(2) * int(item[2]))
                    # update the stock quantity determine by the orderQuantity edited
                    if(int(2) > int(order[2])):
                        item[4] = str(int(item[4]) + -(int(2) - int(order[2])))
                    else:
                        item[4] = str(int(item[4]) + int(order[2]) - int(4))
            # now only update the quantity, if put before update item stock will patch the quantity
            order[2] = str(2)
    writeOrderFileByReplace(orders, 1)
    writeItemFileByReplace(items, 1)
    # UPDATE THE QUANTITY AND TOTAL PRICE (itemUnitPrice x quantity)
    # UPDATE THE ITEM STOCK QUANTITY DETERMINED BY THE SCENARIO
    return None


def viewOrder():
    # OPEN AND READ ORDER.TXT
    orders = openOrderFile()
    # DESIGN UI INTERFACE, LOOP INTERFACE USING FOR LOOP
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     View Order                         ")
    for order in orders:
        print += order[0] + " " + order[1]  + " " + order[2] + " " + order[3] + " " + order[4] + " " + order[5] + "\n"
    # IF PRESS BACK, THEN BACK TO PARENT MENU
    return None


def viewOrderByOrderId(orderId):
    # OPEN AND READ ORDER.TXT
    # DESIGN UI INTERFACE
    # FIND THE ROW OF DATA USING ORDERID
    # IF PRESS BACK, THEN BACK TO PARENT MENU
    return None


# TODO MISC
# SEE IF GOT ANY MISC FUNCTION, PUT HERE
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
    # TODO writeMode = 1/2, 1 no need + \n
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

# TODO MISC put test function under here
deleteOrder([])