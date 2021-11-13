from JimTut.itemClass import Item

# setters and getters = provides special behaviours to attributes

item1 = Item('MacBook m1', 88000, 1)
# After setting @property & _name in Item
"item1.name = 'Lenovo'"
print(item1.name)
# Now we can't set attribute but we can still access _name
'item1._name'
# To make it a private attribute use __name in Item() class
'item1.__name - Now it cant be accessed'
# Now name is private(read-only attribute)


'''property is getter in python'''
# But if you want to set value of private attributes use @setter
item1.name = 'Acer' # Setting an Attribute
print(item1.name)
# after defining setter we can access the name property again

item1.name = 'asdfghjklpo '