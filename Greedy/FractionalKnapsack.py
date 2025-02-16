# Question:
# Given two arrays, val[] and wt[], representing the values and weights of items, and an integer capacity
# representing the maximum weight a knapsack can hold, determine the maximum total value that can be achieved by
# putting items in the knapsack. You are allowed to break items into fractions if necessary.
# Return the maximum value as a double, rounded to 6 decimal places.

# Logic:
# Pretty straight forward --> we get the val/wt ratio for each element and then sort it based on it.
# Then greedily try to adjust as much as possible.

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, val, wt, capacity):
        z = [[v, w] for v, w in zip(val, wt)]
        z = sorted(z, key= lambda x: x[0]/x[1], reverse=True)
        total = 0
        for items in z:
            val, wt = items[0], items[1]
            if wt > capacity:
                total += (val/wt)*capacity
                capacity = 0
            else:
                capacity -= wt
                total += val
        return total