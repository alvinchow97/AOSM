from item import createItem, viewItem



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
