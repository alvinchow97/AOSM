from login import access, register
from menu import addCategoryMenu, createItemMenu, viewItemByCategoryMenu, modifyItemMenu, viewRecordOfItemMenu, \
    viewCustomerOrderMenu, viewCustomerPayment, viewDeliverySystemMenu,placeOrderMenu, makePaymentMenu, viewDeliveryOrderMenu, assignDeliveryToMySelfMenu, changeAccountPasswordMenu


def home():
    option = input("Please input 1 to login, input 2 to sign up.")
    if option == "1":
        access()
    elif option == 2:
        register()
    else:
        print("Invalid option")


def adminHome():
    option = input(
        "1. Add Category\n2. Add Item\n3. Modify Item\n4. View record of Items\n5. View record of Item by category\n6.View all record of Customer Orders\n7.View all record of Customer Payment\n8.Search Customer Order\n9.Search Customer Payment\n10. Add/Modify/search/delete Delivery Staff\n11.Assign orders for delivery staff\n12. Exit\nPlease enter your choice: ")
    if option == str(1):
        addCategoryMenu()
    elif option == str(2):
        createItemMenu()
    elif option == str(3):
        modifyItemMenu()
    elif option == str(4):
        viewRecordOfItemMenu()
    elif option == str(5):
        viewItemByCategoryMenu()
    elif option == str(6):
        viewCustomerOrderMenu()
    elif option == str(7):
        viewCustomerPayment()
    elif option == str(8):
        viewDeliverySystemMenu()
    else:
        print("Invalid option")
        adminHome()


def customerHome():
    print("Customer Menu")
    print("=============")
    print("1. View Item Per Category")
    print("2. See All Item")
    print("3. Place an order")
    print("4. Make Payment")
    print("5. View delivery status")
    print("6. Create delivery feedback")
    option = input("Input your option:")
    if option == str(1):
        viewItemByCategoryMenu()
    elif option == str(2):
        viewRecordOfItemMenu()
    elif option == str(3):
        placeOrderMenu()
    elif option == str(4):
        makePaymentMenu()
    elif option == str(5):
        viewDeliveryStatus()
    elif option == str(6):
        createDeliveryFeedbackMenu()
    else:
        cautionInput = input("Invalid option ! Press any key to go back.")
        customerHome()


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
    print("Welcome to delivery staff menu")
    print("==============================")
    print("1. View All Order")
    print("2. Assign delivery to myself")
    print("3. Change account password")
    option = input("Option: ")
    if option == str(1):
        viewDeliveryOrderMenu()
    elif option == str(2):
        assignDeliveryToMySelfMenu()
    elif option == str(3):
        changeAccountPasswordMenu()
    # STEP 1
    # Show all available option
    # View all order (that unassigned delivery staff)
    # Select desired order, let the user type
    # Update delivery status
    # Let the user see order in hand, status of progress
    # List out progress option. 1.Not ready, 2. Ready for delivery. 3. Delivering etc
    # Let the user key in, then press any key back to delivery menu
    return


if __name__ == "__main__":
    home()
