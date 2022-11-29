import login
import menu

def home():
    option = input("Please input 1 to login, input 2 to sign up.")
    if option == "1":
        login.access()
    elif option == 2:
        login.register()
    else:
        print("Invalid option")


def adminHome():
    option = input(
        "1. Add Category\n2. Add Item\n3. Modify Item\n4. View record of Items\n5. View record of Item by category\n6.View all record of Customer Orders\n7.View all record of Customer Payment\n8.Search Customer Order\n9.Search Customer Payment\n10. Delivery System (Admin)\n11. Exit\nPlease enter your choice: ")
    if option == str(1):
        menu.addCategoryMenu()
    elif option == str(2):
        menu.createItemMenu()
    elif option == str(3):
        menu.modifyItemMenu()
    elif option == str(4):
        menu.viewRecordOfItemMenu()
    elif option == str(5):
        menu.viewItemByCategoryMenu()
    elif option == str(6):
        menu.viewCustomerOrderMenu()
    elif option == str(7):
        menu.viewCustomerPayment()
    elif option == str(8):
        menu.searchOrderByOrderIdMenu()
    elif option == str(9):
        menu.searchPaymentByPaymentId()
    elif option == str(10):
        menu.viewDeliverySystemMenu()
    elif option == str(11):
        exit()
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
    option = input("Input your option:")
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
    else:
        cautionInput = input("Invalid option ! Press any key to go back.")
        customerHome()
    return


def deliveryHome():
    print("Welcome to delivery staff menu")
    print("==============================")
    print("1. View All Order")
    print("2. Assign delivery to myself")
    print("3. Change account password")
    option = input("Option: ")
    if option == str(1):
        menu.viewDeliveryOrderMenu()
    elif option == str(2):
        menu.assignDeliveryToMySelfMenu()
    elif option == str(3):
        menu.changeAccountPasswordMenu()
    return


if __name__ == "__main__":
    home()
