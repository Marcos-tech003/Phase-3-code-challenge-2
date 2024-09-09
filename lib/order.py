class Order:
    _all = []

    def __init__(self, customer, coffee, price):
        from lib.customer import Customer
        from lib.coffee import Coffee
        if not isinstance(customer, Customer):
            raise ValueError("Invalid Customer instance.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid Coffee instance.")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._customer = customer
        self._coffee = coffee
        self._price = price
        Order._all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
