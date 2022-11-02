class Product:
    def __init__(self,code,name,price,manu_cost,stock,month_units):
        print("*** Morgan's Sample Stock Statement ***")
        print("Product Code:",code,)
        print("Product Name:",name,)
 
        print("Sale Price:",price,"CAD")
        print("Manufacture Cost:",manu_cost,"CAD")
        print("Monthly Production:",month_units,"units (Approx.)")
   
   
 
the_loop = False
 
class Application:
 
   
    print("Welcome to Morgan's Magnificent Products")
    while the_loop == False:
        code = input("Please enter your Product's code: ")
        code = int(code)
        if code >= 100 and code <= 1000:
            the_loop == True
        else:
            print("Invalid Product Code, please try again")
 
    loop = 0
    name = input("Please enter the Name of your Product: ")
    price = input("Please enter the Price of the Product: ")
    manu_cost = input("Please enter the Manufacturing Cost: ")
    stock = input("Please enter the amount of Stock of the Product: ")
    month_units = input("Please enter the amount of stock made in a month: ")
    App_product = Product(code,name,price,manu_cost,stock,month_units)