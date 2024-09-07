class Coffee:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = name
        Coffee._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 3:
            raise ValueError("Name must be at least 3 characters long.")
        self._name = value

    def orders(self):
        return [order for order in Order._all if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if len(self.orders()) == 0:
            return 0
        return sum(order.price for order in self.orders()) / len(self.orders())
