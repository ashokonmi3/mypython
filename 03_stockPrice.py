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
# =================
# Explaination
# ✅ Function: calculate_max_profit(prices)
# This function helps us find the maximum profit we can make
#  by buying and selling a stock once.
# We are given a list of prices, where each element represents the 
# price of the stock on that day.
# Step 1: Check if the prices list is empty or has only one price.
# We need at least two prices — one to buy and one to sell.
# If there are not enough prices, we return 0 as no profit can be made.

# Step 2: Assume we buy the stock on the first day.
# So, we store the first price as the minimum price seen so far (min_price).

# Step 3: We also set the initial maximum profit to 0,
#  since we haven't made any transaction yet.

# Step 4: Now we start checking from the second day onwards.
# For each day, we calculate how much profit we would make if 
# we bought at min_price and sold today.
# If the profit is greater than our current max_profit, we update max_profit.
# If today’s price is lower than our current min_price, we update min_price.
# This helps us always have the lowest buy price and the best profit opportunity.

# Step 5: After checking all the prices, we return the highest profit found.
# If no profit was possible (prices kept going down), it returns 0.
# ✅ Time and Space Complexity (explained in simple language):

# 👉 Time Complexity: O(N)
# N is the number of days — or the number of elements in the prices list.
# We look at each day's price only one time in a single loop.
# We do not use any nested loops or go back again.
# So the time taken grows linearly with the number of days.
# That’s why the time complexity is called "O(N)" — one operation per element.

# 👉 Example:
# If there are 5 prices, we do 5 steps.
# If there are 100 prices, we do 100 steps.
# We process each price once — nothing more.

# 👉 Space Complexity: O(1)
# This means the amount of memory (space) used does not grow with the input size.
# We only use two variables — min_price and max_profit — no matter
#  how long the list is.
# We are not storing any extra lists or data structures.
# So the space used stays constant, even if the input list is huge.

# 🧠 Summary:
# Time Complexity = O(N) → fast and efficient
# Space Complexity = O(1) → uses very little memory

# O(1) = Fixed work or memory, no matter how big the input is.
# O(N) = Work or memory grows with the size of the input.
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
