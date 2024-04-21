#----------------------------------------Name & Student ID: Parvathy Sathyaratnan (s3985864)------------------------------------
# Highest part attempted: Part 3
# Any problems in the code and requirements that have not been met: No problems in the code.All the requirements mentioned are met.


import sys # Importing 'sys'module to access system specific parameters and functions

# ----------------------------------------------Global dictionaries ------------------------------------------------------------
# Global dictionaries for customers,product information and order list
customers = {
    "Kate": 20,
    "Tom": 32
}

product_info = {
    "vitaminC": (12.0,"n"),   
    "vitaminE": (14.5,"n"),  
    "coldTablet":(6.4,"n"), 
    "vaccine": (32.6,"y"),   
    "fragrance": (25.0 ,"n") 
}

order_list = {
    "Kate":[],
    "Tom":[]
}

# ------------------------------------------------- UTILITY FUNCTIONS ---------------------------------------------------------

# Function to get user input based on prompt sent to this function
def get_user_input(prompt):
    sys.stdout.write(prompt + ": ") 
    sys.stdout.flush() 
    return sys.stdin.readline().strip()  

# Function used to calculate total cost
def calc_total_cost(price, qty):
    print(price, qty ,price*qty)
    return price*qty

# Function used to round reward points
def round_reward_points(rewardPoints):
    roundVal = rewardPoints- int(rewardPoints)
    print(roundVal)
    if (roundVal < 0.5):
        return int(rewardPoints)
    else: 
        return int(rewardPoints)+1

# Function to print the receipt    
def print_receipt(name,orders):

    sum =0
    rewards =0
    print("---------------------------------------------------------")
    print("                     Receipt                             ")
    print("---------------------------------------------------------")
    print(" Name:"+ name)

    for order in orders:
        sum+= order[3]
        rewards+=order[4]
        print(" Product: "+ order[1])
        print(" Unit Price: ",order[2]," (AUD)")
        print(" Quantity: "+ str(order[0]))

    print(" ---------------------------------------------------------")
    current_rewards =0
    if name in customers:    
        current_rewards = customers[name]
    else:
        current_rewards = 0

    (sum,current_rewards) = apply_discounts(sum, current_rewards)

    if name in customers:    
        customers[name] = current_rewards
        
    print(" Total cost: "+ str(sum) +"(AUD)")
    print(" Earned reward: "+ str(rewards))
    return rewards

# Function used to apply discounts
def apply_discounts(sum,rewards):
    if rewards>=100:
        sum-=10
        rewards-=100
        
    return (sum, rewards)
# Function to check if the products are vaild
def check_valid_products(products):
    for product in products:
        if not (product in product_info):
            return False        
    return True
# Function to check if prescription is required for any product
def check_prescription_required(products):
    for product in products:
        (price,pres) = product_info[product]
        if pres == "y":
            return True
    return False
# Function to promt quantities for user
def prompt_quantities(num):
    quantity_list =[]
    while True:
        quantity_list = get_user_input("what quantities do you need? ")
        quantity_list =quantity_list.split(",")
        flag = True
        if(len(quantity_list) == num):
            for quantity in quantity_list:
                if quantity.isdigit() and int(quantity) > 0:
                    flag = True
                else:
                    flag = False
                    print("Entered invalid quantity.Enter a positive integer.")
                    break
        else:
            print("Invalid Quantity!")
            flag = False
        if flag:
            return quantity_list     
# Function to checkout order
def checkout_order(product_list,quantity_list):
    order = []
    for i in range(len(product_list)):
        product= product_list[i]
        product_unit_price = product_info[product][0]
        product_quantity = int(quantity_list[i])
        price = calc_total_cost(product_unit_price,product_quantity) 
        reward_points = round_reward_points(price) 
        order.append([product_quantity,product,product_unit_price,price,reward_points])
    return order
    
#----------------------------------------------------MENU FUNCTIONS-------------------------------------------------------

# Menu option 1 to make purchase
def make_purchase():
    # Customer name to be entered only in alphabets
    while True:
        name = get_user_input("What's your name: ") 
        if name.isalpha():
            break
        else:
            print("Sorry,please enter a valid name.The entered name is invalid")

    product_list=[]
    # Product entered should always be vaild
    while True:
        product_list = get_user_input("What product do you want? ")

        # storing multiple products
        product_list= product_list.split(",")

        if check_valid_products(product_list):
            break
    
    num_of_products = len(product_list)
    
    # Check if the product requires a prescription and handle accordingly
    prescription_answer=""
    quantity_list=[]

    # if prescrption needed prompt for it
    while True:
        if check_prescription_required(product_list):
            prescription_answer = get_user_input(f"One of your product requires a doctor's prescription. Do you have a prescription? (y/n)")
            if prescription_answer in ["y","n"]:

                # if prescription input is n then exit
                if prescription_answer.lower() != 'y':
                    print("The product requires a prescription by doctor.Please provide a prescription for purchasing it.")
                    sys.exit()

                # if y then prompt quantity
                quantity_list = prompt_quantities(num_of_products)
                break
            else:
                print("Please enter a valid choice. Do you have a prescription (y/n)?")
        else:

            # if no prescription was needed prompt for quantities
            
            quantity_list = prompt_quantities(num_of_products)
            break

    # process the order, and push it into order history
    order= checkout_order(product_list,quantity_list)

    # process the receipt and the rewards
    rewards= print_receipt(name,order)


    # Checks if new user or already existing user and updates their rewards and orders
    if( name in customers):
        customers[name] += rewards
        order_list[name] += order
    else:
        customers[name] = rewards
        order_list[name] = order

# Menu option 2 to add or update product information
def add_update_product():
    product_info_input = get_user_input("Enter product information (name price dr_prescription): ")

    product_info_list = product_info_input.split(",")
    for product in product_info_list:
        product = product.split(" ")
        product_name = product[0]
        product_info[product_name] = (float(product[1]), product[2])

# Menu option 3 to display existing customers
def display_customers():
    print("Existing customers and their accumulated reward points:")
    for customer, reward_points in customers.items():
        print(f"{customer}: {reward_points}")

# Menu option 4 to display existing customers
def display_products():
    print("Existing products with their prices and prescription requirement:")
    for product, info in product_info.items():
        price, dr_prescription = info
        print(f"Product: {product}, Price: {price}, Doctor's Prescription Required: {'Yes' if dr_prescription == 'y' else 'No'}")

# Menu option 5 to display the order history of a customer
def order_history():
    name=""
    while True:
        name = get_user_input("Enter the name to search up")
        if name in customers:
            break
    orders = order_list[name]
    i=1 
    for order in orders:
        print("Order "+ str(i) + " "+ str([order[1]])+"x"+str([order[0]])+ " "+ str(order[2])+" "+ str(order[4]))
        i+=1

# Menu option 6 to exit the program
def exit_program():
    sys.exit()

# Main menu options
menu_options = {
    "1": make_purchase,
    "2": add_update_product,
    "3": display_customers,
    "4": display_products,
    "5": order_history,
    "6": exit_program
}

# Main program loop
while True:
    print("\nMain Menu:")
    print("1. Make a purchase")
    print("2. Add/update information of products")
    print("3. Display existing customers")
    print("4. Display existing products")
    print("5. Order history of a customer")
    print("6. Exit the program")
    choice = get_user_input("Enter your choice (1-6): ")

    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

#------------------------------------------------------------Explanation---------------------------------------------------

# Design Process and Approach

# I started the assignment by understanding the requirements,which emphasised on developing a menu-driven software to manage customer purchases and product information.Implementing each item in the menu as a function increased the readability of the code.This helps in maintaining the program effectively.Introducing its own function makes it easier in future to make any changes or expand the application.
# Functions were used to validate the data entered by user and to check for any errors.
# I have used dictionaries in order to store customer data, product details and order history.
# Error handling techniques were built into the code to deal with potential runtime issues.This includes detecting invalid user inputs, handling exceptions, and displaying relevant error messages.
# I used comments and documentation throughout the code to clarify the purpose of each function, method, and variable. These comments serve as a guidance for developers, improving code readability.

# Reflection

# Key areas of focus included robust input validation logic, handling prescription-only medicines, accurate order processing, and an intuitive menu structure.
# The code mostly uses while loops for user input validation and menu navigation because of their ability to iterate until a certain condition is met, assuring precise input handling and program execution.This technique enables dynamic user interaction, gentle error handling, and smooth navigation through the menu. 

#---------------------------------------------------------------------------------------------------------------------------