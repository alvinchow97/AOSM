#TODO THIRD PRIORITY
#TODO Redefine {orderId,quantity, itemId, itemPrice, orderTotalPrice,status, user} to {orderId,quantity, itemId, orderTotalPrice, user}
# FOLLOW RULES OF CRUD, CREATE/READ/UPDATE/DELETE

def createPayment(orderId):
    #OPEN FILE AND READ FILE FOR ORDER
    #SEARCH THE ORDER BASED ON THE ORDER ID
    #CHECK THE ORDER PAYMENT STATUS IF UNPAID
    #IF YES, THEN PROCEED, IF PAID, THEN TELL THE USER TO IS PAID AND ASK IF WANT TO CONTINUE
    #GET THE TOTAL AND PROMPT TO THE USER IF WANT TO PAY
    #IF THE USER DIDNT WANT TO PAY, UPDATE STATUS OF THE ORDER TO UNPAID
    #IF THE USER WANT TO PAY, ASK THE USER TO KEY IN TOTAL PAID, THEN UPDATE THE STATUS TO PAID OF ORDER
    return None

def viewPayment():
    #OPEN FILE AND READ FILE OF PAYMENT
    #LIST IT OUT
    return None


def deletePayment(paymentId):
    #READ FILE OF PAYMENT
    #IDENTIFY WHICH ROW OF THE PAYMENT IS
    #DELETE THE PAYMENT, WRITE INTO FILE
    return None


