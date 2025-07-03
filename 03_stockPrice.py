
# 🎤 Clarifying questions to ask the interviewer
#  👉 “Can I assume the input list only contains positive integers, 
#      or can it have zero or negative prices?”
#  👉 “Is it guaranteed that the list has at least two days of prices,
#      or do I need to handle empty or one-element lists?”
#  👉 “Should I return zero profit if no profit is possible, 
#       or do you want some special output in that case?”
#  👉 “Do I need to return the actual buy/sell days or prices,
#      or just the maximum profit?”
#  👉 “Is there only one transaction allowed (one buy, one sell), 
#      or can we buy and sell multiple times?”

# 🎤 How to explain the approach
# 👉 “I scan through the prices one by one. 
# I keep track of the lowest price I’ve seen so far to know the best day to buy. 
# Each day I calculate the profit if I sold today at that lowest price. 
# If the profit is better than any profit I’ve seen so far, I update my max profit.
#  I also update my lowest price if today’s price is lower.”

def max_profit(prices):
    """
    This function calculates the maximum profit possible from a single buy-sell transaction.
    If no profit is possible (prices always decline), it returns 0.

    Parameters:
    prices (List[int]): The input list of daily stock prices.

    Returns:
    int: The maximum profit achievable.
    """

    if not prices:
        return 0  # No prices means no transactions possible.

    # Initialize min_price as the first price in the list (best buy price so far).
    min_price = prices[0]

    # Initialize max_profit to 0 (no profit made yet).
    max_profit = 0

    # Loop through each day starting from day 1 because we already used day 0 for min_price.
    for i in range(1, len(prices)):
        price = prices[i]  # Current day's price.

        # Calculate potential profit if we sell today.
        potential_profit = price - min_price

        # Check if this profit is better than our max so far.
        if potential_profit > max_profit:
            max_profit = potential_profit

        # Update min_price if today's price is lower (better buy price).
        if price < min_price:
            min_price = price

        # Iteration trace for input [71, 5, 3, 6, 4]:
        # i = 1, price = 5
        #   potential_profit = 5 - 71 = -66
        #   max_profit = 0 (no update, profit negative)
        #   min_price = 5 (5 < 71 → update)
        #
        # i = 2, price = 3
        #   potential_profit = 3 - 5 = -2
        #   max_profit = 0 (no update, profit negative)
        #   min_price = 3 (3 < 5 → update)
        #
        # i = 3, price = 6
        #   potential_profit = 6 - 3 = 3
        #   max_profit = 3 (3 > 0 → update)
        #   min_price = 3 (6 > 3 → no change)
        #
        # i = 4, price = 4
        #   potential_profit = 4 - 3 = 1
        #   max_profit = 3 (1 not > 3 → no update)
        #   min_price = 3 (4 > 3 → no change)

    return max_profit  # Return the best profit found.

# Example call:
# Input: [71, 5, 3, 6, 4]
# Expected output: 3 (buy at 3, sell at 6)
print(max_profit([71, 5, 3, 6, 4]))

# ✅ Time and space complexity
# 👉 “Time complexity is O(N) because we go through the list once. 
# Space complexity is O(1) because we only use two variables — min_price and max_profit.”
