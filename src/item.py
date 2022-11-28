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
    categoryDb = openCategoryFile(category)
    highestId = 0
    for i in categoryDb:
        if (int(i[0]) >= highestId):
            highestId = (int(i[0]) + 1)

    highestId = highestId + 1
    categoryString =  + str(highestId) + ""
    writeCategoryFile(categoryString)
    # GET THE LATEST CATEGORY ID
    # ON TOP OF THE LATEST CATEGORY ID, +1
    # WRITE INTO THE FILE



    Categoryname = input("Enter a category name: ")
    print("successfully added a new category")

    return None

def viewItem():
    # IN THIS CASE, WE VIEW THE FILE BY ALL, IF NEEDED TO SPECIFIC, CREATE ANOTHER FUNCTION
    # OPEN FILE, READ FILE
    items = openItemFile()
    # RETURN THE ITEM, REPLACE THE NONE BELOW

    # TODO , do the UI Interface
    printString = ""
    # TODO , do the UI Interface
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     This is Item List                         ")
    for item in items:
         printString += str(item[0] + " " + item[1]) + "\n"
    print(printString)

    # Press back, back to menu (refer to the function below)
    #HanBin changes
    return None

def viewCategory():
    # IN THIS CASE, WE VIEW THE FILE BY ALL, IF NEEDED TO SPECIFIC, CREATE ANOTHER FUNCTION
    # OPEN FILE, READ FILE
    categories = openCategoryFile()
    # RETURN THE ITEM, REPLACE THE NONE BELOW

    # TODO , do the UI Interface
    printString = ""
    # TODO , do the UI Interface
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    print("                     This is Category                         ")
    for category in categories:
        printString += (str(category[0] + " " + category[1]) + "\n")
    print(printString)

    # Press back, back to menu (refer to the function below)
    # HanBin changes
    return None

def viewItemByCategory(categoryId, category):
    # OPEN ITEM FILE, READ FILE
    items = openItemFile(item.txt)
    # OPEN CATEGORY FILE, READ FILE
    categoryDb = openCategoryFile(category.txt)
    # DISPLAY WHAT IS THE CATEGORY NAME
    print(categoryId)
    # FETCH THE ITEM UNDER THE CATEGORY ID
    print("""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""")
    for item in items:
        item[4] = ItemByCategory
        ItemByCategory = int(item[4]) + str(";" + item[2]) + "\n"
        print(ItemByCategory)
    # RETURN THE VIEW, REPLACE NONE BELOW
    return viewItem()


def updateItemUnitPrice(itemId, updatedUnitPrice):
    # TODO assume itemId is 1 , and updateUnitPrice is 10
    # OPEN FILE, READ FILE
    items = openItemFile()
    itemsLocated = []
    for item in items:
        if(item[0] == str(1)):
            item[2] = str(88) # update itemUnitPrice happen here
    writeItemFileByReplace(items,1)
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST UNIT PRICE

    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemStockQuantity(itemId, stockQuantity):
    # IN THIS CASE, FOR ADMIN USE, NOT ORDER
    # OPEN FILE, READ FILE
    # TODO assume itemId is 1 , and stockQuantity is 2
    items = openItemFile()
    itemsLocated = []
    # TODO replace the 2 later with the quantity later, validation last do (last week)
    for item in items:
        if (item[0] == str(1)):
            item[4] = str(int(30)) # update stockQuantity happen here

    writeItemFileByReplace(items,2)
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST STOCK QUANTITY
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def updateItemStockQuantityByReduce(itemId, reduceNo):
    items = openItemFile()
    # TODO replace the 2 later with the quantity to be reduce later, validation last do (last week)
    # TODO replace the 1 with the itemId later
    for item in items:
        if (item[0] == str(1)):
            item[4] = str(int(int(item[4]) - 2))  # update stockQuantity happen here (reduce by 2)

    writeItemFileByReplace(items, 2)
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
    # TODO replace the 1 with the itemId later, 5 for categoryId/newCategory
    items = openItemFile()
    for item in items:
        if (item[0] == str(1)):
            item[3] = str(int(5))  # update stockQuantity happen here (reduce by 2)

    writeItemFileByReplace(items, 1)
    return None


def updateItemDescription(itemId, newDescription):
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # UPDATE THE LATEST ITEM DESCRIPTION
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    # TODO replace the 1 with the itemId later, "new description" for newDescription
    items = openItemFile()
    for item in items:
        if (item[0] == str(1)):
            item[1] = str("test new description")  # update stockQuantity happen here (reduce by 2)

    writeItemFileByReplace(items, 1)
    return None


def deleteItem(itemId):
    index = 0
    items = openItemFile()
    # TODO replace the 1 with the itemId later
    for item in items:
        if (item[0] == str(1)):
            items.pop(index)
        index = index + 1
    writeItemFileByReplace(items, 1)
    # OPEN FILE, READ FILE
    # FIND THE INDEX WHERE THE ITEM IS LOCATED
    # DELETE THE ROW OF THE ITEM
    # WRITE BACK TO THE FILE
    # RETURN TRUE IF DONE GOOD, FALSE IF FAILED
    return None


def deleteCategory(categoryId):
    # TODO HARDEST PART IN THIS MODULE
    # OPEN CATEGORY FILE, READ FILE
    categories = openCategoryFile()
    items = openItemFile()

    replacedItems = items.copy()
    replacedCategories = categories.copy()

    itemIndex = 0
    categoryIndex = 0
    # TODO replace 1 with categoryId
    for category in categories:
        if(category[0] == str(1)):
            # found category, check any items if got same category, if got, then delete
            for item in items:
                if(item[3] == str(1)):
                    if(len(replacedItems) == len(items)):
                        replacedItems.pop(itemIndex)
                    else:
                        replacedItems.pop(itemIndex-1)
                itemIndex = itemIndex + 1
            writeItemFileByReplace(replacedItems, 1)

            if(len(replacedCategories) == len(categories)):
                categories.pop(categoryIndex)
            else:
                categories.pop(categoryIndex - 1)
        categoryIndex = categoryIndex + 1
    writeCategoryFileByReplace(categories,1)
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

def writeItemFileByReplace(writeItem,writeMode):
    # TODO writeMode = 1/2, 1 no need + \n
    writeString = ""
    count = 0
    for item in writeItem:
        if (writeMode == 1):
            writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]
        elif(writeMode == 2):
            if (count == 0):
                writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4] + "\n"
            else:
                writeString += item[0] + ";" + item[1] + ";" + item[2] + ";" + item[3] + ";" + item[4]
        count = count + 1
    writeFileDb = open("db/item.txt", "w")
    writeFileDb.write(writeString)

def writeCategoryFileByReplace(writeCategory,writeMode):
    # TODO writeMode = 1/2, 1 no need + \n
    writeString = ""
    count = 0
    for item in writeCategory:
        if (writeMode == 1):
            writeString += item[0] + ";" + item[1]
        elif(writeMode == 2):
            if (count == 0):
                writeString += item[0] + ";" + item[1] + "\n"
            else:
                writeString += item[0] + ";" + item[1]
        count = count + 1
    writeFileDb = open("db/category.txt", "w")
    writeFileDb.write(writeString)
def writeCategoryFile(writeCategory,writeMode):
    # FIND THE FILE, READ THE FILE
    # WRITE THE FILE
    # RETURN TRUE IF GOOD, FALSE IF FAILED
    writeString = ""
    count = 0
    for item in writeCategory:
        if (writeMode == 1):
            writeString += item[0] + ";" + item[1]
        elif (writeMode == 2):
            if (count == 0):
                writeString += item[0] + ";" + item[1]
            else:
                writeString += item[0] + ";" + item[1]
        count = count + 1
    writeFileDb = open("db/category.txt", "w")
    writeFileDb.write(writeString)
    return None

# TODO MISC, put test function here to try
viewItem()
