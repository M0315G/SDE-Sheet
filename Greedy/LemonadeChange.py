from typing import List

# Question:
# At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time
# (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
# You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
# Note that you do not have any change in hand at first.
# Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer
# with the correct change, or false otherwise.

# Logic:
# Just iterate:
# 1. store all 5$ bills
# 2. for 10$ remove 1 5$ and add the 10$
# 3. for 20$, if you have 1 10$ and 1 5$ else 3 5$
# IF any of above fails, return False

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five !=0:
                    five -= 1
                    ten += 1
                else:
                    return False
            else:
                if five !=0:
                    if ten != 0:
                        five -= 1
                        ten -= 1
                    elif five >= 3:
                        five -= 3
                    else:
                        return False
                else:
                    return False
        return True