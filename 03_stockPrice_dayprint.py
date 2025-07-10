def calculate_max_profit(prices):
    """
    Calculates the maximum profit from a single buy-sell transaction.
    Returns 0 if no profit is possible (prices decline or stay the same).
    Also prints the best day to buy and sell to get that maximum profit.
    """

    if not prices or len(prices) < 2:
        print("Not enough data to calculate profit.")
        return 0

    min_price = prices[0]      # Track the lowest price seen so far
    min_day = 0                # Index (day) of min_price
    max_profit = 0             # Highest profit seen so far
    buy_day = 0                # Day to buy
    sell_day = 0               # Day to sell

    # Loop through prices starting from day 1
    for i in range(1, len(prices)):
        price = prices[i]

        potential_profit = price - min_price

        # Update max profit and corresponding buy/sell days
        if potential_profit > max_profit:
            max_profit = potential_profit
            buy_day = min_day
            sell_day = i

        # Update min_price if a new lower price is found
        if price < min_price:
            min_price = price
            min_day = i

    # Print the result
    if max_profit > 0:
        print(f"Buy on day {buy_day} at price {prices[buy_day]}")
        print(f"Sell on day {sell_day} at price {prices[sell_day]}")
        print(f"Maximum profit: {max_profit}")
    else:
        print("No profit is possible.")

    return max_profit

# ✅ Test the function
calculate_max_profit([7, 1, 5, 3, 6, 4])
