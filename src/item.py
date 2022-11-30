
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
    print(printString)
    return


def viewItemByCategory(categoryId):
    # TODO Decorate
    itemDb = openItemFile()
    print("================================================================")
    for item in itemDb:
        if item[3] == categoryId:
            categoryString = "     " + str(item[1]) + "      " + str(item[2]) + "      " + str(item[3]) + "      " + str(item[4]) + "      "
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
