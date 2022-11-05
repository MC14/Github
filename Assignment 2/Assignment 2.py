import random #imports random for it to be used within the class Product (random.randrange)
class Product: #Creates the class product, with the data given from the application & method month_statement
   
    def __init__(self,code,name,price,manu_cost,stock,month_units): #constructor methods that creates the object with all the inputs made before
        print("*** Morgan's Sample Stock Statement ***") #print simple statement
        print("Product Code:",code,) #prints code number
        print("Product Name:",name,) #prints the name 
 
        print("Sale Price:",price,"CAD") #prints the sale price
        print("Manufacture Cost:",manu_cost,"CAD") #prints the manufacture cost
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
        
        net_Profit = (total_Unit_Sold * price ) - (total_Manufactured * manu_cost) #creates a variable that calculates the net profit of the 12 months
        print(net_Profit) #prints net profit to show it
   
   
 

 
class Application: #creates a class that runs all the inputs in the program and then runs the Product class
    the_loop = 0 #sets the_loop to 0 in order to use while loops
    print("Welcome to Morgan's Magnificent Products") #print statement to show the start of the code
    while the_loop == 0: #creates a while loop that continues until the_loop does not equal zero
        code = input("Please enter your Product's code: ") #input statement to create the product's code
        code = int(code) #turns the variable into an int if able, if not will cause an error
        if code >= 100 and code <= 1000: #checks if the product code is in between 100 and 1000, if it is the code continues but if not, try again
            the_loop = 1 #turns variable the_loop to 1 in order to break the while loop and continues the code
        else: #if anything else, besides 100 and 1000
            print("Invalid Product Code, please try again") #print invalid code and try again
    the_loop = 0 #resets the_loop in order to do another while loop for the next input variable  
    name = input("Please enter the Name of your Product: ")
    while the_loop == 0:
        price = input("Please enter the Price of the Product: ")
        price = float(price) #turns the variable into a float
        if price > 0:
            the_loop = 1
        else:
            print("Invalid Price, please try again")
    the_loop = 0
    while the_loop == 0:
        manu_cost = input("Please enter the Manufacturing Cost: ")
        manu_cost = float(manu_cost) #turns the variable into a float
        if manu_cost > 0:
            the_loop = 1
        else:
            print("Invalid Manufacturing Cost, please try again")
    the_loop = 0
    while the_loop == 0:       
        stock = input("Please enter the amount of Stock of the Product: ")
        stock = int(stock)
        if stock > 0:
            the_loop = 1
        else:
            print("Invalid Stock, please try again")
    the_loop = 0
    while the_loop == 0:
        month_units = input("Please enter the amount of stock made in a month: ")
        month_units = int(month_units) #turns the variable into an interger
        if month_units > 0:
            the_loop = 1
        else:
            print("Invalid Monthly Units, please try again")
    app_Product = Product(code,name,price,manu_cost,stock,month_units) #creates an object using the class product and the inputs given from the application class
    app_Product.month_Statement(month_units,stock,price,manu_cost) #runs the Product class method using the object app_product and it's variables
    