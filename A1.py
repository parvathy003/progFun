import sys

reward_points = 0
def get_user_input(prompt): # Function to get user input based on prompt sent to this function
    sys.stdout.write(prompt + ": ")  # Display prompt
    sys.stdout.flush()  # Ensure prompt is displayed immediately
    return sys.stdin.readline().strip()  # Read user input and strip newline character

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
print("Hello,", name)


product = get_user_input("What product do you want? ")
print("Product:" ,product)

quantity = get_user_input("what quantity do you need? ")
print("quantity:" , quantity)

price = calc_total_cost(12,int(quantity))
print("Total Cost price:" , price)

reward_points+= round(price)
print("Reward points: ", reward_points)

print_receipt(name,product,price,quantity,reward_points)