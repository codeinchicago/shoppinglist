"""
Build a shopping cart program with the following capabilities:

1) Takes in an input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, prints out a receipt of the items with total and quantity.
"""
#TO DO: X Two decimal precision for the total. {:2f}
# X Duplicate items, order apple, then banana, then apple.
# Ensure valid input from user, numbers only for price, anything fine for item.
# X Adding up cost of items is wrong.
# Receipt needs total and quantity.
# Needed nicely formatted list of items ordered.
# What if item to delete is not in items?
# Duplicate items on receipt.

# X 1. Get and store input

def orders():
    running = True
    total = 0
    order_dict = {}
    numitems = {}

    while running == True:   
        entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ")
        #If entry already found, add the cost of the item.
        if entry == "quit":
            print(order_dict)
            for item in order_dict.values():
                total += float(item)
            print(f'Your total is {total:.2f}.')
            break
        elif entry == "delete":
            remove = input("What would you like to delete? ")
            del order_dict[remove]
        elif entry == "view":
            print(order_dict)
            for order, price in order_dict.items():
                print(order, ': ', price)
        elif entry not in order_dict.keys():
            cost = input("How much does it cost? ")
            order_dict[entry] = cost
            numitems[entry] = 1
        else:
            numitems[entry] += 1
            #print(numitems)       

orders()