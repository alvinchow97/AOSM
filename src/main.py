from login import home
from menu import home

#login is file
#home is function
def home():
    # STEP 1
    # Let the user to key in 1/2 for Login or Sign Up
    option = input("Please input 1 to login, input 2 to sign up.")
    if (option == "1"):
        access()
    elif (option == 2):
        register()
    else:
        print("Invalid option")

#If login, let the user to key in username/password
    result = access()
    db = openUserFile()
    username = input("Enter username:")
    password = input("Enter Password:")
    for user in userDb:
        if(username == user[0] and password == user[1]):
            if (username != user[0]):
                print("Wrong username")
        return home
    #username wrong, prompt Wrong (new display function in display.py), go back key in username
        #password wrong, let the user to key in up to 3 times, if not go back to key in username/password
        #if correct, go to STEP 2
        #If sign up, let the user to key in username/password
from user import home
with open("database.txt", "a"):
    db.write(username + ", " + password + "\n")
    print("Successfully register!")

    return login
        #after sign up, back to login at above (no need validation)

    #STEP 2
    # Check the user is what role, go to different page.
        # Admin go to Admin page
        # Customer go to Customer page
        # Delivery staff go to Delivery page

def adminHome():
    # Admin Home , STEP 1
    # show the menu to check what action
    # Add Category, Add Item into Category, Modify Item, Display all record, Search specific record, Order Management System
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

        #Check delivery status
        #Let the user check the delivery attach to the him/she
        #Update feedback to delivery with status completed
        #Key in the feedback, press any key back to customer menu
def deliveryHome():
    # STEP 1
    # Show all available option
    # View all order (that unassigned delivery staff)
    # Select desired order, let the user type
    # Update delivery status
    # Let the user see order in hand, status of progress
    # List out progress option. 1.Not ready, 2. Ready for delivery. 3. Delivering etc
    # Let the user key in, then press any key back to delivery menu


def optionMenu():
    # Temporary for guided use, DO NOT DELETE
    # Prompt username wrong
    # prompt password wrong
    # prompt Login/Sign Up
    # Prompt password wrong, param (username, password, timeOfTry) - return boolean
    # In progress
if __name__ == "__main__":
    home()

#test
home()