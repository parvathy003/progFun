import sys

customers = {
    "Kate": 20,
    "Tom": 32
}

product_info = {
    "vitaminC": 12.0,   
    "vitaminE": 14.5,   
    "coldTablet": 6.4,  
    "vaccine": 32.6,    
    "fragrance": 25.0   
}
def get_user_input(prompt): # Function to get user input based on prompt sent to this function
    sys.stdout.write(prompt + ": ") 
    sys.stdout.flush() 
    return sys.stdin.readline().strip()  

# Example usage:

def calc_total_cost(price, qty):
    print(price, qty ,price*qty)
    return price*qty

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



name = get_user_input("What's your name: ")

product = get_user_input("What product do you want? ")

quantity = get_user_input("what quantity do you need? ")

price = calc_total_cost(12,int(quantity))
print("Total Cost price:" , price)

reward_points = round(price)
print("Reward points: ", reward_points)

print_receipt(name,product,price,quantity,reward_points)

# Checks if new user or already existing user
if( name in customers):
    customers[name] += reward_points
else:
    customers[name] = reward_points
print(customers)