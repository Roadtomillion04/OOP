import csv
from itemClass import Item

# cls
Item.instantiate_csv_files()
print(Item.all)

#static
print(Item.is_integer(4.0))
