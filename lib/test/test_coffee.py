import pytest
from lib.coffee import Coffee
from lib.customer import Customer
from lib.order import Order

def test_coffee_name():
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

def test_average_price():
    coffee = Coffee("Mocha")
    customer = Customer("Dave")
    customer.create_order(coffee, 6.0)
    customer.create_order(coffee, 4.0)
    assert coffee.average_price() == 5.0
