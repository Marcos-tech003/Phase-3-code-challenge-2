from lib.customer import Customer
from lib.coffee import Coffee

from lib.order import Order

customer1 = Customer("John")
coffee1 = Coffee("Latte")
order1 = customer1.create_order(coffee1, 5.0)

print(f"Customer: {order1.customer.name}, Coffee: {order1.coffee.name}, Price: {order1.price}")
