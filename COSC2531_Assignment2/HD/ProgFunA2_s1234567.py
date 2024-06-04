# Name:
# Student ID: s1234567
# Highest Level Attempted: HD
# Known Issues: None

import sys
from datetime import datetime

class Customer:
    """
    Base class representing a customer.
    This class serves as a template for different types of customers. 
    It contains primary attributes and methods related to customer information and rewards.
    """
    def __init__(self, ID, name, reward):
        """
        Initialize the customer with ID, name, and reward points.
        
        ID: Unique identifier for the customer.
        name: Name of the customer.
        reward: Reward points accumulated by the customer.
        """
        self.ID = ID
        self.name = name
        self.reward = reward

    def update_reward(self, value):
        """
        Update reward points by adding the given value.
        This method increases the customer's reward points by the specified value.
        """
        self.reward += value

    def redeem_rewards(self, reward_points):
        """
        Redeem rewards for a discount. 10 reward points = $1 discount.
        This method converts reward points into a discount and subtracts the redeemed points from the customer's total.
        """
        discount = reward_points * 0.1  
        self.reward -= reward_points
        return discount

    def display_info(self):
        """
        Display customer information.
        This method is intended to be overridden in subclasses to show customer details.
        """
        pass

# Exception classes for error handling
class InvalidNameException(Exception):
    """Exception raised for invalid customer names."""
    pass

class InvalidProductException(Exception):
    """Exception raised for invalid product names or IDs."""
    pass

class InvalidQuantityException(Exception):
    """Exception raised for invalid product quantities."""
    pass

class InvalidPrescriptionException(Exception):
    """Exception raised for missing required prescriptions."""
    pass

class BasicCustomer(Customer):
    """
    Class representing a basic customer.
    This class inherits from the Customer class and adds specific functionality for basic customers.
    """
    def __init__(self, ID, name, reward, reward_rate=1.0):
        """
        Initialize a basic customer with reward rate.
        
        reward_rate: Multiplier used to calculate rewards based on total cost.
        """
        super().__init__(ID, name, reward)
        self.reward_rate = reward_rate

    def get_reward(self, total_cost):
        """
        Calculate reward based on total cost and reward rate.
        This method returns the reward points earned for a given purchase amount.
        """
        return round(total_cost * self.reward_rate)

    def update_reward(self, value):
        """Update reward points by adding the given value."""
        self.reward += value

    def display_info(self):
        """
        Display basic customer information.
        This method prints the customer's ID, name, and reward points.
        """
        print(f"ID: {self.ID}, Name: {self.name}, Reward: {self.reward}")

    @classmethod
    def set_reward_rate(cls, rate):
        """"
        Set the reward rate for all basic customers.
        This class method updates the reward rate multiplier for all instances of BasicCustomer.
        """
        cls.reward_rate = rate

class VIPCustomer(Customer):
    """
    Class representing a VIP customer.
    This class inherits from the Customer class and adds specific functionality for VIP customers.
    """
    reward_rate = 1.0
    def __init__(self, ID, name, reward, discount_rate=0.08):
        """
        Initialize a VIP customer with discount rate.
        
        discount_rate: Percentage discount applied to the total cost for VIP customers.
        """
        super().__init__(ID, name, reward)
        self.discount_rate = discount_rate

    def get_discount(self, total_cost):
        """
        Calculate discount based on total cost and discount rate.
        This method returns the discount amount for a given purchase amount.
        """
        return total_cost * self.discount_rate

    def get_reward(self, discounted_cost):
        """
        Calculate reward based on discounted cost.
        This method returns the reward points earned after applying the discount.
        """
        return round(discounted_cost * VIPCustomer.reward_rate)

    def update_reward(self, value):
        """Update reward points by adding the given value."""
        self.reward += value 

    def display_info(self):
        """
        Display VIP customer information.
        This method prints the customer's ID, name, discount rate, and reward points.
        """
        print(f"ID: {self.ID}, Name: {self.name}, Discount Rate: {self.discount_rate}, Reward: {self.reward}")
        
    @classmethod
    def set_reward_rate(cls, rate):
        """
        Set the reward rate for all VIP customers.  
        This class method updates the reward rate multiplier for all instances of VIPCustomer.
        """
        cls.reward_rate = rate

    def set_discount_rate(self, rate):
        """
        Set the discount rate for this VIP customer.
        This method updates the discount rate for an individual VIP customer.
        """
        self.discount_rate = rate

class Product:
    """
    Class representing a product.
    This class contains attributes and methods related to product information.
    """
    def __init__(self, ID, name, price, prescription_required='n'):
        """
        Initialize a product with ID, name, price, and prescription requirement.
        
        prescription_required: Indicates whether a doctor's prescription is needed ('y-YES' or 'n-NO').
        """
        self.ID = ID
        self.name = name
        self.price = price
        self.prescription_required = prescription_required

    def display_info(self):
        """
        Display product information.
        This method prints the product's ID, name, price, and prescription requirement.
        """
        print(f"product_ID: {self.ID}, product_name: {self.name}, unit_price: {self.price}, dr_prescription: {self.prescription_required}")

class Bundle:
    """
    Class representing a bundle of products.
    This class contains attributes and methods related to bundled product information.
    """
    def __init__(self, ID, name, component_ids, products):
        """
        Initialize a bundle with ID, name, component IDs, and products.
        
        component_ids: List of product IDs included in the bundle.
        products: List of product objects included in the bundle.
        """
        self.ID = ID
        self.name = name
        self.component_ids = component_ids  
        self.products = products  
        self.price = self.calculate_price()
        self.prescription_required = self.check_prescription_requirement()

    def calculate_price(self):
        """
        Calculate the bundle price as 80% of the total price of individual products.
        This method computes the discounted price for the bundle.
        """
        total_price = sum(product.price for product in self.products)
        return round(total_price * 0.8, 1)

    def check_prescription_requirement(self):
        """
        Check if any product in the bundle requires a doctor's prescription.
        This method determines if a prescription is needed based on the products in the bundle.
        """
        return 'y' if any(product.prescription_required == 'y' for product in self.products) else 'n'

    def display_info(self):
        """
        Display bundle information.
        This method prints the bundle's ID, name, price, components, and prescription requirement.
        """
        component_info = ', '.join(self.component_ids)
        print(f"product_ID: {self.ID}, product_name: {self.name}, unit_price: {self.price:.1f}, Components: {component_info}, dr_prescription: {self.prescription_required}")

class Order:
    """
    Class representing an order.
    This class contains attributes and methods related to order information.
    """
    def __init__(self, customer, items):
        """
        Initialize an order with a customer and items.
        
        items: List of tuples (product, quantity) representing the products and their quantities.
        """
        self.customer = customer
        self.items = items  

    def compute_cost(self):
        """
        Compute original cost, discount, final cost, and reward for the order.
        This method calculates the total cost, applies any discounts, and computes reward points.
        """
        original_cost = sum(product.price * quantity for product, quantity in self.items)
        discount = 0
        if isinstance(self.customer, VIPCustomer):
            discount = self.customer.get_discount(original_cost)
        final_cost = original_cost - discount

        # Allow redeeming rewards for additional discount
        additional_discount = 0
        if self.customer.reward > 0:
            print(f"Customer has {self.customer.reward} reward points.")
            while True:
                redeem = input("Redeem rewards for additional discount? (y/n): ").lower()
                if redeem == 'y':
                    try:
                        reward_points = int(input(f"Enter reward points to redeem (max {self.customer.reward}): "))
                        if reward_points < 0 or reward_points > self.customer.reward:
                            raise ValueError("Invalid number of reward points.")
                        additional_discount = self.customer.redeem_rewards(reward_points)
                        break
                    except ValueError as e:
                        print(e)
                elif redeem == 'n':
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

        final_cost -= additional_discount
        reward = self.customer.get_reward(final_cost)
        return original_cost, discount + additional_discount, final_cost, reward
    
class Records:
    """
    Class for managing customer and product records.
    This class handles reading from and writing to files, and storing customer and product data.
    """
    def __init__(self):
        """Initialize records for customers, products, and orders."""
        self.customers = []
        self.products = []
        self.orders = []  # Add this line to initialize the orders list

    def read_customers(self, file_name):
        """
        Read customers from a file and add them to the list.
        This method reads customer data from the specified file, processes each line to create customer objects,
        and appends them to the customers list.
        """
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                try:
                    if parts[0].startswith('B') and len(parts) == 4:
                        customer = BasicCustomer(parts[0], parts[1], int(parts[3]), float(parts[2]))
                    elif parts[0].startswith('V') and len(parts) == 5:
                        customer = VIPCustomer(parts[0], parts[1], int(parts[4]), float(parts[3]))
                    else:
                        print(f"Skipping invalid line in {file_name}: {line.strip()}")
                        continue
                    self.customers.append(customer)
                except (IndexError, ValueError) as e:
                    print(f"Error processing line in {file_name}: {line.strip()}. Error: {e}")

    def save_customers(self):
        """
        Save the updated customer data to the customers.txt file.
        This method writes the current list of customers to a file, preserving their updated information.
        """
        with open('customers.txt', 'w') as file:
            for customer in self.customers:
                if isinstance(customer, BasicCustomer):
                    file.write(f"{customer.ID},{customer.name},{customer.reward_rate},{customer.reward}\n")
                elif isinstance(customer, VIPCustomer):
                    file.write(f"{customer.ID},{customer.name},{customer.reward_rate},{customer.discount_rate},{customer.reward}\n")

    def read_products(self, file_name):
        """
        Read products and bundles from a file and add them to the list.
        This method reads product and bundle data from the specified file, processes each line to create product or bundle objects,
        and appends them to the products list.
        """
        products_to_add = []
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4 and parts[3] in ['y', 'n']:
                    # Regular product
                    try:
                        product = Product(parts[0].strip(), parts[1].strip(), float(parts[2].strip()), parts[3].strip())
                        self.products.append(product)
                    except ValueError as e:
                        print(f"Error processing line in {file_name}: {line.strip()}. Error: {e}")
                elif len(parts) > 2 and parts[0].startswith('B'):
                    # Add bundles to be processed later
                    products_to_add.append(parts)
                else:
                    print(f"Skipping invalid line in {file_name}: {line.strip()}")

        for parts in products_to_add:
            # Bundle
            try:
                component_ids = parts[2:]
                components = [product for product in self.products if product.ID in component_ids]
                if len(components) == len(component_ids):
                    bundle = Bundle(parts[0].strip(), parts[1].strip(), component_ids, components)
                    self.products.append(bundle)
                else:
                    print(f"Skipping invalid bundle line in {file_name}: {line.strip()} - Component IDs not found")
            except ValueError as e:
                print(f"Error processing line in {file_name}: {line.strip()}. Error: {e}")

    def read_orders(self, file_name):
        """
        Read orders from a file and add them to the list.
        This method reads order data from the specified file, processes each line to create order objects,
        and appends them to the orders list.
        """
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    customer_id_or_name = parts[0]
                    total_cost = float(parts[-3])
                    earned_rewards = int(parts[-2])
                    date = parts[-1]
                    items = []
                    i = 1
                    while i < len(parts) - 3:
                        product_id_or_name = parts[i]
                        quantity = int(parts[i + 1])
                        product = self.find_product(product_id_or_name)
                        if product:
                            items.append((product, quantity))
                        i += 2
                    customer = self.find_customer(customer_id_or_name)
                    if customer:
                        customer.update_reward(earned_rewards)
                        order = {
                            'customer': customer,
                            'items': items,
                            'total_cost': total_cost,
                            'earned_rewards': earned_rewards,
                            'date': date
                        }
                        self.orders.append(order)
        except Exception as e:
            print("Cannot load the order file")
            print(e)

    def find_customer(self, value):
        """
        Find a customer by ID or name.
        This method searches the customers list for a customer with a matching ID or name.
        """
        value = value.lower()
        for customer in self.customers:
            if customer.ID.lower() == value or customer.name.lower() == value:
                return customer
        return None

    def find_product(self, value):
        """
        Find a product by ID or name.
        This method searches the products list for a product with a matching ID or name.
        """
        value = value.lower()
        for product in self.products:
            if product.ID.lower() == value or product.name.lower() == value:
                return product
        return None

    def list_customers(self):
        """
        List all customers.
        This method iterates through the customers list and displays information for each customer.
        """
        for customer in self.customers:
            customer.display_info()

    def list_products(self):
        """
        List all products.
        This method iterates through the products list and displays information for each product.
        """
        for product in self.products:
            product.display_info()

    def list_orders(self):
        """
        List all orders.
        This method iterates through the orders list and displays information for each order.
        """
        for order in self.orders:
            if 'original_input' in order:
                customer_identifier = order['customer'].ID if order['customer'].ID.lower() in order['original_input'] else order['customer'].name
                item_details = ', '.join(f"{item[0].ID if item[0].ID.lower() in order['original_input'] else item[0].name}, {item[1]}" for item in order['items'])
            else:
                customer_identifier = order['customer'].ID
                item_details = ', '.join(f"{item[0].ID}, {item[1]}" for item in order['items'])
            print(f"{customer_identifier}, {item_details}, {order['total_cost']}, {order['earned_rewards']}, {order['date']}")

class Operations:
    """
    Main class for handling operations and user interactions.
    This class manages the main functionality of the program, including loading data, saving data, and handling user inputs.
    """
    def __init__(self, customer_file, product_file, order_file='orders.txt'):
        """
        Initialize the operations with file names for customer, product, and order data.
        This method sets up the Records object and loads data from the specified files.
        """
        self.records = Records()
        self.customer_file = customer_file
        self.product_file = product_file
        self.order_file = order_file
        self.load_data()

    def load_data(self):
        """
        Load customer, product, and order data from files.
        This method calls the read methods of the Records class to load data from the specified files.
        """
        try:
            self.records.read_customers(self.customer_file)
            self.records.read_products(self.product_file)
            self.records.read_orders(self.order_file)
        except FileNotFoundError as e:
            print(e)
            exit()

    def save_customers(self):
        """
        Save the updated customer data to the customers.txt file.
        This method calls the save_customers method of the Records class to write customer data to a file.
        """
        self.records.save_customers()

    def save_products(self):
        """
        Save the updated product data to the products.txt file.
        This method calls the save_products method of the Records class to write product data to a file.
        """
        with open(self.product_file, 'w') as file:
            for product in self.records.products:
                if isinstance(product, Product):
                    file.write(f"{product.ID},{product.name},{product.price},{product.prescription_required}\n")
                elif isinstance(product, Bundle):
                    component_ids = ','.join(product.component_ids)
                    file.write(f"{product.ID},{product.name},{component_ids}\n")

    def generate_next_id(self):
        """
        Generate the next ID for a product or bundle.
        This method generates a new unique ID by finding the highest existing ID and incrementing it.
        """
        existing_ids = [product.ID for product in self.records.products]
        existing_numbers = [int(id[1:]) for id in existing_ids]
        next_number = max(existing_numbers, default=0) + 1
        return next_number
    
    def add_update_product(self):
        """
        Add or update a product or bundle in the system.
        This method allows the user to input details for a new or existing product or bundle and saves the updated information.
        """
        while True:
            product_input = input("Enter product ID or name: ").strip()
            product = self.records.find_product(product_input)

            if product:
                # Update existing product or bundle
                if isinstance(product, Product):
                    print(f"Updating existing product: {product.name}")
                    try:
                        product_price = float(input(f"Enter new product price (current: {product.price}): ").strip())
                        if product_price <= 0:
                            print("Price must be a positive number. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid price. Please enter a valid number.")
                        continue
                    prescription_required = input(f"Does this product require a doctor's prescription (current: {product.prescription_required})? (y/n): ").strip().lower()
                    if prescription_required not in ['y', 'n']:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        continue

                    product.price = product_price
                    product.prescription_required = prescription_required
                    print(f"Product '{product.ID}' updated successfully.")
                elif isinstance(product, Bundle):
                    print(f"Updating existing bundle: {product.name}")
                    component_ids = input(f"Enter new component product IDs separated by commas (current: {', '.join(product.component_ids)}): ").strip().split(',')
                    component_ids = [component_id.strip() for component_id in component_ids]
                    existing_components = {component.ID for component in product.products}
                    new_components = set(component_ids)

                    all_component_ids = existing_components.union(new_components)
                    components = [self.records.find_product(component_id) for component_id in all_component_ids]

                    if not all(components):
                        print("One or more component IDs are invalid. Please try again.")
                        continue

                    product.component_ids = list(all_component_ids)
                    product.products = components
                    product.price = product.calculate_price()
                    product.prescription_required = product.check_prescription_requirement()
                    print(f"Bundle '{product.ID}' updated successfully.")
            else:
                # Add new product or bundle
                next_id = self.generate_next_id()
                product_type = input("Enter 'P' for product or 'B' for bundle: ").strip().upper()
                if product_type == 'P':
                    product_id = f"P{next_id}"
                    product_name = product_input  # Use the initial input as the product name

                    try:
                        product_price = float(input("Enter product price: ").strip())
                        if product_price <= 0:
                            print("Price must be a positive number. Please try again.")
                            continue
                    except ValueError:
                        print("Invalid price. Please enter a valid number.")
                        continue

                    prescription_required = input("Does this product require a doctor's prescription? (y/n): ").strip().lower()
                    if prescription_required not in ['y', 'n']:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        continue

                    new_product = Product(product_id, product_name, product_price, prescription_required)
                    self.records.products.append(new_product)
                    print(f"Product '{product_id}' added successfully.")
                elif product_type == 'B':
                    bundle_id = f"B{next_id}"
                    bundle_name = product_input  # Use the initial input as the bundle name

                    component_ids = input("Enter component product IDs separated by commas: ").strip().split(',')
                    component_ids = [component_id.strip() for component_id in component_ids]
                    components = [self.records.find_product(component_id) for component_id in component_ids]
                    if not all(components):
                        print("One or more component IDs are invalid. Please try again.")
                        continue

                    new_bundle = Bundle(bundle_id, bundle_name, component_ids, components)
                    self.records.products.append(new_bundle)
                    print(f"Bundle '{bundle_id}' added successfully.")
                else:
                    print("Invalid product type. Please enter 'P' for product or 'B' for bundle.")
                    continue

            # Save changes to the products file
            self.save_products()
            break

    def save_orders(self):
        """
        Save the updated order data to the orders.txt file.
        This method appends new orders to the orders.txt file, ensuring existing orders are not duplicated.
        """
        try:
            with open(self.order_file, 'r') as file:
                existing_orders = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            existing_orders = []

        existing_orders_set = set(existing_orders)  # Use a set to avoid duplicates

        new_orders = []
        for order in self.records.orders:
            original_inputs = order.get('original_input', [])
            customer_identifier = order['customer'].ID if order['customer'].ID.lower() in original_inputs else order['customer'].name
            item_details = ', '.join(f"{item[0].ID if item[0].ID.lower() in original_inputs else item[0].name}, {item[1]}" for item in order['items'])
            new_order_line = f"{customer_identifier}, {item_details}, {order['total_cost']}, {order['earned_rewards']}, {order['date']}"
            if new_order_line not in existing_orders_set:
                new_orders.append(new_order_line)

        with open(self.order_file, 'a') as file:  # Append new orders to avoid overwriting
            for new_order in new_orders:
                file.write(new_order + '\n')

    def display_menu(self):
        """
        Display the main menu and handle user inputs.
        This method presents a menu of options to the user and calls the appropriate methods based on the user's choice.
        """
        while True:
            print("\n1. Make a purchase\n2. Display existing customers\n3. Display existing products\n4. Add/update product\n5. Display all orders\n6. Display a customer order history\n7. Adjust the reward rate of all Basic customers\n8. Adjust the discount rate of a VIP customer\n9. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.make_purchase()
            elif choice == '2':
                self.records.list_customers()
            elif choice == '3':
                self.records.list_products()
            elif choice == '4':
                self.add_update_product()
            elif choice == '5':
                self.display_all_orders()
            elif choice == '6':
                self.display_customer_order_history()
            elif choice == '7':
                self.adjust_basic_customer_reward_rate()
            elif choice == '8':
                self.adjust_vip_customer_discount_rate()
            elif choice == '9':
                self.save_customers()
                self.save_products()
                self.save_orders()
                break
            else:
                print("Invalid choice. Please try again.")

    def make_purchase(self):
        """
        Handle the purchase process for a customer.
        This method facilitates the purchase process by allowing the user to select a customer, choose products, and finalize the purchase.
        """
        while True:
            try:
                customer_input = input("Enter customer name or ID: ")
                # Check if the input is a valid customer ID
                if customer_input.isdigit() or (customer_input[0].isalpha() and customer_input[1:].isdigit()):
                    customer = self.records.find_customer(customer_input)
                else:
                    # Validate the customer name
                    if not customer_input.replace(' ', '').isalpha() or not customer_input[0].isupper():
                        raise InvalidNameException("Name must start with a capital letter and contain only alphabetic characters.")
                    customer = self.records.find_customer(customer_input)
                if not customer:
                    customer = BasicCustomer(f"B{len(self.records.customers) + 1}", customer_input, 0)
                    self.records.customers.append(customer)
                    print(f"New Basic customer added: {customer_input}")
                else:
                    if isinstance(customer, VIPCustomer):
                        print(f"Existing customer: {customer.name} (VIP Customer)")
                    else:
                        print(f"Existing customer: {customer.name} (Basic Customer)")
                break
            except InvalidNameException as e:
                print(e)

        items = []
        original_inputs = [customer_input.lower()]
        while True:
            try:
                product_input = input("Enter product name or ID (or 'done' to finish): ")
                if product_input.lower() == 'done':
                    break
                product = self.records.find_product(product_input)
                if not product:
                    raise InvalidProductException("Invalid product name or ID.")
                original_inputs.append(product_input.lower())
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity <= 0:
                            raise InvalidQuantityException("Quantity must be a positive integer.")
                        break
                    except (ValueError, InvalidQuantityException) as e:
                        print(e)
                items.append((product, quantity))
            except InvalidProductException as e:
                print(e)

        if not items:
            print("No items selected.")
            return
        
        requires_prescription = any(item[0].prescription_required == 'y' for item in items)
        if requires_prescription:
            while True:
                try:
                    has_prescription = input("Do you have a doctor's prescription? (y/n): ").lower()
                    if has_prescription not in ['y', 'n']:
                        raise InvalidPrescriptionException("Invalid input. Please enter 'y' or 'n'.")
                    if has_prescription == 'n':
                        print("Purchase cannot be completed without a doctor's prescription for one or more selected products.")
                        return
                    break
                except InvalidPrescriptionException as e:
                    print(e)

        total_original_cost = 0
        total_discount = 0
        total_final_cost = 0
        total_reward = 0
        order = Order(customer, items)
        original_cost, discount, final_cost, reward = order.compute_cost()
        total_original_cost += original_cost
        total_discount += discount
        total_final_cost += final_cost
        total_reward += reward

        print(f"\n{'-'*57}\n{'Receipt':^57}\n{'-'*57}")
        print(f"Name:                    {customer.name:<30}")
        for product, quantity in items:
            print(f"Product:                 {product.name:<30}")
            print(f"Unit Price:              {product.price:<5} (AUD)")
            print(f"Quantity:                {quantity:<30}")
        print(f"{'-'*57}")
        print(f"Total original cost:     {total_original_cost:<5} (AUD)")
        print(f"Total discount:          {total_discount:<5} (AUD)")
        print(f"Total final cost:        {total_final_cost:<5} (AUD)")
        print(f"Earned reward:           {total_reward:<30}\n{'-'*57}")

        customer.update_reward(total_reward)

        # Add the order to the records after purchase
        order = {
            'customer': customer,
            'items': items,
            'total_cost': total_final_cost,
            'earned_rewards': total_reward,
            'date': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'original_input': original_inputs
        }
        self.records.orders.append(order)
        self.save_orders()

    def display_all_orders(self):
        """
        Display all orders.
        This method calls the list_orders method of the Records class to display all orders.
        """
        self.records.list_orders()

    def display_customer_order_history(self):
        """
        Display a particular customer's order history.
        This method prompts the user for a customer name or ID and displays the order history for that customer.
        """
        customer_input = input("Enter customer name or ID: ")
        customer = self.records.find_customer(customer_input)
        if not customer:
            print("Customer not found.")
            return
        print(f"\n{'-'*80}\n{'Order History for ' + customer.name:^80}\n{'-'*80}")
        print(f"{'Products':^45}{'Total Cost':>10}        {'Earned Rewards':>15}")
        order_count = 1
        for order in self.records.orders:
            if order['customer'].ID == customer.ID:
                product_details = ', '.join(f"{item[0].name} x{item[1]}" for item in order['items'])
                print(f"{'Order ' + str(order_count):<10}{product_details:^26}      {order['total_cost']:>10.1f}     {order['earned_rewards']:>15}")
                order_count += 1
        print(f"{'-'*80}")

    def adjust_basic_customer_reward_rate(self):
        """
        Adjust the reward rate for all Basic customers.
        
        This method prompts the user for a new reward rate and updates the reward rate for all BasicCustomer instances.
        """
        while True:
            try:
                new_rate = float(input("Enter the new reward rate for all Basic customers (e.g., enter 1 for 100%): ").strip())
                if new_rate <= 0:
                    print("The reward rate must be a positive number. Please try again.")
                    continue
                BasicCustomer.set_reward_rate(new_rate)
                for customer in self.records.customers:
                    if isinstance(customer, BasicCustomer):
                        customer.reward_rate = new_rate
                self.save_customers()
                print(f"Reward rate for all Basic customers has been set to {new_rate * 100}%.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def adjust_vip_customer_discount_rate(self):
        """
        Adjust the discount rate of a VIP customer.
        This method prompts the user for a VIP customer and a new discount rate, and updates the discount rate for that customer.
        """
        while True:
            try:
                customer_input = input("Enter VIP customer name or ID: ").strip()
                customer = self.records.find_customer(customer_input)
                if not customer or not isinstance(customer, VIPCustomer):
                    print("Invalid VIP customer. Please try again.")
                    continue
                
                new_rate = float(input(f"Enter the new discount rate for VIP customer {customer.name} (e.g., enter 0.2 for 20%): ").strip())
                if new_rate <= 0:
                    print("The discount rate must be a positive number. Please try again.")
                    continue
                
                customer.set_discount_rate(new_rate)
                self.save_customers()
                print(f"Discount rate for VIP customer {customer.name} has been set to {new_rate * 100}%.")
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    customer_file = 'customers.txt'
    product_file = 'products.txt'
    order_file = 'orders.txt'

    if len(sys.argv) > 1:
        if len(sys.argv) == 3 or len(sys.argv) == 4:
            customer_file = sys.argv[1]
            product_file = sys.argv[2]
            if len(sys.argv) == 4:
                order_file = sys.argv[3]
        else:
            print("Usage: python ProgFunA2_s1234567.py <customer_file> <product_file> [order_file]")
            sys.exit(1)

    operations = Operations(customer_file, product_file, order_file)
    operations.display_menu()

"""
Design Process and Reflections:

The program was meant to keep track of the orders, products, and client information for a retailing system. 
One of the primary goals was to ensure that the procedures for both basic and VIP customers were being followed. 
For instance, typical discounts are given to basic customers, whereas individual discounts are given to VIP customers. 
It was found that rewards were computed correctly and that orders were processed quickly.

The first step in the development process is the definition of the following core classes: Customer, BasicCustomer, VIPCustomer, Product, Bundle, 
Order, and Records. Each class has been designed to incorporate specific methods and variables, which provide the needed functionality. 
Several client categories require tailored behaviour and BasicCustomer and VIPCustomer Client classes extend client. However, for the sake of the 
ongoing documentation of all system events, there is a task assigned to the Records class, which is responsible for the collecting of information 
about client contacts, changes in product availability, and purchase histories.

The first difficulty was the creation of the order processing system, which should be responsible for such parameters as the application of discounts, 
calculation of rewards, or inclusion of bundles in an order. The Order class was created to add the total cost, calculate discounts for VIP clients, 
and calculate the entire reward system. The discount given to the VIP customers is the total cost minus the percentage of the total cost and the reward 
points are the total cost divided by 10 and then it rounds down to the nearest integer. This will help to avoid miscalculations regarding discount and 
reward provision to VIP customers.

The program effectively executes an error handling system and safeguards itself against independent exceptions with personal exceptions such as InvalidNameException, 
InvalidProductException, InvalidQuantityException, and InvalidPrescriptionException. This guarantees not only the settling of input but also the mistake 
management; hence, it will assure the stakeholders with the confidence of the program's reliability.


Reference:

[1] “9. Classes — Python 3.8.4rc1 documentation,” docs.python.org. https://docs.python.org/3/tutorial/classes.html

[2] python.org, “8. Errors and Exceptions — Python 3.8.1 documentation,” Python.org, 2020. https://docs.python.org/3/tutorial/errors.html
"""