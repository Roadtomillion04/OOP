class Item(object):
    pay_rate = 0.8
    all = []

    def __init__(self, name:str, price:float, quantity=0):
        assert price >= 0, f'Price {price} can\'t be negative'
        assert quantity >= 0., f'quantity {quantity} can\'t be negative'

        self.__name = name # To make it private variable
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    # Let's set name attribute inaccessible
    @property # property = Read-only attribute
    def name(self): # It throws error as setter is not defined so change it _name
        return self.__name

    # Let's use setter to make property name accessible again
    @name.setter # func in property.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception(f'{value} is too long!')
        self.__name = value


    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # We are using class method - global method
    @classmethod
    def instantiate_csv_files(cls):
        with open('Items.csv', 'r') as f:
            reader = csv.DictReader(f) # This read csv files in list of dictionaries k, v
            items = list(reader) # To iterate

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    # static method - it's like normal func doesn't take cls or obj
    @staticmethod
    def is_integer(num):
        # check the num has decimal points
        if isinstance(num, float):
            return num.is_integer() # is_integer return True if 1.0 else false
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self): # represent method
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'

    # This sets the attributes inaccessible
    @property
    def read_only_name(self):
        return 'AAA'
