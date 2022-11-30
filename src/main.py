import login
import menu
import os
def home():
    option = input("Please input 1 to login, input 2 to sign up.")
    if option == "1":
        login.access()
    elif option == "2":
        login.register()
    else:
        print("Invalid option")
        home()


def adminHome():
    # TODO Decorate
    option = input(
        "1. Add Category\n2. Add Item \n3. Add Item to Category\n4. Modify Item\n5. View record of Items\n6. View record of Item by category\n7.View all record of Customer Orders\n8.View all record of Customer Payment\n9.Search Customer Order\n10.Search Customer Payment\n11. Delivery System (Admin)\n12. Back\nPlease enter your choice: ")
    os.system('cls')
    if option == str(1):
        menu.addCategoryMenu()
    elif option == str(2):
        menu.createItemMenu()
    elif option == str(3):
        menu.addItemIntoCategory()
    elif option == str(4):
        menu.modifyItemMenu()
    elif option == str(5):
        menu.viewRecordOfItemMenu()
    elif option == str(6):
        menu.viewItemByCategoryMenu()
    elif option == str(7):
        menu.viewCustomerOrderMenu()
    elif option == str(8):
        menu.viewCustomerPayment()
    elif option == str(9):
        menu.searchOrderByOrderIdMenu()
    elif option == str(10):
        menu.searchPaymentByPaymentId()
    elif option == str(11):
        menu.viewDeliverySystemMenu()
    elif option == str(12):
        home()
    else:
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
        menu.viewItemByCategoryMenu("customer")
    elif option == str(2):
        menu.viewRecordOfItemMenuCustomer("customer")
    elif option == str(3):
        menu.placeOrderMenu(user)
    elif option == str(4):
        menu.makePaymentMenu(user)
    elif option == str(5):
        menu.viewDeliveryStatusMenu(user)
    elif option == str(6):
        menu.createDeliveryFeedbackMenu(user)
    elif option == str(7):
        home()
    else:
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
        menu.viewDeliveryOrderMenu(username)
    elif option == str(2):
        menu.assignDeliveryToMySelfMenu(username)
    elif option == str(3):
        menu.changeAccountPasswordMenu(username)
    elif option == str(4):
        home()
    else:
        cautionInput = input("Invalid option ! Press any key to go back.")
        deliveryHome(username)
    return


if __name__ == "__main__":
    home()
