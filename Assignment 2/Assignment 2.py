import random #imports random for it to be used within the class Product (random.randrange)
class Product: #Creates the class product, with the data given from the application & method month_statement
   
    def __init__(self,code,name,price,manu_cost,stock,month_units): #constructor methods that creates the object with all the inputs made before
        print("*** Morgan's Sample Stock Statement ***") #print simple statement
        print("Product Code:",code,) #prints code number
        print("Product Name:",name,) #prints the name 
 
        print("Sale Price:",price,"CAD") #prints the sale price
        print("Manufacture Cost:",manu_cost,"CAD") #prints the manufacture cpst
        print("Monthly Production:",month_units,"units (Approx.)") #print the monthly production given
   
    def month_Statement(self,month_units,stock,price,manu_cost): #creates a method with these parameters variables to estimate a net profit within 12 months.
        for month in range(1,12): #creates a for loop to act as a 12 month for the product
            print("Month",month,":") #print the month number given by the range
            print("Manufactured:",month_units,"units") #print the amount manufactured given by the product
            new_sold = random.randrange(-10,11) #using the random library create a range from -10 to 10 in order to act as the amount of product sold
            Sold = int(month_units) + new_sold #creates variable to show off the amount sold in each month
            print("Sold:",Sold,"units") #prints the created sold variable
            new_stock = int(stock) + (-new_sold) #creates variable to show off the new amount of stock in each month
            print("Stock:",new_stock,"units") #prints the created new_stock variable
            total_Manufactured = total_Manufactured + month_units #variable that keeps track of total amount of product manufactured through all the months
            total_Unit_Sold = total_Unit_Sold + new_sold #variable that keeps track of total amount of product sold through all the months
        
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
    