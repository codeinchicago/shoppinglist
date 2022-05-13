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

#Two dictionaries, number of items, cost of items.

# X 1. Get and store input

def orders():
    running = True
    total = 0
    order_dict = {}
    while running == True:   
        entry = input("What would you like to order? May also 'delete', 'view', or 'quit'. ")
        if entry == "quit":
            print(order_dict)
            for item in order_dict.values():
                total += float(item)
            #total = "{:2f}".format(total)
            print(f"Your total is {total}.")
            break
        elif entry == "view":
            print(order_dict)        


# 2. Add, delete items and view current shopping list
        elif entry == "delete":
            remove = input("What would you like to delete? ")
            del order_dict[remove]
        elif entry not in order_dict.keys():
            cost = input("How much does it cost? ")
            order_dict[entry] = cost
        # Add cost to duplicate dictionary
        #if entry in order_dict.keys():
        #    pass



# 3. Loop until quitting,
        

# 4.  Print receipt upon quitting

orders()