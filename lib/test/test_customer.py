import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_customer_name():
    customer = Customer("Alice")
    assert customer.name == "Alice"

def test_create_order():
    customer = Customer("Bob")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
