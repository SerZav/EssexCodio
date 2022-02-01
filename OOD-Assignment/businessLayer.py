import enum
import re
import datetime
from visualLayer import *
from dataLayer import *

class UserType(enum.Enum):
    # enumerator to simplify types of user
    Buyer = 0
    InternalSeller = 1
    ExternalSeller = 2
    Admin = 3

class State(enum.Enum):
    # Enumerator that describes the states of a shopping cart
    Cancelled = 0
    InProgress = 1
    InCheckout = 2
    Finished = 3

def formatAmount(amount):
    # function to format numbers into currency
    formatted = "£{:,.2f}".format(amount)
    return formatted    

class Order(object):
    """ Parent class for orders. It holds the order information
    and has the method to create an order, calling the
    Entity object to persist data.
    """

    def __init__(self):
        # order number is increased automatically when persisted
        self.orderNumber = 0
        self.date = datetime.datetime.now()
        self.amount = 0
        self.tax = 0
        self.orderLines = {}
        self.payment = None
        self.deliveryService = {}

    def createOrder(self, Entity):
        # The CreateOrder is abstracted in the Entity class
        # and it does not depend on this method.
        return Entity.CreateOrder(self)

    def getTotal(self):
        # calculate order total by calling the getLineTotal()
        # method of the object OrderLine
        result = 0
        for line in self.orderLines:            
            result += self.orderLines[line].getLineTotal()
        return result

    def getTotalFormatted(self):
        # special method to show the total with currency format
        return formatAmount(self.getTotal())

    def __str__(self):
        # str method can be used for reporting or debugging purposes
        # prints out the data of the object
        return "\norderNumber: {0}\ndate: {1}\namount: {2}\ntax: {3}"\
            .format(self.orderNumber, self.date, formatAmount(self.amount), \
            formatAmount(self.tax))


class ShoppingBasket(Order):
    """ Inherits from Order. It has special methods to
    manipulate an ongoing shopping basket, that the
    Order class does not has.
    """

    def __init__(self, state):
        # since we inherit from order, we can call
        # the parent and the add the new attribute state,
        # exclusive of the child
        Order.__init__(self)
        self.state = state

    def __str__(self):
        # overrides str method to include state
        # str method can be used for reporting or debugging purposes
        # prints out the data of the object
        strResult = ""
        # check if orderLines exist
        isCartEmpty = not bool(self.orderLines)
        if isCartEmpty:
            return "Empty"
        # Joins printing results of every Order Line
        for line in self.orderLines:
            strResult += self.orderLines[line]
        return strResult.rstrip("\n")

    def __radd__(self, other):
        # Special method to allow adding the output of self __str__ method
        # to a string.
        return other + str(self)    

    def addOrderLine(self, orderLine):
        # receives an orderLine object and add it to dictionary
        self.orderLines[orderLine.product.productId] = orderLine
        if (self.orderLines[orderLine.product.productId].quantity == 0):
            del self.orderLines[orderLine.product.productId]

    def addPayment(self, paymentMehod):
        # receives a paymentMethod object
        self.payment = paymentMehod


class OrderLine(object):
    """ Order lines of an Order """

    def __init__(self, product, quantity):
        self.orderNumber = 0
        self.product = product
        self.quantity = quantity

    def __str__(self):
        # str method can be used for reporting or debugging purposes
        # prints out the data of the object
        return "{0} / Price: {1} / Quantity: {2}\n"\
            .format(self.product.description, formatAmount(self.product.price), self.quantity)
    
    def getLineTotal(self):
        return self.product.price * self.quantity

    def __radd__(self, other):
        return other + str(self)


class Address(object):
    """ Address class that keeps address information """
 
    def __init__(self, city, street, building, number):
        self.city = city
        self.street = street
        self.building = building
        self.number = number

    def __str__(self):
        # Method used to print out the contents of the object
        # It can be used for reporting
        return "{0},{1},{2},{3}".format(self.city, self.street, self.building,\
            self.number)


class User(object):
    """ class that holds user information and credentials """

    def __init__(self, userId, userPassword, userType):
        # userId is conerted to lowercase
        # userPassword can be used for user login
        # but it is not implemented
        self.userId = userId.lower()
        self.userPassword = userPassword
        self.userType = userType
    
    def createUser(self, Entity):
        # The called method is abstracted in the Entity class
        # and it does not depend on this method.        
        return Entity.CreateUser(self)


class Customer(object):
    """ class that contains customer information  """

    def __init__(self, userId, name, homeAddress = None, 
    deliveryAddressList = None, phoneNumber = 0, cart = None):
        # this constructor holds one customer information
        # the customerId has been replaced by userId to 
        # increase readability

        # userId is conerted to lowercase
        self.userId = userId
        self.name = name
        self.homeAddress = homeAddress
        self.deliveryAddress = deliveryAddressList
        self.phoneNumber = phoneNumber
        self.cart = Order
    
    def createAccount(self, Entity):
        # The called method is abstracted in the Entity class
        # and it does not depend on this method.
        return Entity.CreateCustomer(self)
    
    def __str__(self):
        # str method can be used for reporting or debugging purposes
        # prints out the data of the object
        return "\nId: {0}\nName: {1}\nHomeAddress: {2}".format(self.userId, self.name,\
            self.homeAddress)

    def __eq__(self, other):
        # Compares the content between to instances of the object
        # instead of comparing the memory address.
        if other == None:
            # If the object to compare is empty, returns False
            return False
        if self.userId == other.userId and self.name == other.name and \
            self.homeAddress == other.homeAddress and \
            self.deliveryAddress == other.deliveryAddress and \
            self.phoneNumber == other.phoneNumber and \
            self.cart == other.cart:
            # compares every attribute and returns True if they are equal
            return True
        else:
            # if any attribute is different, returns False
            return False


class PaymentMethod(object):
    """ Payments. This is the parent class for
    other payment methods  """
    
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def approveTransaction(self):
        # This method must be overrided by inherited
        # classes to provide some functionality
        pass

    def validInput(self):
        # This method must be overrided by inherited
        # classes to provide some functionality
        pass

    def mask(self):
        # This method must be overrided by inherited
        # classes to provide some functionality
        pass

    def __str__(self):
        # This method must be overrided by inherited
        # classes to provide some functionality
        pass        

class Card(PaymentMethod):
    """ inherits from PaymentMethod """

    def __init__(self, description, amount, number):
        # since we inherit from PaymentMethod, we can call
        # the parent and the add the new attribute
        PaymentMethod.__init__(self, description, amount)
        self.number = number
    
    def approveTransaction(self):
        # this method can be used to connect
        # to the appropriate service
        # not implemented
        return True

    def validInput(self):
        # validate card format. For testing purposes must be a number of at least 8 digits
        if len(self.number) > 7 and self.number.isnumeric():
            return ""
        else:
            return "ERROR: Invalid card number (must have at least 8 numbers)"

    def mask(self):
        # masks the credit card number 
        return "****" + self.number[-4:]

    def __str__(self):
        # used for printing/reporting purposes
        return "{0} / Number: {1} / Amount: {2}"\
            .format(self.description, self.mask(), formatAmount(self.amount))


class Service(PaymentMethod):
    """ inherits from PaymentMethod """

    def __init__(self, description, amount, email):
        # since we inherit from PaymentMethod, we can call
        # the parent and the add the new attribute
        PaymentMethod.__init__(self, description, amount)
        self.email = email

    def approveTransaction(self):
        # this method overrides
        # to the appropriate service
        # not implemented
        return True

    def validInput(self):
        # validate email format with regular expressions
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.match(regex, self.email):
            return ""
        else:
            return "ERROR: invalid email"

    def mask(self):
        # masks the email
        return self.email[0:4] + "****" + self.email[-4:]

    def __str__(self):
        # used for printing/reporting purposes
        return "{0} / Number: {1} / Amount: {2}"\
            .format(self.description, self.mask(), formatAmount(self.amount))        


class GiftVoucher(PaymentMethod):
    """ inherits from PaymentMethod """

    def __init__(self, description, amount, code):
        # since we inherit from PaymentMethod, we can call
        # the parent and the add the new attribute
        PaymentMethod.__init__(self, description, amount)
        self.code = code
    
    def approveTransaction(self):
        # this method overrides
        # to the appropriate service
        # not implemented
        return True

    def validInput(self):
        # validate code format. For testing purposes must be a number of at least 8 digits
        if len(self.code) > 7 and self.code.isnumeric():
            return ""
        else:
            return "ERROR: Invalid Gift voucher number (must have at least 8 numbers)"

    def mask(self):
        return self.code

    def __str__(self):
        # used for printing/reporting purposes
        return "{0} / Number: {1} / Amount: {2}"\
            .format(self.description, self.mask(), formatAmount(self.amount))


class PromoCode(PaymentMethod):
    """ inherits from PaymentMethod """

    def __init__(self, description, amount, code):
        # since we inherit from PaymentMethod, we can call
        # the parent and the add the new attribute
        PaymentMethod.__init__(self, description, amount)
        self.code = code

    def mask(self):
        return self.code

    def validInput(self):
        # validate promo code format. For testing purposes must be a number of at least 8 digits
        if len(self.code) > 7 and self.code.isnumeric():
            return ""
        else:
            return "ERROR: Invalid code number (must have at least 8 numbers)"

    def approveTransaction(self):
        # this method overrides
        # to the appropriate service
        # not implemented
        return True

    def __str__(self):
        # used for printing/reporting purposes
        return "{0} / Number: {1} / Amount: {2}"\
            .format(self.description, self.mask(), formatAmount(self.amount))



class Product(object):
    """ Class that represents one product """

    def __init__(self, description, sellerId, price, stock = 0):
        self.productId = 0
        self.description = description
        self.sellerId = sellerId
        self.price = price
        self.stock = stock

    def createProduct(self, Entity):
        # The called method is abstracted in the Entity class
        # and it does not depend on this method.
        return Entity.CreateProduct(self)

    def searchProduct(self, Entity, searchParam):
        # if empty, returns None
        if not searchParam:
            return None
        # verify if searchParam is numeric to look for product code
        if searchParam.isnumeric():
            result = Entity.ReadProduct(int(searchParam))
            if result != None:
                return result
        # if product code not found or searchParam is text
        return Entity.ReadProductByText(searchParam)

    def __str__(self):
        # str method can be used for reporting or debugging purposes
        # prints out the data of the object
        return "Id: {0} / Description: {1} /  Price: {2} / Available: {3}"\
            .format(self.productId, self.description, formatAmount(self.price), \
            self.stock)


if __name__ == '__main__':
    DataBase = Entity()
