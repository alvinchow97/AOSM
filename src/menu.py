from item import viewCategory, viewItem, createItem, viewItemByCategory, updateItemCategory, updateItemDescription, \
    updateItemUnitPrice, updateItemStockQuantity, createCategory
from order import viewOrder
from main import adminHome,customerHome
from payment import viewPayment, createPayment
from order import createOrder


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


def viewRecordOfItemMenu():
    viewItem()
    option = input("Please any key to back.")
    adminHome()


def viewItemByCategoryMenu():
    viewCategory()
    option = input("Please select your category desired")
    viewItemByCategory(option)
    option = input("Please any key to back.")
    adminHome()


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


def staffMenu():
    print("staffMenu");
    return


def addCategoryMenu():
    print("Existing Category")
    viewCategory()
    option = input("Do you wish to continue to add category ? 1.Continue, others Key to go back")
    if (option == str(1)):
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
    option =  input("Please input your option:")
    if option == str(1):
        addDeliveryStaffMenu()
    elif option == str(2):
        deleteDeliveryStaffMenu()
    elif option == str(3):
        viewDeliveryStaffMenu()
    elif option == str(4):
        assignOrderForDeliveryStaffMenu()
    return

def addDeliveryStaffMenu():
    newDeliveryStaff = input("Please enter new delivery staff name:")
    # pending add delivery staff
    print("Delivery stuff created successfully. Default login password: 1234")
    return

def deleteDeliveryStaffMenu():
    # Pending create
    viewDeliveryStaff()
    option = input("Please any key back to menu")
    adminHome()
    return

def viewDeliveryStaffMenu():
    viewDeliveryStaff()
    return;

def assignOrderForDeliveryStaffMenu():
    viewOrder()
    orderOption = input("Please select order to assign:")
    assignOrderWithDeliveryStaff(orderOption)
    quitOption = input("Assign successfully, please any key to continue")
    adminHome()

def placeOrderMenu():
    viewItem()
    select = input("Do you wish to continue to place order ? 1. Yes, or any Key to back")
    if select == str(1):
        orderItem = input("Item:")
        quantity = input("Quantity:")
        createOrder(orderItem, quantity)
    else:
        customerHome()
    return

def makePaymentMenu():
    viewOrder()
    select = input("Do you wish to continue to place order ? 1. Yes, 2. No")
    if select == str(1):
        orderItem = input("Order:")
        paymentAmount = input("Payment Amount:")
    createPayment(orderItem,paymentAmount)


