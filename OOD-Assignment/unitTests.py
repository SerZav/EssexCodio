import unittest
from businessLayer import *

class OOSI(unittest.TestCase):
    # testing classes to manipulate objects
    def test_businessLayer_User_operations(self):
        DataBase = Entity()
        newUser = User("sergod", "abc", UserType.Buyer)
        
        # use class to create new user
        self.assertEqual(newUser.createUser(DataBase), True, "Expected result: True")   

        # try to repeat new user should return False
        self.assertEqual(newUser.createUser(DataBase), False, "Expected result: False")   

    def test_businessLayer_Customer_operations(self):
        DataBase = Entity()
        newCustomer = Customer("sergod","sergio", None, None, 645111000)  
        
        # use class to create new Customer
        self.assertEqual(newCustomer.createAccount(DataBase), True, "Expected result: True")   

        # try to repeat new user should return False
        self.assertEqual(newCustomer.createAccount(DataBase), False, "Expected result: False")               


    #Testing CRUD operations directly in the dataLayer
    def test_dataLayer_User_CRUD(self):
        #Create database instance
        DataBase = Entity()

        #Testing User CRUD operations
        newUser = User("sergod","123", UserType.Buyer)

        #test insert new user
        self.assertEqual(DataBase.CreateUser(newUser), True, "Expected result: True")

        #test insert repeated user
        self.assertEqual(DataBase.CreateUser(newUser), False, "Expected result: False")

    def test_dataLayer__Customer_CRUD(self):
        #Create database instance
        DataBase = Entity()

        #Create user and Customer
        newUser = User("sergod","123", UserType.Buyer)
        homeAddress = Address("Madrid","Gran Via","2","1")
        deliveryAddress = Address("Alicante","Belgica","17","12")
        newCustomer = Customer(newUser.userId, "Sergio Zavarce", homeAddress,
            deliveryAddress, 635111000)

        #test insert Customer
        self.assertEqual(DataBase.CreateCustomer(newCustomer), True, "Expected result: True")

        #test insert repeated Customer
        self.assertEqual(DataBase.CreateCustomer(newCustomer), False, "Expected result: False")

        #test delete Customer
        self.assertEqual(DataBase.DeleteCustomer(newUser.userId), True, "Expected result: True")

        #test delete non-existent Customer
        self.assertEqual(DataBase.DeleteCustomer(newUser.userId), False, "Expected result: False")

        #test read Customer
        DataBase.CreateCustomer(newCustomer)
        testCustomer2 = Customer(newUser.userId, "Sergio Zavarce", homeAddress,
            deliveryAddress, 635111000)
        self.assertEqual(DataBase.ReadCustomer(newUser.userId), testCustomer2,
            "Expected result: {0}".format(testCustomer2))        

        #test read Customer not found
        self.assertEqual(DataBase.ReadCustomer("non-existent"), None, "Expected result: None")
        
        #test update Customer
        DataBase.CreateCustomer(newCustomer)
        testCustomer3 = Customer(newUser.userId, "Luis Zavarce", homeAddress,
            deliveryAddress, 635111000)
        DataBase.UpdateCustomer(testCustomer3)
        self.assertEqual(DataBase.ReadCustomer(newUser.userId), testCustomer3,
             "Expected result: {0}".format(testCustomer3))


    def test_dataLayer__Customer_CRUD_DataValidation(self):
        #Create database instance
        DataBase = Entity()   
        newUser = User("sergod","123", UserType.Buyer)

        #test insert data type validation
        self.assertRaises(ValueError, DataBase.CreateCustomer, 1)
        self.assertRaises(ValueError, DataBase.CreateCustomer, None)
        self.assertRaises(ValueError, DataBase.CreateCustomer, newUser)

        #test read data type validation
        self.assertRaises(ValueError, DataBase.ReadCustomer, 1)
        self.assertRaises(ValueError, DataBase.ReadCustomer, None)
        self.assertRaises(ValueError, DataBase.ReadCustomer, "")        

        #test update data type validation
        self.assertRaises(ValueError, DataBase.UpdateCustomer, 1)
        self.assertRaises(ValueError, DataBase.UpdateCustomer, None)
        self.assertRaises(ValueError, DataBase.UpdateCustomer, "")

        #test delete data type validation
        self.assertRaises(ValueError, DataBase.DeleteCustomer, 1)
        self.assertRaises(ValueError, DataBase.DeleteCustomer, None)
        self.assertRaises(ValueError, DataBase.DeleteCustomer, "")        

if __name__ == "__main__":
    unittest.main()