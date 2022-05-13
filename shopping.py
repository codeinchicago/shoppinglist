"""
Build a shopping cart program with the following capabilities:

1) Takes in an input
2) Stores user input into a dictionary or list
3) The User can add or delete items
4) The User can see current shopping list
5) The program Loops until user 'quits'
6) Upon quiting the program, prints out a receipt of the items with total and quantity.
"""
#TO DO: Two decimal precision for the total. {:2f}
# Duplicate items, order apple, then banana, then apple.
# Ensure valid input from user.
# Adding up cost of items is wrong.

#Two dictionaries, number of items, cost of items.

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
            #total = "{:2f}".format(total)
            print(f"Your total is {total}.")
            break
        elif entry == "delete":
            remove = input("What would you like to delete? ")
            del order_dict[remove]
        elif entry == "view":
            print(order_dict)        
        elif entry not in order_dict.keys():
            cost = input("How much does it cost? ")
            order_dict[entry] = cost
            numitems[entry] = 1
        elif entry in order_dict.keys():
            numitems[entry] += 1
            print(numitems)


        # 2. Add, delete items and view current shopping list

        
orders()