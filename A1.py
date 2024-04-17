import sys

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

# Function to get user input based on prompt sent to this function
def get_user_input(prompt):
    sys.stdout.write(prompt + ": ") 
    sys.stdout.flush() 
    return sys.stdin.readline().strip()  

####################################DOUBT################################

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
        return rewardPoints
    else: 
        return int(rewardPoints)+1
    
def print_receipt(name,product,price,qty,rewardPoints):
    print("---------------------------------------------------------")
    print("                     Receipt                             ")
    print("---------------------------------------------------------")
    print(" Name:"+ name)
    print(" Product: "+ product)
    print(" Unit Price: ",price," (AUD)")
    print(" Quantity: "+qty)
    print(" ---------------------------------------------------------")
    print(" Total cost: "+ str(price) +"(AUD)")
    print(" Earned reward: "+ str(rewardPoints))


# Customer name to be entered only in alphabets
while True:
    name = get_user_input("What's your name: ") 
    if name.isalpha():
        break
    else:
        print("Sorry,please enter a valid name.The entered name is invalid")

        
# Product entered should always be vaild
while True:
    product = get_user_input("What product do you want? ")
    if product in product_info:
        break
    else:
        print("You have entered an invaild product name. Enter a valid product name") 

# Check if the product requires a prescription and handle accordingly
if product_info[product][1] == "y":
        prescription_answer=""
quantity=0
while True:
    prescription_answer = get_user_input(f"Product '{product}' requires a doctor's prescription. Do you have a prescription? (y/n)")
    if prescription_answer in ["y","n"]:
        if prescription_answer.lower() != 'y':
            print("The product requires a prescription by doctor.Do provide a prescription for purchasing it.")
            sys.exit()
        
        while True:
            quantity = get_user_input("what quantity do you need? ")
            if quantity.isdigit() and int(quantity) > 0:
                break
            else:
                print("Entered invalid quantity.Enter a positive integer.")
                
        break
    else:
        print("Please enter a valid choice. Do you have a prescription (y/n)?")


price = calc_total_cost(product_info[product][0],int(quantity)) 
print("Total Cost price:" , price)

# Calculating the rewrd points earned from purchase

reward_points = round_reward_points(price) 
print("Reward points: ", reward_points)

print_receipt(name,product,price,quantity,reward_points)

# Checks if new user or already existing user
if( name in customers):
     customers[name] += reward_points
else:
     customers[name] = reward_points
     print(customers)



    