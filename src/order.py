# TODO SECOND PRIORITY
# TODO Redefine {orderId,quantity, itemId, itemPrice, orderTotalPrice, user} to {orderId,quantity, itemId, orderTotalPrice, user}
# FOLLOW RULES OF CRUD, CREATE/READ/UPDATE/DELETE
from item import openItemFile,updateItemStockQuantity
def createOrder(order):
    # CREATE NEW FUNCTION UNDER ITEM READ TO FIND ITEM PRICE BY QUANTITY
    # OPEN ORDER.TXT
    # FIND THE LATEST ORDER ID, ON TOP OF THAT, +1 TO THE ID

    orders = openOrderFile()
    highestId = 0

    for i in orders:
        if (int(i[0]) > highestId):
            highestId = int(i[0])

    highestId = highestId + 1

    items = openItemFile()
    itemLocated = []
    # replace the 1 with item id later
    for i in items:
        if(i[0] == str(1)):
            itemLocated = i
    # OPEN ITEM FILE AND READ THE FILE TO FIND UNIT PRICE BY ITEM ID
    unitPriceByItemId = itemLocated[2]
    # MAKE A LIST OF ORDER TO APPEND
    orderString = "\n" + str(highestId) + ";" + str(1) + ";" + str(1) + ";" + str(unitPriceByItemId * 1) + ";" + "NEW" + ";" + str(1)
    writeOrderFile(orderString)
    # WRITE INTO ORDER.TXT

    # FINAL STEP, CALL ITEM updateStockQuantityByReduce to reduce the stock quantity
    updateItemStockQuantity(1, 3)
    # RETURN TRUE IF DONE, FALSE IF FAILED
    return None


def deleteOrder(orderId):
    # OPEN AND READ order.txt
    # FIND THE ROW OF DATA BASED ON ORDERID
    # REMOVE THE ROW OF DATA FROM THE ARRAY
    # WRITE IN BACK TO THE FILE

    # CREATE NEW FUNCTION UNDER ITEM TO UPDATE BACK THE QUANTITY
    # CREATE A VARIABLE EARLIER TO HOLD THE QUANTITY
    # EXECUTE THE FUNCTION WITH PARAMETER ITEMID, QUANTITY
    return None


def editOrderByQuantity(orderId, newQuantity):
    # OPEN AND READ ORDER.TXT
    # FIND THE ROW OF DATA USING ORDERID
    # UPDATE THE QUANTITY AND TOTAL PRICE (itemUnitPrice x quantity)

    # WRITE BACK INTO THE FILE
    # RETURN TRUE IF DONE, FALSE IF FAIL
    return None


def viewOrder():
    # OPEN AND READ ORDER.TXT
    # DESIGN UI INTERFACE, LOOP INTERFACE USING FOR LOOP
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
    # DO THE OPEN FILE READ FILE ACTION HERE
    orders = []
    orderDb = db = open("db/order.txt", "r")
    for i in orderDb:
        orderId, itemId, quantity, orderTotalPrice, status, user = i.split(";")
        orders.append([orderId, itemId, quantity, orderTotalPrice, status, user])
    # THEN REPLACE THE COMMENT ABOVE
    # RETURN WHAT INSIDE THE FILE
    return orders

def writeOrderFile(writeFile):
    writeFileDb = open("db/order.txt", "a")
    writeFileDb.write(writeFile)
    # FIND THE FILE, READ THE FILE
    # WRITE THE FILE
    # RETURN TRUE IF GOOD, FALSE IF FAILED
    return None

createOrder([])