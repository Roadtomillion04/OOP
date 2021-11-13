# Parent class
from itemClass import Item

# Creating an instance class
class Phone(Item): # child class

    def __init__(self, name ,price, quantity, broken_phones=0):
        # Calling super() to have access to parent class attribute / methods
        super().__init__(name, price, quantity)

        assert broken_phones >=0, f'Broken phone {broken_phones} can\'t be negative'
        # Assigning phone's attribute
        self.broken_phones = broken_phones

    # phone's method



phone1 = Phone('JcPhone01', 500, 5, 6)
phone2 = Phone('JcPhone02', 700, 15, 3)
phone2.apply_discount()
print(phone2.price)

# Both gives same Item() as output because we didn't change __repr__
# After changing in __rep__ in Item() now it prints instance is from which class
print(Item.all)
print(Phone.all)
