import os
from testData import *
from businessLayer import *
def clear(): 
    #clears screen
    os.system('clear')

def showOptions(options):
    # build menu options depending on parameter
    result = ""
    for option in options:
        if option == "L":
            result += "(L) Login"
        elif option == "Q":
            result += "(Q) Quit"
        elif option == "C":
            result += "(C) Checkout"
        elif option == "S":
            result += "(S) Search for product"
        elif option == "A":
            result += "(A) Add to basket"
        elif option == "D":
            result += "(D) display basket content"
        elif option == "1":
            result += "(1) Credit card"
        elif option == "2":
            result += "(2) PayPal"
        elif option == "3":
            result += "(3) Gift Voucher"
        elif option == "4":
            result += "(4) Promo Code"
        result += "\n"
    return result


def selectOption(options, message):
    # repeat until a valid option is selected
    selected = ""
    while not selected or selected not in options:
        print(showOptions(options))
        selected = input(message).upper()
    return selected


def searchProduct(DataBase):
    # search for a product in DataBase
    retrievedProduct = None
    searchParam = input("(Search) Enter product code or description: ")
    if returnInt(searchParam) > 0:
        # if parameter provided is a number, search by code
        retrievedProduct = DataBase.ReadProduct(returnInt(searchParam))
    elif searchParam:
        # if parameter provided is a text, search by description
        retrievedProduct = DataBase.ReadProductByText(searchParam.lower())
    if retrievedProduct != None:
        # if product is found, shows product information
        clear()
        print("Product information:")
        print(retrievedProduct)
    else:
        print("product not found")
    # returns the retrieved Product object (or None if not found)
    return retrievedProduct

def addProduct(shoppingBasket, retrievedProduct):
    # add a product to cart if quantity is greater than 0
    quantity = -1
    while quantity < 0:
        # shows the item selected and ask for quantity
        print("Item: {0}".format(retrievedProduct.description))
        print("Select quantity (available: {0})".format(retrievedProduct.stock))        
        quantity = returnInt(input())
        if quantity > retrievedProduct.stock:
            print("Not enough items in stock")
        elif quantity == 0:
            addToCart(shoppingBasket, retrievedProduct, 0)
            print("0 units selected. Removed from basked")
        else:
            addToCart(shoppingBasket, retrievedProduct, quantity)
            return True
    return False

def addToCart(shoppingBasket, retrievedProduct, quantity):
    # uses the shoppingBasket object to add an orderLine
    newOrderLine = OrderLine(retrievedProduct, quantity)
    shoppingBasket.addOrderLine(newOrderLine)

def returnInt(str):
    # convert string to numeric safely
    number = 0
    if str and str.isnumeric():
        number = int(str)
    return number

if __name__ == '__main__':
    clear()
    # connects to database or instanciate memory object
    DataBase = Entity()
    # load test data
    LoadTestData(DataBase)
    clear()
    retrievedProduct = None
    # create an empty basket
    shoppingBasket = ShoppingBasket(State.InProgress)
    selected = ""
    # set initial UI options
    options = "SQ"    
    # iterate until option "Q" is selected
    while not selected or selected != "Q":
        # select available options depending on product search
        # show shopping cart content
        print("---------SHOPPING-CART-------------")
        print(shoppingBasket)
        print("-----------------------------------")
        State = shoppingBasket.state
        print("Status: {0}".format(State.name))
        print("---------------TOTAL---------------")
        print(shoppingBasket.getTotalFormatted())
        # wait for user input
        if shoppingBasket.state == State.InProgress:
            print("-----------------------------------")
            selected = selectOption(options, "Select an option and press ENTER: ")
            if selected == "S":
                # search product
                clear()
                retrievedProduct = searchProduct(DataBase)
                if retrievedProduct != None:
                    options = "SAQ"
                else:
                    options = "SQ"            
            if selected == "A":
                # add product to basket
                clear()
                result = addProduct(shoppingBasket, retrievedProduct)
                if result:
                    options = "SCQ"
                    retrievedProduct = None
            if selected == "Q":
                # quit
                answer = input("Quit: are you sure (s/n)").upper()
                if answer != "S":
                    selected = ""
                else:
                    clear()
                    print("Come back soon!")
            if selected == "C":
                # checkout
                shoppingBasket.state = State.InCheckout
                options = "1234Q"
                clear()
        elif shoppingBasket.state == State.InCheckout:
            print("---------PAYMENT-METHOD------------")
            print(shoppingBasket.payment)
            print("-----------------------------------")
            selected = selectOption(options, "Select a payment method: ")
            if selected == "1":
                number = input("Credit card number: ")
                payment = Card("Credit Card", shoppingBasket.getTotal(), number)
                clear()
            if selected == "2":
                email = input("Paypal Email: ")
                payment = Service("PayPal", shoppingBasket.getTotal(), email)
                clear()
            if selected == "3":
                code = input("Gift Voucher: ")
                payment = GiftVoucher("Gift voucher code", shoppingBasket.getTotal(), code)
                clear()
            if selected == "4":
                code = input("Promo Code: ")
                payment = PromoCode("Promo Code", shoppingBasket.getTotal(), code)
                clear() 
            validationError = payment.validInput()
            transactionApproved = payment.approveTransaction()
            # for testing purposes always returns True (approved)
            if selected == "Q":
                break
            if validationError:
                print(validationError)
                input("Press enter to continue...")
            elif transactionApproved:
                print("-----------------------------------")
                print("Payment approved.")
                input("press ENTER to continue...")
                shoppingBasket.state = State.Finished
                shoppingBasket.payment = payment
        else:
            print("---------PAYMENT-METHOD------------")
            print(shoppingBasket.payment)
            print("-----------------------------------")            
            input("Thank you for your purchase!")
            selected = "Q"

