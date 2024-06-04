
#Parvathy Sathyaratnan
import sys
class Customer:
    def __init__(self, ID, name, reward):
        self.ID = ID
        self.name = name
        self.reward = reward

    def get_reward(self):
        pass

    def get_discount(self):
        pass

    def update_reward(self):
        pass

    def display_info(self):
        pass

class BasicCustomer(Customer):
    def __init__(self, ID, name, reward, reward_rate=1.0):
        super().__init__(ID, name, reward)
        self.reward_rate = reward_rate

    def get_reward(self, total_cost):
        return round(total_cost * self.reward_rate)

    def update_reward(self, value):
        self.reward += value

    def display_info(self):
        print(f"ID: {self.ID}, Name: {self.name}, Reward Rate: {self.reward_rate}")

    def set_reward_rate(self, rate):
        self.reward_rate = rate

class VIPCustomer(Customer):
    def __init__(self, ID, name, reward, reward_rate=1.0, discount_rate=0.08):
        super().__init__(ID, name, reward)
        self.reward_rate = reward_rate
        self.discount_rate = discount_rate

    def get_discount(self, total_cost):
        return total_cost * self.discount_rate

    def get_reward(self, total_cost):
        return round((total_cost - self.get_discount(total_cost)) * self.reward_rate)

    def update_reward(self, value):
        self.reward += value

    def display_info(self):
        print(f"ID: {self.ID}, Name: {self.name}, Reward Rate: {self.reward_rate}, Discount Rate: {self.discount_rate}")

    def set_reward_rate(self, rate):
        self.reward_rate = rate

    def set_discount_rate(self, rate):
        self.discount_rate = rate

class Product:
    def __init__(self, ID, name, price):
        self.ID = ID
        self.name = name
        self.price = price

    def display_info(self):
        print(f"ID: {self.ID}, Name: {self.name}, Price: {self.price}")


