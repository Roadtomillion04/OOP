# Every Instance is a Object i.e str, int
# Creating new class
class Item(object):
    pass

# Instancing a class
item1 = Item()
print(type(item1))

# Creating method in class
class Item(object):
    def calculate_price(self, price, quantity): # self is an instance variable
        print(price * quantity)

item1 = Item()
# assigning attributes
item1.price = 100
item1.quantity = 4
#self   method
item1.calculate_price(price = item1.price, quantity = item1.quantity)

item2 = Item()
item2.price = 75
item2.quantity = 12
item2.calculate_price(price = item2.price, quantity = item2.quantity)

# Understanding __init__ dander method
class Item(object):
    def __init__(self): # python calls this method first when instanced
        print('hi, I am created')

item1 = Item()
item2 = Item()

# Assigning attributes in class
class Item(object):
    # to assign a attributes we use constructor method
    def __init__(self, name):
        print(f'Instance created: {name}')
item1 = Item(name = 'Laptop')


# Creating an Actual class
class Item(object):
    # class attributes - accessed globally in class
    pay_rate = 0.8 # 20% discount
    all = []

                        # typing             # default value
    def __init__(self, name:str, price:float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} can\'t be negative'
        assert quantity >= 0., f'quantity {quantity} can\'t be negative'

        # this refers when item.name passed, give name as output
        self.name = name
        self.price = price
        self.quantity = quantity
        # instance attributes

        # Appending all instances
        Item.all.append(self)

    def apply_discount(self): # call class attributes as self to make it dynamic for each instance
        self.price = self.price * self.pay_rate

    def __repr__(self): # represent method
        return f'{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})'
        # Now it makes easy to read in console

item1 = Item(name = 'Laptop', price = 88000, quantity = 1)
print(item1.price, item1.name, item1.quantity)
#item2 = Item('Phone', -1)
item3 = Item(name = 'Phone', price = 20000, quantity = 2)
item4 = Item(name = 'Keyboard', price = 2000, quantity = 3)

# class attributes can be accessed in instance level too
print(Item.pay_rate, item1.pay_rate)

# Returns all belonging attribute
print(Item.__dict__, item1.__dict__)

item1.apply_discount(), print(item1.price)

# to apply separate discount
item3.pay_rate = 0.7, item3.apply_discount(), print(item3.price)

# To access all instance we created list
print(Item.all)
# To get specific attribute
for instance in Item.all:
    print(instance.name)

