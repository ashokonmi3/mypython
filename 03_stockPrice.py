# 🎤 Clarifying questions to ask the interviewer
#  👉 “Can I assume the input list only contains positive integers, 
#      or can it have zero or negative prices?”
#  👉 “Is it guaranteed that the list has at least two days of prices,
#      or do I need to handle empty or one-element lists?”
#  👉 “Is there only one transaction allowed (one buy, one sell), 
#      or can we buy and sell multiple times?”
#  👉 “how much time i have to solve this problem , 


# 🎤 How to explain the approach
# 👉 “I scan through the prices one by one. 
# I keep track of the lowest price I’ve seen so far to know the best day to buy. 
# Each day I calculate the profit if I sold today at that lowest price. 
# If the profit is better than any profit I’ve seen so far, I update my max profit.
#  I also update my lowest price if today’s price is lower.”

def calculate_max_profit(prices):
    """
    Calculates the maximum profit from a single buy-sell transaction.
    Returns 0 if no profit is possible (prices decline or stay same).
    """

    if not prices or len(prices) < 2:
        return 0  # No profit possible with empty list or one price

    # min_price keeps track of the lowest price we've seen so far.
    # Initialize with price on first day — assume we buy on day 0 initially.
    min_price = prices[0]

    # max_profit keeps track of the highest profit found so far.
    max_profit = 0

    # Loop through prices starting from day 1 (since min_price is from day 0)
    for i in range(1, len(prices)):
        price = prices[i]  # Current day's price

        # Calculate profit if we sold today at current price
        potential_profit = price - min_price

        # If this profit is better than what we've seen before, update max_profit
        if potential_profit > max_profit:
            max_profit = potential_profit

        # If today's price is lower than min_price seen so far, update min_price
        if price < min_price:
            min_price = price

        # 👉 Behind-the-scenes iteration trace:
        # For input [7, 1, 5, 3, 6, 4]:
        #
        # Day 1: price = 1
        #   potential_profit = 1 - 7 = -6 → max_profit = 0 (no update)
        #   min_price updated to 1 (1 < 7)
        #
        # Day 2: price = 5
        #   potential_profit = 5 - 1 = 4 → max_profit updated to 4
        #   min_price remains 1
        #
        # Day 3: price = 3
        #   potential_profit = 3 - 1 = 2 → max_profit remains 4
        #   min_price remains 1
        #
        # Day 4: price = 6
        #   potential_profit = 6 - 1 = 5 → max_profit updated to 5
        #   min_price remains 1
        #
        # Day 5: price = 4
        #   potential_profit = 4 - 1 = 3 → max_profit remains 5
        #   min_price remains 1

    # After looping, return the best profit found
    return max_profit


# ✅ Direct function call with hardcoded input
result = calculate_max_profit([7, 1, 5, 3, 6, 4])

# Print final result
print(f"Maximum profit: {result}")

# Explaination 
# This program is designed to calculate the maximum profit that can be 
# earned from a single buy-and-sell transaction given a list of daily 
# stock prices. The logic starts by handling edge cases—if the list is empty or
# has fewer than two prices, no transaction is possible, so it returns 0. 
# It then initializes two variables: min_price, which keeps track of the lowest 
# stock price seen so far (best day to buy), and max_profit,
# which tracks the highest profit we can make by selling on any
# day after the minimum price day.
# Here i am  iterating through the price list from the second day onward. 
# For each day, it calculates the potential profit by subtracting min_price from the current price. 
# If this potential profit is greater than the max_profit recorded so far, we update max_profit. 
# Similarly, if the current price is lower than min_price, we update min_price to reflect the new best buying opportunity. 
# After going through all the prices, the function returns the highest profit found. 


# ✅ Time and space complexity
# 👉 “Time complexity is O(N) because we go through the list once. 
# Space complexity is O(1) because we only use two variables — min_price and max_profit.”
# =========================================
# [7, 6, 4, 3, 1]
def calculate_max_profit(prices):
    """
    Calculates maximum profit from a single buy-sell transaction.
    Returns 0 if no profit is possible (prices decline or stay same).
    """

    if not prices or len(prices) < 2:
        return 0  # No profit possible

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        price = prices[i]
        potential_profit = price - min_price

        if potential_profit > max_profit:
            max_profit = potential_profit

        if price < min_price:
            min_price = price

        # 👉 Behind-the-scenes trace for input [7, 6, 4, 3, 1]
        #
        # Day 1: price = 6
        #   potential_profit = 6 - 7 = -1
        #   max_profit = 0 (no update, negative profit)
        #   min_price = 6 (6 < 7 → update min_price)
        #
        # Day 2: price = 4
        #   potential_profit = 4 - 6 = -2
        #   max_profit = 0 (no update, negative profit)
        #   min_price = 4 (4 < 6 → update min_price)
        #
        # Day 3: price = 3
        #   potential_profit = 3 - 4 = -1
        #   max_profit = 0 (no update, negative profit)
        #   min_price = 3 (3 < 4 → update min_price)
        #
        # Day 4: price = 1
        #   potential_profit = 1 - 3 = -2
        #   max_profit = 0 (no update, negative profit)
        #   min_price = 1 (1 < 3 → update min_price)

    return max_profit


# ✅ Call the function with [7, 6, 4, 3, 1]
result = calculate_max_profit([7, 6, 4, 3, 1])

print(f"Maximum profit: {result}")
# ==================================
# [1, 10, 3, 11, 3]

def calculate_max_profit(prices):
    """
    Calculates maximum profit from a single buy-sell transaction.
    Returns 0 if no profit is possible.
    """

    if not prices or len(prices) < 2:
        return 0  # Need at least two prices for a transaction

    min_price = prices[0]  # Best price to buy so far
    max_profit = 0  # Best profit seen so far

    for i in range(1, len(prices)):
        price = prices[i]

        # Calculate what profit we'd make if we sold at today's price
        potential_profit = price - min_price

        # Update max_profit if today’s potential profit is better
        if potential_profit > max_profit:
            max_profit = potential_profit

        # Update min_price if today’s price is lower (better buying opportunity)
        if price < min_price:
            min_price = price

        # 👉 Behind-the-scenes trace for input [1, 10, 3, 11, 3]
        #
        # Iteration {i}
        # Current price: {price}
        # Current min_price: {min_price}
        # Potential profit today: {potential_profit}
        # Current max_profit: {max_profit}

        # Example trace:
        # Day 1: price = 10
        #   potential_profit = 10 - 1 = 9
        #   max_profit = 9 (updated from 0)
        #   min_price = 1 (10 > 1 → no change)
        #
        # Day 2: price = 3
        #   potential_profit = 3 - 1 = 2
        #   max_profit = 9 (no update)
        #   min_price = 1 (3 > 1 → no change)
        #
        # Day 3: price = 11
        #   potential_profit = 11 - 1 = 10
        #   max_profit = 10 (updated from 9)
        #   min_price = 1 (11 > 1 → no change)
        #
        # Day 4: price = 3
        #   potential_profit = 3 - 1 = 2
        #   max_profit = 10 (no update)
        #   min_price = 1 (3 > 1 → no change)

    return max_profit

# ✅ Call with your input
result = calculate_max_profit([1, 10, 3, 11, 3])
print(f"Maximum profit: {result}")
# ==============================
# [3, 5, 10, 2, 5, 10, 1]
def calculate_max_profit(prices):
    """
    Calculates maximum profit from a single buy-sell transaction.
    Returns 0 if no profit is possible.
    """

    if not prices or len(prices) < 2:
        return 0  # Need at least two prices for a transaction

    min_price = prices[0]  # Best price to buy so far
    max_profit = 0  # Best profit seen so far

    for i in range(1, len(prices)):
        price = prices[i]

        # Calculate potential profit if we sold today
        potential_profit = price - min_price

        # Update max_profit if today’s potential profit is better
        if potential_profit > max_profit:
            max_profit = potential_profit

        # Update min_price if today’s price is lower
        if price < min_price:
            min_price = price

        # 👉 Behind-the-scenes trace for input [3, 5, 10, 2, 5, 10, 1]
        #
        # i = 1, price = 5
        #   potential_profit = 5 - 3 = 2
        #   max_profit = 2 (updated from 0)
        #   min_price = 3 (no change)
        #
        # i = 2, price = 10
        #   potential_profit = 10 - 3 = 7
        #   max_profit = 7 (updated from 2)
        #   min_price = 3 (no change)
        #
        # i = 3, price = 2
        #   potential_profit = 2 - 3 = -1
        #   max_profit = 7 (no update)
        #   min_price = 2 (updated from 3)
        #
        # i = 4, price = 5
        #   potential_profit = 5 - 2 = 3
        #   max_profit = 7 (no update)
        #   min_price = 2 (no change)
        #
        # i = 5, price = 10
        #   potential_profit = 10 - 2 = 8
        #   max_profit = 8 (updated from 7)
        #   min_price = 2 (no change)
        #
        # i = 6, price = 1
        #   potential_profit = 1 - 2 = -1
        #   max_profit = 8 (no update)
        #   min_price = 1 (updated from 2)

    return max_profit

# ✅ Call with your input
result = calculate_max_profit([3, 5, 10, 2, 5, 10, 1])
print(f"Maximum profit: {result}")
