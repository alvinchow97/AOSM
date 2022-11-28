from login import access, register
from item import createCategory,createItem,viewItem,viewItemByCategory
from order import viewOrder,viewOrderByOrderId
from payment import viewPayment,viewPaymentByPaymentId
from delivery import assignDeliveryStaff,createDelivery,viewDelivery,deleteDeliveryStaff
from menu import addCategoryMenu,modifyMenu,viewItemByCategoryMenu,staffManagementMenu,assignOrderToStaffMenu

def home():
    option = input("Please input 1 to login, input 2 to sign up.")
    if (option == "1"):
        access()
    elif (option == 2):
        register()
    else:
        print("Invalid option")


def adminHome():
    option = input("1. Add Category\n2. Add Item\n3. Modify Item\n4. View record of Items\n5. View record of Item by category\n6.View all record of Customer Orders\n7.View all record of Customer Payment\n8.Search Customer Order\n9.Search Customer Payment\n10. Add/Modify/search/delete Delivery Staff\n11.Assign orders for delivery staff\n12. Exit\nPlease enter your choice: ")
    switch(option):
    case 1:
        addCategoryMenu()
    case 2:
        createItem()
    case 3:
        modifyMenu()
    case 4:
        viewItem()
    case 5:
        viewItemByCategoryMenu()
    case 6:
        viewOrder()
    case 7:
        viewPayment()
    case 8:
        viewOrderByOrderId()
    case 9:
        viewPaymentByPaymentId()
    case 10:
        staffManagementMenu()
    case 11:
        assignOrderToStaffMenu()
    case 12:
        exit()

    # Han Bin
    # 1. Add admin menu in menu got many action
    # Add Category, Add Item into Category, Modify Item, Display all record, Search specific record, Order Management System
    # 1.xxxx
    # 2.xxxx
    # let the user input the option, if 0 then back to home()

    # According to the function, do each menu for them in menu.py

    # Fabian
    # 1. Add category (follow by Han Bin function)
    # let the user see existing Category -> display out all the category -> do in item.py
    # let the user to key in category field, only name
    # Optional, no need do first, check cannot same category in file
    # tell the user successfully created the category
    # remember import createCategory from item.py
    # do ViewCategory
    return


def addCategoryMenuExample():
    # Fabian use
    return

    # Admin Home , STEP 1
    # show the menu to check what action
    # Category
    # Show available category
    # Let the user key in category name or 0 to quite
    # Add Item into category
    # Show available category and Item
    # Let the user key in item and category ID
    # If item ID or category not found, let the user key in again, 0 to quit

    # Modify Item
    # Show all item
    # Let the user key in the item want to modify
    # Show the item detail and available field to modify
    # Key in the value based on the field
    # Call the function, then display done, press any back to admin menu

    # Display all record
    # Let the user key in what record ? Category, Item etc
    # Display all the record
    # Press any to go back Admin menu

    # Search Specific Record
    # Display all the available category of record, Category, Item etc
    # Let the user key in what type of category he want
    # Let the user key in the ID
    # If found, then ok, not found that show no found, press any key to Admin Menu
    # Delivery Management System
    # go to Delivery Menu (Admin)
    return


def customerHome():
    # STEP 1
    # Show all the option available, view item per category, see all item, place an order, make payment
    # View item per category
    # Show all category
    # Let the user type what category intended
    # Display the item under the category, press any key back to customer menu
    # View All Item
    # Display all item, press any key back to customer menu
    # Place an order
    # Display Item details
    # Let the user key in what should get from order
    # Payment
    # Display the order under the customer
    # Let the user make the payment
    # Display delivery ID that ready for it, press any key to go customer menu

    # Check delivery status
    # Let the user check the delivery attach to the him/she
    # Update feedback to delivery with status completed
    # Key in the feedback, press any key back to customer menu
    return


def deliveryHome():
    # STEP 1
    # Show all available option
    # View all order (that unassigned delivery staff)
    # Select desired order, let the user type
    # Update delivery status
    # Let the user see order in hand, status of progress
    # List out progress option. 1.Not ready, 2. Ready for delivery. 3. Delivering etc
    # Let the user key in, then press any key back to delivery menu
    return


def optionMenu():
    # Temporary for guided use, DO NOT DELETE
    # Prompt username wrong
    # prompt password wrong
    # prompt Login/Sign Up
    # Prompt password wrong, param (username, password, timeOfTry) - return boolean
    # In progress
    return


# if __name__ == "__main__":
#     home()

home()
