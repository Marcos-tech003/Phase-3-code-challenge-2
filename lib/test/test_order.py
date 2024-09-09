import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_order_creation():
    customer = Customer("Eve")
    coffee = Coffee("Cappuccino")
    order = Order(customer, coffee, 3.5)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 3.5
