#!/usr/bin/env python3
import shop

"""
Based of of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders: [('apples', 1.0), ('oranges', 3.0)] best shop is shop1.
For orders: [('apples', 3.0)] best shop is shop2.
"""

import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """

    # *** Your Code Here ***
    # Need to find a shop where amount spent is least - set a default shop as best shop
    # Calc total price and compare
    # Use getPriceOfOrder as it calc total cost for order list
    # Compare with first shop
    # If less, set selected shop as best shop
    # If more, set the previous shop as best shop

    least_amt_shop = fruitShops[1] 
    total_price_shop_2 = fruitShops[1].getPriceOfOrder(orderList)
    for i in fruitShops:
        old_price = i.getPriceOfOrder(orderList)
        if total_price_shop_2 > old_price:
            least_amt_shop = i
            total_price = old_price
    return least_amt_shop
    

    return None

def main():
    dir1 = {
        'apples': 2.0,
        'oranges': 1.0
    }

    dir2 = {
        'apples': 1.0,
        'oranges': 5.0
    }

    shop1 =  shop.FruitShop('shop1', dir1)
    shop2 = shop.FruitShop('shop2', dir2)

    shops = [shop1, shop2]

    orders = [('apples', 1.0), ('oranges', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

    orders = [('apples', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

if __name__ == '__main__':
    main()
