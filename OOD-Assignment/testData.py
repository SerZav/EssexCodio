from dataLayer import *

def LoadTestData(DataBase):
    # load test data in Database
    # creating the object and then
    # calling the method that will 
    # persist data on the DataBAse
    print("Loading test data...")
    newProduct = Product("chair", 1, 23.10, 5)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(1))
    newProduct = Product("desk", 1, 42.99, 2)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(2))
    newProduct = Product("lamp", 1, 9.99, 2)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(3))
    newProduct = Product("pencil", 1, 0.99, 100)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(4))
    newProduct = Product("scissors", 1, 2.99, 10)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(5))        
    newProduct = Product("marker", 1, 0.35, 5)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(6))        
    newProduct = Product("eraser", 1, 0.19, 10)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(7))        
    newProduct = Product("calculator", 1, 5.99, 5)
    newProduct.createProduct(DataBase)
    print(DataBase.ReadProduct(8))        
    print ("Loading test data Completed\n")
    input ("press enter to continue...")
