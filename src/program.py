import os
from datetime import datetime


def showCurrentTime():
    os.system('cls')
    print("Current Time =", datetime.now().strftime("%H:%M:%S"))

# Single File

# Context of item.py

def createItem(itemDescription, itemUnitPrice, itemCategory, itemStockQuantity):
    items = openItemFile()
    highestId = 0
    for i in items:
        if int(i[0]) > highestId:
            highestId = int(i[0])

    highestId = highestId + 1
    itemString = "\n" + str(highestId) + ";" + str(itemDescription) + ";" + str(itemUnitPrice) + ";" + str(itemCategory) + ";" + str(itemStockQuantity)
    writeItemFile(itemString)
    return None


def createCategory(category):
    categoryDb = openCategoryFile()
    highestId = 0
    for i in categoryDb:
        if int(i[0]) >= highestId:
            highestId = int(i[0])
    highestId = highestId + 1
    categoryString = "\n" +  str(highestId) + ";" + str(category)
    writeCategoryFile(categoryString)
    return


def viewItem():
    items = openItemFile()
    printString = ""
    print("                    View Items Records                          ")
    print("================================================================")
    print(" ItemID| ItemDescription| ItemUnitPrice| Category| StockQuantity")
    for item in items:
        printString +="   " + str(item[0] + "     " + item[1]) + "      " + item[2] + "            " + item[3] + "           " + item[4] + "      " + "\n"
    os.system('cls')
    print(printString)
    return


def viewCategory():
    # TODO Decorate
    categories = openCategoryFile()
    printString = ""
    print("================================================================")
    print("     Category ID                  Category Name                  ")
    for category in categories:
        printString += "        " + (str(category[0] + "                             " + category[1]) + "\n")
    os.system('cls')
    print(printString)
    return


def viewItemByCategory(categoryId):
    # TODO Decorate
    itemDb = openItemFile()
    print("================================================================")
    for item in itemDb:
        if item[3] == categoryId:
            categoryString = "     " + str(item[1]) + "      " + str(item[2]) + "      " + str(item[3]) + "      " + str(item[4]) + "      "
            os.system('cls')
            print(categoryString)
    return


def updateItemUnitPrice(itemId, updatedUnitPrice):
    items = openItemFile()
    for item in items:
        if item[0] == str(itemId):
            item[2] = str(updatedUnitPrice)  # update itemUnitPrice happen here
    writeItemFileByReplace(items, 1)
    return


def updateItemStockQuantity(itemId, stockQuantity):
    items = openItemFile()
    for item in items:
        if item[0] == str(itemId):
            item[4] = str( int(item[4].strip()) - int(stockQuantity) )
    writeItemFileByReplace(items, 2)
    return


def updateItemStockQuantityByReduce(itemId, reduceNo):
    items = openItemFile()
    for item in items:
        if item[0] == str(itemId):
            item[4] = str(int(int(item[4]) - int(reduceNo)))

    writeItemFileByReplace(items, 2)
    return


def updateItemCategory(itemId, newCategory):
    items = openItemFile()
    for item in items:
        if item[0] == str(itemId):
            item[3] = str(newCategory)
    writeItemFileByReplace(items, 1)
    return


def updateItemDescription(itemId, newDescription):

    items = openItemFile()
    for item in items:
        if item[0] == str(itemId):
            item[1] = str(newDescription)  # update stockQuantity happen here (reduce by 2)
    writeItemFileByReplace(items, 1)
    return


def deleteItem(itemId):
    index = 0
    items = openItemFile()

    for item in items:
        if item[0] == str(1):
            items.pop(index)
        index = index + 1
    writeItemFileByReplace(items, 1)
    return


def deleteCategory(categoryId):
    categories = openCategoryFile()
    items = openItemFile()

    replacedItems = items.copy()
    replacedCategories = categories.copy()

    itemIndex = 0
    categoryIndex = 0
    for category in categories:
        if category[0] == str(categoryId):
            for item in items:
                if item[3] == str(categoryId):
                    if len(replacedItems) == len(items):
                        replacedItems.pop(itemIndex)
                    else:
                        replacedItems.pop(itemIndex - 1)
                itemIndex = itemIndex + 1
            writeItemFileByReplace(replacedItems, 1)

            if len(replacedCategories) == len(categories):
                categories.pop(categoryIndex)
            else:
                categories.pop(categoryIndex - 1)
        categoryIndex = categoryIndex + 1
    writeCategoryFileByReplace(categories, 1)
    return




def itemMenu():
    # DO ANY MENU ACTION HERE, USING SWITCH CASE
    return


def openItemFile():
    items = []
    itemDb = db = open("db/item.txt", "r")
    for i in itemDb:
        itemId, itemDescription, itemUnitPrice, categoryId, stockQuantity = i.split(";")
        items.append([itemId, itemDescription, itemUnitPrice, categoryId, stockQuantity])
    return items


def openCategoryFile():
    categories = []
    categoryDb = db = open("db/category.txt", "r")
    for i in categoryDb:
        categoryId, categoryName = i.split(";")
        categories.append([categoryId, categoryName])
    return categories


def writeItemFile(writeFile):
    writeFileDb = open("db/item.txt", "a")
    writeFileDb.write(writeFile)
    return


def writeItemFileByReplace(writeItem, writeMode):
    # TODO writeMode = 1/2, 1 no need + \n
    writeString = ""
    count = 0
    for item in writeItem:
        if writeMode == 1:
            writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]
        elif (writeMode == 2):
            if count == 0:
                writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4] + "\n"
            else:
                writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]
        count = count + 1
    writeFileDb = open("db/item.txt", "w")
    writeFileDb.write(writeString)
    return


def writeCategoryFileByReplace(writeCategory, writeMode):
    writeString = ""
    count = 0
    for item in writeCategory:
        if writeMode == 1:
            writeString += item[0] + ";" + item[1]
        elif (writeMode == 2):
            if count == 0:
                writeString += item[0] + ";" + item[1] + "\n"
            else:
                writeString += item[0] + ";" + item[1]
        count = count + 1
    writeFileDb = open("db/category.txt", "w")
    writeFileDb.write(writeString)
    return


def writeCategoryFile(writeCategory):
    writeFileDb = open("db/category.txt", "a")
    writeFileDb.write(writeCategory)
    return

# End of item.py

# Context of delivery.py

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
    deliveries = openDeliveryFile()
    deliveryString = ""
    print("================================================================")
    print("                  View Delivery Records                         ")
    print("deliveryId | orderId | paymentId | feedback  |  status  | userId")
    for delivery in deliveries:
        deliveryString += str(delivery[0]) + str("," + delivery[1]) + str("," + delivery[2]) + str(
            "," + delivery[3]) + str(
            "," + delivery[4]) + str("," + delivery[5]) + "\n"
        os.system('cls')
        print(deliveryString)
    return


def viewDeliveryByUser(user):
    # TODO Decorate
    deliveries = openDeliveryFile()
    deliveryString = ""
    print("================================================================")
    print("                  View Delivery Records                         ")
    print("deliveryId | orderId | paymentId | feedback  |  status  | userId")
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
            if (count == 0):
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

# End of delivery.py

# Context of common.py



# End of common.py

# Context of login.py

def register():
    # TODO Decorate
    userDb = openUserFile()
    username = input("Create username:")
    for user in userDb:
        if user[0] == username:
            os.system('cls')
            print("Username exist")
            register()
            return
    password = input("Create Password:")
    password1 = input("Confirm Password:")
    if password != password1:
        return
    createUser(username, password)
    os.system('cls')
    print("User created successfully... Returning to login page")
    home()
    return


def access():
    # TODO Decorate
    userDb = openUserFile()
    username = input("Enter username:")
    password = input("Enter Password:")
    print("\n Enter 0 in both field to quit the program.")
    trueFindFlag = False
    for user in userDb:
        if username == str(user[0]) and password == str(user[1]):
            print("Login success")
            print("Hi, ", str(user[2]))
            trueFindFlag = True
            checkUserRoleAndRedirect(user[0], user[2])
        elif username == str(0) and password == str(0):
            exit()
    if not trueFindFlag:
        print("Invalid username")
        access()
    return

# End of login.py

# Context of order.py

def createOrder(itemId, quantity,username):
    orders = openOrderFile()
    highestId = 0

    for i in orders:
        if int(i[0]) > highestId:
            highestId = int(i[0])

    highestId = highestId + 1

    items = openItemFile()
    itemLocated = []
    unitPriceByItemId = 0

    for i in items:
        if i[0] == str(itemId):
            unitPriceByItemId = i[2]
    orderString = "\n" + str(highestId) + ";" + str(itemId) + ";" + str(quantity) + ";" + str(
        int(unitPriceByItemId) * int(quantity)) + ";" + "NEW" + ";" + str(username)
    writeOrderFile(orderString)
    updateItemStockQuantity(itemId, quantity)
    return


def deleteOrder(orderId):
    index = 0
    orders = openOrderFile()
    for order in orders:
        if order[0] == str(1):
            orders.pop(index)
        index = index + 1
    writeOrderFileByReplace(orders, 1)
    return None


def editOrderByQuantity(orderId, newQuantity):
    orders = openOrderFile()
    items = openItemFile()
    for order in orders:
        if order[0] == str(1):
            for item in items:
                if item[0] == order[1]:
                    order[3] = str(int(2) * int(item[2]))
                    if int(2) > int(order[2]):
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
    print(" OrderID| ItemID| Quantity| OrderTotalPrice| Status| User")
    for order in orders:
        orderString += str(
            order[0] + "                    " + order[1] + "                    " + order[2] + "                    " +
            order[3] + "                    " + order[4] + "                    " + order[5] + "\n")  # customer order
    print(orderString)
    return None


def viewOrderByOrderId(orderId):
    orders = openOrderFile()
    foundFlag = False
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                   Search Order Details                       ")
    print(" OrderID| ItemID| Quantity| OrderTotalPrice| Status| User")
    for order in orders:
        if order[0] == str(orderId):
            orderString = str(order[0] + "                    " + order[1] + "                    " + order[
                2] + "                    " + order[3] + "                    " + order[4] + "                    " +
                              order[5])
            print(orderString)
            foundFlag = True
    if not foundFlag:
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
    return


def writeOrderFileByReplace(writeOrder, writeMode):
    writeFileDb = open("db/order.txt", "w")
    writeString = ""
    count = 0
    for order in writeOrder:
        if writeMode == 1:
            writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + order[5]
        elif (writeMode == 2):
            if count == 0:
                writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + \
                               order[5] + "\n"
            else:
                writeString += order[0] + ";" + order[1] + ";" + order[2] + ";" + order[3] + ";" + order[4] + ";" + \
                               order[5]
        count = count + 1
    writeFileDb.write(writeString)

# End of order.py


# Context of payment.py

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
            os.system('cls')
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

# End of payment.py


# Context of user.py

def checkUserRoleAndRedirect(username,role):
    if role == "admin":
        adminHome()
    elif role == "staff":
        deliveryHome(username)
    elif role == "customer":
        customerHome(username)


def openUserFile():
    users = []
    userDb = db = open("db/user.txt", "r")
    for i in userDb:
        username, password, role = i.split(";")
        users.append([username.strip(), password.strip(), role.strip()])
    return users

def createUser(username, password):
    userString = "\n" + str(username) + ";" + str(password) + ";" + "customer"
    writeUserFile(userString)
    return

def createDeliveryStaff(username):
    userString = "\n" + str(username) + ";" + str(1234) + ";" + "staff"
    writeUserFile(userString)
    return

def viewDeliveryStaff():
    userDb = openUserFile()
    for user in userDb:
        if user[2] == "staff":
            staffString = user[0] + " " + user[1] + " " + user[2]
            print(staffString)
    return

def deleteUser(deleteUserName):
    index = 0
    users = openUserFile()
    for user in users:
        if user[0] == str (deleteUserName):
            users.pop(index)
        index = index + 1
    writeUserFileByReplace(users,2)
    return None

def viewCurrentPassword(username):
    users = openUserFile()
    for user in users:
        if user[0] == username:
            print("Current Password: " + user[1])
    return

def changePassword(username, newPassword):
    users = openUserFile()
    for user in users:
        if user[0] == username:
            user[1] = newPassword
    writeUserFileByReplace(users, 2)

def writeUserFile(writeFile):
    writeFileDb = open("db/user.txt", "a")
    writeFileDb.write(writeFile)
    return

def writeUserFileByReplace(users, writeMode):
    writeFileDb = open("db/user.txt", "w")
    writeString = ""
    count = 0
    for user in users:
        if writeMode == 1:
            writeString += user[0] + ";" + user[1] + ";" + user[2]
        elif writeMode == 2:
            if count == 0:
                writeString += user[0] + ";" + user[1] + ";" + user[2] + "\n"
            else:
                writeString += user[0] + ";" + user[1] + ";" + user[2] + "\n"
        count = count + 1
    writeFileDb.write(writeString)

# End of user.py

# Context of main.py

def home():
    option = input("Please input 1 to login, input 2 to sign up.")
    if option == "1":
        access()
    elif option == "2":
        register()
    else:
        os.system('cls')
        print("Invalid option")
        home()


def adminHome():
    # TODO Decorate
    option = input(
        "1. Add Category\n2. Add Item \n3. Add Item to Category\n4. Modify Item\n5. View record of Items\n6. View record of Item by category\n7.View all record of Customer Orders\n8.View all record of Customer Payment\n9.Search Customer Order\n10.Search Customer Payment\n11. Delivery System (Admin)\n12. Back\nPlease enter your choice: ")
    os.system('cls')
    if option == str(1):
        addCategoryMenu()
    elif option == str(2):
        createItemMenu()
    elif option == str(3):
        addItemIntoCategory()
    elif option == str(4):
        modifyItemMenu()
    elif option == str(5):
        viewRecordOfItemMenu()
    elif option == str(6):
        viewItemByCategoryMenu()
    elif option == str(7):
        viewCustomerOrderMenu()
    elif option == str(8):
        viewCustomerPayment()
    elif option == str(9):
        searchOrderByOrderIdMenu()
    elif option == str(10):
        searchPaymentByPaymentId()
    elif option == str(11):
        viewDeliverySystemMenu()
    elif option == str(12):
        home()
    else:
        os.system('cls')
        print("Invalid option... returning to menu again")
        adminHome()


def customerHome(user=""):
    print("Customer Menu")
    print("=============")
    print("1. View Item Per Category")
    print("2. See All Item")
    print("3. Place an order")
    print("4. Make Payment")
    print("5. View delivery status")
    print("6. Create delivery feedback")
    print("7. Back")
    option = input("Input your option:")
    os.system('cls')
    if option == str(1):
        viewItemByCategoryMenu("customer")
    elif option == str(2):
        viewRecordOfItemMenuCustomer("customer")
    elif option == str(3):
        placeOrderMenu(user)
    elif option == str(4):
        makePaymentMenu(user)
    elif option == str(5):
        viewDeliveryStatusMenu(user)
    elif option == str(6):
        createDeliveryFeedbackMenu(user)
    elif option == str(7):
        home()
    else:
        os.system('cls')
        cautionInput = input("Invalid option ! Press any key to go back.")
        customerHome()
    return


def deliveryHome(username):
    print("Welcome to delivery staff menu")
    print("==============================")
    print("1. View/Update My Delivery")
    print("2. Assign delivery to myself")
    print("3. Change account password")
    print("4. Back")
    option = input("Option: ")
    os.system('cls')
    if option == str(1):
        viewDeliveryOrderMenu(username)
    elif option == str(2):
        assignDeliveryToMySelfMenu(username)
    elif option == str(3):
        changeAccountPasswordMenu(username)
    elif option == str(4):
        home()
    else:
        os.system('cls')
        cautionInput = input("Invalid option ! Press any key to go back.")
        deliveryHome(username)
    return


if __name__ == "__main__":
    home()

# End of main.py

# Context of menu.py

def createItemMenu():
    print("Existing item")
    viewItem()
    option = input("Do you wish to add item ? 1. Continue, any Key to back")
    if option == str(1):
        itemDescription = input("New Item Description:")
        itemUnitPrice = input("New Item Unit Price:")
        viewCategory()
        # Validation later
        itemCategory = input("New Item Category:")
        itemStockQuantity = input("New Item Stock Quantity:")
        print("\n Create item processing ...")
        createItem(itemDescription, itemUnitPrice, itemCategory, itemStockQuantity)
        print("\n Item Created Successfully...")
        continueInput = input("Press any key to continue")
        adminHome()
        return
    else:
        adminHome()
        return
def addItemIntoCategory():
    viewCategory()
    option = input("Do you wish to add item ? 1. Continue, any Key to back")
    if option != str(1):
        category = input("Category ID:")
        itemDescription = input("New Item Description:")
        itemUnitPrice = input("New Item Unit Price:")
        itemStockQuantity = input("New Item Stock Quantity:")
        print("\n Create item processing ...")
        createItem(itemDescription, itemUnitPrice, category, itemStockQuantity)
        print("\n Item Created Successfully in with Category ID:" + category)
        continueInput = input("Press any key to continue")
        return
    else:
        adminHome()
        return

def modifyItemMenu():
    print("Modify Item")
    viewItem()
    itemOption = input("Input item desired")
    print("Wish field do you wish to update ?")
    print("1. Item Category")
    print("2. Item Description")
    print("3. Item Unit Price")
    print("4. Item Stock Quantity")
    modifyOption = input("input your selection:")
    if modifyOption == str(1):
        newCategory = input("Please enter new category:")
        updateItemCategory(itemOption, newCategory)
    elif modifyOption == str(2):
        newDescription = input("Please enter new description:")
        updateItemDescription(itemOption, newDescription)
    elif modifyOption == str(3):
        newUnitPrice = input("Please enter new unit price:")
        updateItemUnitPrice(itemOption, newUnitPrice)
    elif modifyOption == str(4):
        newStockQuantity = input("Please enter new stock quantity:")
        updateItemStockQuantity(itemOption, newStockQuantity)
    else:
        print("Invalid option, redirect to home.")
        adminHome()

    adminHome()


def viewRecordOfItemMenu():
    viewItem()
    option = input("Please any key to back.")
    adminHome()

def viewRecordOfItemMenuCustomer(role="admin"):
    viewItem()
    option = input("Please any key to back.")
    if role != "admin":
        os.system('cls')
        customerHome()
    adminHome()
    return

def viewItemByCategoryMenu(role="admin"):
    viewCategory()
    option = input("Please select your category desired")
    viewItemByCategory(option)
    option = input("Please any key to back.")
    if role != "admin":
        customerHome()
    adminHome()
    return


def viewCustomerOrderMenu():
    viewOrder()
    option = input("Please any key to back.")
    adminHome()
    return;


def viewCustomerPayment():
    viewPayment()
    option = input("Please any key to back.")
    adminHome()
    return;

def addCategoryMenu():
    print("Existing Category")
    viewCategory()
    option = input("Do you wish to continue to add category ? 1.Continue, others Key to go back")
    if option == str(1):
        newCategory = input("Please input new category name")
        createCategory(newCategory)
        print("Category added successfully !")
        option = input("Please any key back to menu")
        adminHome()
    else:
        adminHome()


def viewDeliverySystemMenu():
    print("Welcome to delivery system menu - only accessible by Admin")
    print("1. Add delivery staff")
    print("2. Delete Delivery staff")
    print("3. View Delivery staff")
    print("4. Assign order for delivery staff")
    print("Others key to go back")
    option = input("Please input your option:")
    if option == str(1):
        addDeliveryStaffMenu()
    elif option == str(2):
        deleteDeliveryStaffMenu()
    elif option == str(3):
        viewDeliveryStaffMenu()
    elif option == str(4):
        assignOrderForDeliveryStaffMenu()
    else:
        os.system('cls')
        adminHome()


def addDeliveryStaffMenu():
    newDeliveryStaff = input("Please enter new delivery staff name:")
    createDeliveryStaff(newDeliveryStaff)
    print("Delivery stuff created successfully. Default login password: 1234")
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return


def deleteDeliveryStaffMenu():
    viewDeliveryStaff()
    deleteUserName = input("Please enter the username that want to delete:")
    deleteUser(deleteUserName)
    print("Delivery staff deleted successfully !")
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return


def viewDeliveryStaffMenu():
    viewDeliveryStaff()
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return;


def assignOrderForDeliveryStaffMenu():
    viewDeliveryByUnassigned()
    orderOption = input("Please select order to assign:")
    viewDeliveryStaff()
    staffOption = input("Please select staff to deliver")
    assignDeliveryStaff(orderOption,staffOption)
    quitOption = input("Assign successfully, please any key to continue")
    adminHome()
    return


def placeOrderMenu(username):
    viewItem()
    select = input("Do you wish to continue to place order ? 1. Yes, or any Key to back")
    if select == str(1):
        orderItem = input("Item:")
        quantity = input("Quantity:")
        createOrder(orderItem, quantity,username)
    else:
        customerHome()
    return


def makePaymentMenu(username):
    viewOrder()
    select = input("Do you wish to continue to make payment ? 1. Yes, 2. No")
    if select == str(1):
        orderItem = input("Order:")
        paymentAmount = input("Payment Amount:")
        createPayment(orderItem, paymentAmount,username)
    else:
        customerHome()
    return

def viewDeliveryOrderMenu(username):
    viewDeliveryByUser(username)
    option = input("Do you wish to update the delivery status ? 1. Yes, Any key to go back")
    if option != str(1):
        deliveryHome(username)
        return
    deliveryId = input("Delivery ID:")
    print(" Status ")
    print("========")
    print("1. Ongoing")
    print("2. Pending")
    print("3. Onhold")
    print("4. Done")
    status = input("Status:")
    updateDeliveryStatus(deliveryId,status)
    print("Update delivery status successfully !")
    option1 = input("Please any key back to menu")
    deliveryHome(username)
    return


def assignDeliveryToMySelfMenu(username):
    viewDeliveryByUnassigned()  # might be unassigned one
    option = input("Do you wish to update the delivery status ? 1. Yes, Any key to go back")
    if option != str(1):
        deliveryHome(username)
        return
    deliveryId = input("Delivery ID:")
    assignDeliveryStaff(deliveryId,username)
    fakeAction = input("Assigned successfully ! Press any Key to go back")
    deliveryHome(username)


def changeAccountPasswordMenu(username):
    viewCurrentPassword(username)
    option = input("Do you wish to change password ? 1. Yes, any Key to go back")
    if option == str(1):
        password = input("Please enter your new password")
        changePassword(username,password)
        fakeAction = input("Password changed successfully ! Press any Key to go back")
        deliveryHome(username)
    else:
        deliveryHome(username)


def viewDeliveryStatus():
    viewCurrentDeliveryByUser()
    option = input("Please any key back to menu")
    customerHome()


def createDeliveryFeedbackMenu():
    print("Create delivery feedback menu")
    viewCurrentDeliveryByUser()
    deliveryId = input("Pleas enter the delivery ID that you wish to get feedback:")
    feedback = input("Please enter you feedback:")
    createDeliveryFeedback(deliveryId, feedback)
    fakeAction = input("Feedback successfully ! Press any Key to go back")
    customerHome()
    return


def viewDeliveryStatusMenu(user):
    viewDeliveryByUser(user)
    fakeAction = input("Press any Key to go back")
    customerHome()
    return


def createDeliveryFeedbackMenu(user):
    viewDeliveryByUser(user)
    deliveryId = input("Delivery Id:")
    feedback = input("Feedback:")
    createDeliveryFeedback(deliveryId,feedback)
    print("Feedback successfully, press any Key to go back")
    fakeAction = input("Press any Key to go back")
    customerHome()
    return


def searchOrderByOrderIdMenu():
    orderId = input("Please insert order id:")
    viewOrderByOrderId(orderId)
    fakeInput = input("Enter any Key to back.")
    adminHome()


def searchPaymentByPaymentId():
    paymentId = input("Please insert payment id:")
    viewPaymentByPaymentId(paymentId)
    fakeInput = input("Enter any Key to back.")
    adminHome()

# End of menu.py