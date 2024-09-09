# Coffee Ordering System

## Overview

This project consists of a simple Coffee Ordering System with the following components:
- **Order**: Represents a coffee order made by a customer.
- **Customer**: Represents a customer who can place orders.
- **Coffee**: Represents a type of coffee available for ordering.

## Classes

### `Order`

The `Order` class represents an order made by a customer for a specific coffee.

#### Attributes
- `customer` (Customer): The customer who placed the order.
- `coffee` (Coffee): The type of coffee ordered.
- `price` (float): The price of the coffee, which must be between 1.0 and 10.0 inclusive.

#### Methods
- `__init__(self, customer, coffee, price)`: Initializes an order with the provided customer, coffee, and price.
- `customer`: Returns the customer who placed the order.
- `coffee`: Returns the coffee ordered.
- `price`: Returns the price of the coffee.

#### Class Attributes
- `_all`: A class-level list to keep track of all instances of the `Order` class.

### `Customer`

The `Customer` class represents a customer who can place coffee orders.

#### Attributes
- `name` (str): The name of the customer. It must be a string between 1 and 15 characters.

#### Methods
- `__init__(self, name)`: Initializes a customer with the provided name.
- `name`: Getter and setter for the customer's name.
- `orders()`: Returns a list of all orders placed by this customer.
- `coffees()`: Returns a list of unique coffees ordered by this customer.
- `create_order(coffee, price)`: Creates a new order for this customer with the specified coffee and price.
- `most_aficionado(coffee)`: Class method that returns the customer who has spent the most on the specified coffee.

#### Class Attributes
- `_all`: A class-level list to keep track of all instances of the `Customer` class.

### `Coffee`

The `Coffee` class is a placeholder for coffee types and is assumed to be defined in `lib/coffee.py`. It should be used as follows:
- The `Coffee` class should have at least a name or type to identify different coffee varieties.

## Usage

To use this system, you need to create instances of `Customer` and `Coffee` and use these instances to place orders.

### Example

```python
# Import necessary modules (assuming these are in the lib directory)
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

# Create a coffee instance
latte = Coffee(name="Latte")

# Create a customer instance
john = Customer(name="John Doe")

# Create an order
order = john.create_order(coffee=latte, price=5.0)

# Retrieve customer details
print(john.name)  # Output: John Doe
print(john.orders())  # Output: [<Order object>]
print(john.coffees())  # Output: [<Coffee object>]

# Determine the most aficionado customer for a given coffee
most_aficionado = Customer.most_aficionado(coffee=latte)
print(most_aficionado.name)  # Output: John Doe
