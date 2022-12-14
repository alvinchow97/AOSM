from item import viewCategory, viewItem, createItem, viewItemByCategory, updateItemCategory, updateItemDescription, \
    updateItemUnitPrice, updateItemStockQuantity, createCategory
from order import viewOrder, viewOrderByOrderId
from main import adminHome, customerHome, deliveryHome
from payment import viewPayment, createPayment, viewPaymentByPaymentId
from order import createOrder
import user
from delivery import assignDeliveryStaff,viewDeliveryByUser,createDeliveryFeedback, updateDeliveryStatus,viewDeliveryByUnassigned
import os

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
    user.createDeliveryStaff(newDeliveryStaff)
    print("Delivery stuff created successfully. Default login password: 1234")
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return


def deleteDeliveryStaffMenu():
    user.viewDeliveryStaff()
    deleteUserName = input("Please enter the username that want to delete:")
    user.deleteUser(deleteUserName)
    print("Delivery staff deleted successfully !")
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return


def viewDeliveryStaffMenu():
    user.viewDeliveryStaff()
    option = input("Please any key back to menu")
    viewDeliverySystemMenu()
    return;


def assignOrderForDeliveryStaffMenu():
    viewDeliveryByUnassigned()
    orderOption = input("Please select order to assign:")
    user.viewDeliveryStaff()
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
    user.viewCurrentPassword(username)
    option = input("Do you wish to change password ? 1. Yes, any Key to go back")
    if option == str(1):
        password = input("Please enter your new password")
        user.changePassword(username,password)
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
