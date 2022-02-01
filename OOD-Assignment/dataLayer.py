import inspect
import copy
from businessLayer import *


class Entity:
    """ abstract data layer """
    
    def __init__(self):
        # Creates an  instance of a memory object, but it can
        # contain a dataBase connection instead
        # dictionaries are used to store data
        self.CustomersDB = {}
        self.UsersDB = {}
        self.OrdersDB = {}
        self.ProductsDB = {}
        # some attributes are used as counters
        self.OrderId = 0
        self.ProductId = 0

    #CRUD customer operations
    def CreateCustomer(self, Customer):
        # data type validation
        # verify if it is an object
        hasModule = getattr(Customer, '__module__', None) == 'businessLayer'
        # verify if it is of type Customer
        isCustomerClass = hasModule and type(Customer).__name__ == 'Customer'
        if not isCustomerClass:
            raise ValueError("parameter is not an instance of Customer")
        # check if the user exists  
        if (self.ReadCustomer(Customer.userId) == None):
            # if it does not exist, create Customer
            self.CustomersDB[Customer.userId] = Customer
            return True
        else:
            # else return False
            return False

    def ReadCustomer(self, userId):
        # data type validation
        if type(userId) is not str or not userId:
            raise ValueError("userId must be a non-empty string")        # check if Customer exists
        # if exists returns the Customer
        # if not, returns None
        if userId in self.CustomersDB:
            return self.CustomersDB[userId]
        else:
            return None

    def UpdateCustomer(self, Customer):
        # data type validation
        # verify if it is an object
        hasModule = getattr(Customer, '__module__', None) == 'businessLayer'
        # verify if it is of type Customer
        isCustomerClass = hasModule and type(Customer).__name__ == 'Customer'
        if not isCustomerClass:
            raise ValueError("parameter is not an instance of Customer")
        # check if record exists
        if (self.ReadCustomer(Customer.userId) != None):
            # if exists, update record
            self.CustomersDB[Customer.userId] = Customer
            return True
        else:
            # else return False
            return False

    def DeleteCustomer(self, userId):
        # data type validation
        if type(userId) is not str or not userId:
            raise ValueError("userId must be a non-empty string")
        # check if record exists
        recordExists = self.ReadCustomer(userId) != None
        if (recordExists):
            # if exist, delete it and return True
            del self.CustomersDB[userId]
            return True
        else:
            # else return False
            return False

    #CRUD User operations
    def CreateUser(self, User):
        # check if the user exists        
        if (self.ReadUser(User.userId) == None):
            # if it does not exist, create user
            self.UsersDB[User.userId] = User
            return True
        else:
            # else return False
            return False

    def ReadUser(self, userId):
        # check if User exists
        if userId in self.UsersDB:
            # if it exists, return object User
            return self.UsersDB[userId]
        # else return None
        return None

    #CRUD order operations
    def CreateOrder(self, Order):
        # data type validation
        # verify if it is an object
        hasModule = getattr(Order, '__module__', None) == 'businessLayer'
        # verify if class is of type 'Order'
        isOrderClass = hasModule and type(Order).__name__ == 'Order'
        if not isOrderClass:
            raise ValueError("parameter is not an instance of Order")
        # check if the user exists  
        self.OrderId += 1
        # persist the object in DB and update Id
        self.OrdersDB[self.OrderId] = copy.deepcopy(Order)
        self.OrdersDB[self.OrderId].orderNumber = self.OrderId
        return self.OrderId

    def ReadOrder(self, orderNumber):
        # data type validation
        if type(orderNumber) is not int or not orderNumber:
            raise ValueError("orderNumber must be a integer > 0")        
        # check if Order exists
        # if exists returns the Order
        # if not, returns None
        if orderNumber in self.OrdersDB:
            return self.OrdersDB[orderNumber]
        else:
            return None

    #CRUD Product operations
    def CreateProduct(self, Product):
        # check if the product exists        
        if (self.ReadProduct(Product.productId) == None):
            # if it does not exist, create product
            self.ProductId += 1
            self.ProductsDB[self.ProductId] = copy.deepcopy(Product) 
            self.ProductsDB[self.ProductId].productId = self.ProductId 
            return True
        else:
            # else return False
            return False

    def ReadProduct(self, productId):
        # check if Product exists
        if productId in self.ProductsDB:
            # if it exists, return object Product
            return self.ProductsDB[productId]
        # else return None
        return None

    def ReadProductByText(self, text):
        # data type validation
        if type(text) is not str or not text:
            raise ValueError("Text to search must be a non-empty string")        
        # check if Order exists
        # if exists returns the Order
        # if not, returns None
        for productCode in self.ProductsDB:
            # look for the text in description
            if text in self.ProductsDB[productCode].description:
                return self.ProductsDB[productCode]
        # text not found
        return None