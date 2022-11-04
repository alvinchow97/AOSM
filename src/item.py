# TODO TOP PRIORITY, GET THIS DONE FIRST


# TODO CRUD - CREATE/READ/UPDATE/DELETE, do this in sequence

def createItem(item):
    # OPEN FILE, READ FILE
    items = openItemFile()
    highestId = 0

    for i in items:
        if (int(i[0]) > highestId):
            highestId = int(i[0])

    highestId = highestId + 1
    itemString = "\n" + str(highestId) + ";" + "empty item description" + ";" + str(5) + ";" + str(5) + ";" + str(20)
    writeItemFile(itemString)
    # GET THE LATEST ITEM ID
    # ON TOP OF LATEST ITEM ID, +1
    # WRITE INTO THE FILE
    return None


def createCategory(category):
    # OPEN FILE, READ FILE
    # GET THE LATEST CATEGORY ID
    # ON TOP OF THE LATEST CATEGORY ID, +1
    # WRITE INTO THE FILE
    return None


def viewItem():
    # IN THIS CASE, WE VIEW THE FILE BY ALL, IF NEEDED TO SPECIFIC, CREATE ANOTHER FUNCTION
    # OPEN FILE, READ FILE
    items = openItemFile()
    # RETURN THE ITEM, REPLACE THE NONE BELOW

    # TODO , do the UI Interface

    # Press back, back to menu (refer to the function below)

    return items


def viewItemByCategory(categoryId):
    # OPEN ITEM FILE, READ FILE
    items = openItemFile()
    # OPEN CATEGORY FILE, READ FILE
    # DISPLAY WHAT IS THE CATEGORY NAME
    # FETCH THE ITEM UNDER THE CATEGORY ID
    # RETURN THE VIEW, REPLACE NONE BELOW
    return None


def updateItemUnitPrice(itemId, updatedUnitPrice):
    # TODO assume itemId is 1 , and updateUnitPrice is 10
    # OPEN FILE, READ FILE
    items = openItemFile()
    itemsLocated = []
    for item in items:
        if(item[0] == str(1)):
            item[3] = str(10) # update itemUnitPrice happen here

    writeItemFileByReplace(items)
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST UNIT PRICE

    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemStockQuantity(itemId, stockQuantity):
    # IN THIS CASE, FOR ADMIN USE, NOT ORDER
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST STOCK QUANTITY
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemStockQuantityByReduce(itemId, reduceNo):
    # FOR ORDER USE
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST STOCK QUANTITY , CURRENT STOCK QUANTTIY - reduceNo
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemCategory(itemId, newCategory):
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST CATEGORY
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemDescription(itemId, newDescription):
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST ITEM DESCRIPTION
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def deleteItem(itemId):
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # DELETE THE ROW OF THE ITEM
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def deleteCategory(categoryId):
    # TODO HARDEST PART IN THIS MODULE
    # OPEN CATEGORY FILE, READ FILE
    # OPEN ITEM FILE, READ FILE
    # FIND IF GOT ANY ITEM IS IN THIS CATEGORY
    # IF YES, DELETE THEN CONTINUE TO NEXT STEP, IF NOT, CONTINUE TO NEXT STEP
    # AFTER ITEM UNDER THE CATEGORY IS DELETED, ONLY DELETE THE CATEGORY
    # DELETE CATEGORY
    return None


# TODO MISC , OTHER FUNCTION SUPPORT THE TOP PART


def itemMenu():
    # DO ANY MENU ACTION HERE, USING SWITCH CASE
    return None


def openItemFile():
    # DO THE OPEN FILE READ FILE ACTION HERE
    items = []
    itemDb = db = open("db/item.txt", "r")
    for i in itemDb:
        itemId, itemDescription, itemUnitPrice, categoryId, stockQuantity = i.split(";")
        items.append([itemId, itemDescription, itemUnitPrice, categoryId, stockQuantity])
    # THEN REPLACE THE COMMENT ABOVE
    # RETURN WHAT INSIDE THE FILE
    return items


def openCategoryFile():
    # DO THE OPEN FILE READ FILE ACTION HERE
    categories = []
    categoryDb = db = open("db/category.txt", "r")
    for i in categoryDb:
        categoryId, categoryName = i.split(";")
        categories.append([categoryId, categoryName])
    # THEN REPLACE THE COMMENT ABOVE
    # RETURN WHAT INSIDE THE FILE
    return categories


def writeItemFile(writeFile):
    writeFileDb = open("db/item.txt", "a")
    writeFileDb.write(writeFile)
    # FIND THE FILE, READ THE FILE
    # WRITE THE FILE
    # RETURN TRUE IF GOOD, FALSE IF FAILED
    return None

def writeItemFileByReplace(writeItem):
    writeString = ""
    count = 0
    maxCount = len(writeItem)
    for item in writeItem:
        if (count == 0 or count >= maxCount):
            writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]
        else:
            writeString += "\n" + item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]

    writeFileDb = open("db/item.txt", "w")
    writeFileDb.write(writeString)
def writeCategoryFile(writeFile):
    # FIND THE FILE, READ THE FILE
    # WRITE THE FILE
    # RETURN TRUE IF GOOD, FALSE IF FAILED
    return None

# TODO MISC, put test function here to try
updateItemUnitPrice([],[]);