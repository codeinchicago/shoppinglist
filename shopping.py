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
# X Ensure valid input from user, numbers only for price, anything fine for item.
# X Adding up cost of items is wrong.
# X Receipt needs total and quantity.
# X Needed nicely formatted list of items ordered.
# X What if item to delete is not in items?
# X Duplicate items on receipt.
# X Deal with different formatting of input by making it all lower case.
# X Write with print(f "DSFSDFSF") formatting to fix spacing issues.

# X 1. Get and store input

def orders():
    import re
    running = True
    total = 0
    order_dict = {}
    numitems = {}
    valid_input = True

    while running == True:   
        entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ").lower()
        while entry.isalpha() == False:
            print("Letters only, please.")
            entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ").lower()
        if entry == "quit":
            for order, price in order_dict.items():
                print(f"{numitems[order]} {order} at ${price} each, for a total of ${(float(numitems[order]) * float(price))}.")
                total += (float(numitems[order]) * float(price))
                #print("Total cost is: ", total)
            print(f'Your total is ${total:.2f}.')
            break
        elif entry == "delete":
            remove = input("What would you like to delete? ").lower()
            if remove not in order_dict:
                print("Item not in cart.")
            else:
                del order_dict[remove]
        elif entry == "view":
            for order, price in order_dict.items():
                print(f"{numitems[order]} {order} at ${price} each, for a total of ${(float(numitems[order]) * float(price))}.")
        elif entry not in order_dict.keys():
            cost = input("How much does it cost? Input numbers only, please.")
            order_dict[entry] = cost
            numitems[entry] = 1
        else:
            numitems[entry] += 1     

orders()