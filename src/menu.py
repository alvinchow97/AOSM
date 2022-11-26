from item import createCategory,writeItemFileByReplace,updateItemCategory,updateItemDescription,updateItemUnitPrice,updateItemStockQuantity,viewItemByCategory,writeItemFile,openCategoryFile,openItemFile
from delivery import assignDeliveryStaff,modifyDeliveryStaff,searchDeliveryStaff,deleteDeliveryStaff
from order import editOrderByQuantity
def customerMenu():
    print("customerMenu");
    return


def adminMenu():
    print("adminMenu");
    return
def createItem(item):
    items = openItemFile()
    writeItemFile = open("db/item.txt", "a")
    n = int(input("Create item: "))
    for items in range(n):
        items = int(input("Item Code: " + "," + "Item Description: " + "," + "Item Price: " + "," + "Category: " + "," + "Quantity: " + "\n"))
    writeItemFile(items)
    adminMenu()

def displayAllRecord():
    items = ("openItem.txt")

    # RETURN THE ITEM, REPLACE THE NONE BELOW

    # TODO , do the UI Interface
    printString = ""
    # TODO , do the UI Interface
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     This is Item List                         ")
    for item in items:
        printString += str(item[0] + " " + item[1]) + " " + item[2] + " " + item[3] + " " + item[4] + "\n"
    print(printString)
    adminMenu()


def staffMenu():
    print("staffMenu");
    return

def addCategoryMenu():
    categories = openCategoryFile()
    highestId = 0
    categoryString = ""
    print("The category available currently is")
    print("category.txt")
    print("Please insert your option.")
    CategoryID = input("1. Add Category\n0. Exit")
    createCategory()

def addItemMenu():
    items = openItemFile()
    highestId = 0

    for i in items:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    open("item.txt","a")
    itemDescription = input("Please input item name")
    itemUnitPrice = input("Please enter price for every unit")
    itemCategory = input("Please enter item category")
    stockQuantity = input("Please enter stock quantity")
    itemString = str(highestId) + ";" + itemDescription + ";" + itemUnitPrice ";" + str(itemCategory) + ";" + stockQuantity
    writeItemFile(itemString)
    return adminHome()

def modifyMenu():
    itemsLocated = []
    items = openItemFile()
    searchItemID = input("Enter Item ID to modify item ka~")
    for item in items:
        if (searchItemID in itemsLocated[item][0]):
            highestID = int(item[0])
    newItemName = input(item[1] + " Please enter new item name: ")
    newItemPrice = input(item[2] + "Please enter new item price: ")
    newCategory = input(item[3] + "Please enter new item price: ")
    newStockQuantity = input(item[4] + "Please enter new item price: ")
    item[1] = newItemName
    item[2] = newItemPrice
    item[3] = newCategory
    item[4] = newStockQuantity

    else:
        print("Record Not Found")
    newItemDetails = (str(highestId) + ";" + newItemName + ";" + newItemPrice ";" + newCategory + ";" + newstockQuantity)
    writeItemFileByReplace(newItemDetails)





def viewItemByCategoryMenu()
    itemsLocated = []
    items = openItemFile()

    for item in items:
        if (searchItemByCategory in itemsLocated[item][2]):
            highestID = int(item[0])
    print(items)
    searchItemByCategory = input("Enter Category ID to search ka~")
    if (searchItemByCategory == 1):
    elif(searchItemByCategory == 2):
    elif(searchItemByCategory == 3):
    else:
        ("Wrong Category")
    viewItemByCategory()
Return None

def staffManagementMenu()
    deliveries = openFile()
    deliveriesLocated = []

    searchCategory = input("Enter Item ID to modify item ka~")
    for category in categories:
        if (searchCategory in deliveriesLocated[delivery][0]):
            highestID = int(item[0])
    option = input()
    if (option == "1")
        assignDeliveryStaff()
    elif (option == "2")
        modifyDeliveryStaff()
    elif (option == "3")
        searchDeliveryStaff
    elif (option == "4")
        deleteDeliveryStaff()
    return None



def assignOrderToStaffMenu()
    AssignOrder = input("1.Assign order to delivery staff")
    option = input()
    if (option == "1")
        editOrderByQuantity()
    return None






def addCategoryMenu():
    categories = openCategoryFile()
    highestId = 0
    categoryString = ""
    print("The category available currently is")
    print("category.txt")
    print("Please insert your option.")
    CategoryID = input("1. Add Category\n0. Exit")
    createCategory()

def addItemMenu():
    items = openItemFile()
    highestId = 0

    for i in items:
        if (int(i[0]) > highestId):
            highestId = int(i[0])
    highestId = highestId + 1
    open("item.txt","a")
    itemDescription = input("Please input item name")
    itemUnitPrice = input("Please enter price for every unit")
    itemCategory = input("Please enter item category")
    stockQuantity = input("Please enter stock quantity")
    itemString = str(highestId) + ";" + itemDescription + ";" + itemUnitPrice ";" + str(itemCategory) + ";" + stockQuantity
    writeItemFile(itemString)
    return adminHome()

def modifyMenu():
    itemsLocated = []
    items = openItemFile()
    searchItemID = input("Enter Item ID to modify item ka~")
    for item in items:
        if (searchItemID in itemsLocated[item][0]):
            highestID = int(item[0])
    newItemName = input(item[1] + " Please enter new item name: ")
    newItemPrice = input(item[2] + "Please enter new item price: ")
    newCategory = input(item[3] + "Please enter new item price: ")
    newStockQuantity = input(item[4] + "Please enter new item price: ")
    item[1] = newItemName
    item[2] = newItemPrice
    item[3] = newCategory
    item[4] = newStockQuantity

    else:
        print("Record Not Found")
    newItemDetails = (str(highestId) + ";" + newItemName + ";" + newItemPrice ";" + newCategory + ";" + newstockQuantity)
    writeItemFileByReplace(newItemDetails)





def viewItemByCategoryMenu()
    itemsLocated = []
    items = openItemFile()

    for item in items:
        if (searchItemByCategory in itemsLocated[item][2]):
            highestID = int(item[0])
    print(items)
    searchItemByCategory = input("Enter Category ID to search ka~")
    if (searchItemByCategory == 1):
    elif(searchItemByCategory == 2):
    elif(searchItemByCategory == 3):
    else:
        ("Wrong Category")
    viewItemByCategory()






