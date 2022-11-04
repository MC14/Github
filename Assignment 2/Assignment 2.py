import random
class Product:
   
    def __init__(self,code,name,price,manu_cost,stock,month_units):
        print("*** Morgan's Sample Stock Statement ***")
        print("Product Code:",code,)
        print("Product Name:",name,)
 
        print("Sale Price:",price,"CAD")
        print("Manufacture Cost:",manu_cost,"CAD")
        print("Monthly Production:",month_units,"units (Approx.)")
   
    def month_Statement(self,month_units,stock,price,manu_cost):
        for month in range(1,13):
            print("Month",month,":")
            print("Manufactured:",month_units,"units")
            new_sold = random.randrange(-10,11)
            Sold = int(month_units) + new_sold
            print("Sold:",Sold,"units")
            new_stock = int(stock) + (-new_sold)
            print("Stock:",new_stock,"units")
            total_Manufactured = total_Manufactured + month_units
            total_Unit_Sold = total_Unit_Sold + new_sold
        
        net_Profit = (total_Unit_Sold * price ) - (total_Manufactured * manu_cost)
        print(net_Profit)
   
   
 

 
class Application:
    the_loop = 0
    print("Welcome to Morgan's Magnificent Products")
    while the_loop == 0:
        code = input("Please enter your Product's code: ")
        code = int(code)
        if code >= 100 and code <= 1000:
            print(type(code))
            print("Hooray")
            the_loop == 1
        else:
            print("Invalid Product Code, please try again")
 
    loop = 0
    name = input("Please enter the Name of your Product: ")
    price = input("Please enter the Price of the Product: ")
    manu_cost = input("Please enter the Manufacturing Cost: ")
    stock = input("Please enter the amount of Stock of the Product: ")
    month_units = input("Please enter the amount of stock made in a month: ")
    app_Product = Product(code,name,price,manu_cost,stock,month_units)
    app_Product.month_Statement(month_units,stock,price,manu_cost)
    