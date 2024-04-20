import sys

# ----------------------------------------------Global dictionaries ------------------------------------------------------------
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


def prescription_required(product, product_info):
    product_list = product_info.get(product,(0, "n"))
    return product_list[1] == "y"

def calc_total_cost(price, qty):
    print(price, qty ,price*qty)
    return price*qty

def round_reward_points(rewardPoints):
    roundVal = rewardPoints- int(rewardPoints)
    print(roundVal)
    if (roundVal < 0.5):
        return int(rewardPoints)
    else: 
        return int(rewardPoints)+1
    
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
    print(" Total cost: "+ str(sum) +"(AUD)")
    print(" Earned reward: "+ str(rewards))

    (sum,rewards) = apply_discounts(sum, rewards)
    return rewards


def apply_discounts(sum,rewards):
    if rewards>=100:
        sum-=10
        rewards-=100
    return (sum, rewards)
def check_valid_products(products):
    for product in products:
        if not (product in product_info):
            return False        
    return True

def check_prescription_required(products):
    for product in products:
        (price,pres) = product_info[product]
        if pres == "y":
            return True
    return False

def prompt_quantities(num):
    quantity_list =[]
    while True:
        quantity_list = get_user_input("what quantities do you need? ")
        quantity_list =quantity_list.split(",")
        if(len(quantity_list) == num):
            flag = True
            for quantity in quantity_list:
                if quantity.isdigit() and int(quantity) > 0:
                    flag = True
                else:
                    flag = False
                    print("Entered invalid quantity.Enter a positive integer.")
                    break

            if flag:
                break     
        else:
            print("Invalid Quantity!")
    return quantity_list

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

# option 1
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

        product_list= product_list.split(",")

        if check_valid_products(product_list):
            break
    
    check_prescription_required(product_list)
    num_of_products = len(product_list)
    
    # Check if the product requires a prescription and handle accordingly
    prescription_answer=""
    quantity_list=[]
    while True:
        prescription_answer = get_user_input(f"One of your product requires a doctor's prescription. Do you have a prescription? (y/n)")
        if prescription_answer in ["y","n"]:
            if prescription_answer.lower() != 'y':
                print("The product requires a prescription by doctor.Please provide a prescription for purchasing it.")
                sys.exit()
            
            quantity_list = prompt_quantities(num_of_products)
            break
        else:
            print("Please enter a valid choice. Do you have a prescription (y/n)?")

    order= checkout_order(product_list,quantity_list)
    rewards= print_receipt(name,order)


    # Checks if new user or already existing user
    if( name in customers):
        customers[name] += rewards

        order_list[name] += order
    else:
        customers[name] = rewards

        order_list[name] = order
        print(customers)

# option 2
def add_update_product():
    product_info_input = get_user_input("Enter product information (name price dr_prescription): ")

    product_info_list = product_info_input.split(",")
    for product in product_info_list:
        product = product.split(" ")
        product_name = product[0]
        product_info[product_name] = (float(product[1]), product[2])

# option 3
def display_customers():
    print("Existing customers and their accumulated reward points:")
    for customer, reward_points in customers.items():
        print(f"{customer}: {reward_points}")

# option 4
def display_products():
    print("Existing products with their prices and prescription requirement:")
    for product, info in product_info.items():
        price, dr_prescription = info
        print(f"Product: {product}, Price: {price}, Doctor's Prescription Required: {'Yes' if dr_prescription == 'y' else 'No'}")

# option 5
def order_history():
    
    name = get_user_input("Enter the name to search up")
    orders = order_list[name]
    i=1 
    for order in orders:
        print("Order "+ str(i) + " "+ str([order[1]])+" BAAKI FORMAT")
        i+=1

# option 6
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
