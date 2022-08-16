#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

def buyLotsOfFruit(orderList):
    """
    orderList: List of (fruit, weight) tuples

    Returns cost of order
    """

    # *** Your Code Here ***
    # create variable to calculate the total cost of fruits
    totalCost = 0.0
    # create loop to find fruit i in list, check if price is mentioned, 
    # #if yes, calculate total cost, 
    # #if not, print error message 
    for i in orderList:    
        if i[0] not in FRUIT_PRICES:
            print ("%s not in list" % (i[0]))
            return None
        else:
            totalCost += FRUIT_PRICES[i[0]] * i[1]
    return totalCost


def main():
    orderList = [
        ('apples', 2.0),
        ('pears', 3.0),
        ('limes', 4.0)
    ]

    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))

if __name__ == '__main__':
    main()
