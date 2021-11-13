import csv


# Let's create csv here
with open('./Items.csv', 'w', newline="") as file:
    # pass  values in List/tuple
    ROWS = {
        'row0': ['name', 'price', 'quantity'],
        'row1': ['Laptop', 88000, 1],
        'row2': ['Phone', 20000, 3],
        'row3': ['Keyboard', 700, 4],
        'row4': ['Cable', 125, 11],
        'row5': ['Mouse', 890, 2]
    }
                                    # ends with 5
    all_values = [ROWS[f'row{a}'] for a in range(len(ROWS))]
    print(all_values) # Returns values in list

    # Create writer object
    writer = csv.writer(file)
    writer.writerows(all_values)

