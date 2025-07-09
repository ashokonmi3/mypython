# -------------------- INTERVIEW QUESTIONS TO ASK BEFORE WRITING CODE --------------------
# 1. Should we check for a specific pair of numbers or all amicable numbers in a range?
# 2. Should the input numbers always be positive integers?
# 3. Do we need to return True/False or just print the result?
# 4. Are we allowed to use helper functions?
# 5. Do we need to handle invalid inputs like strings or negatives?

# -------------------- APPROACH TO EXPLAIN --------------------
# - I will write a helper function that returns the sum of all proper divisors of a number.
# - Proper divisors are numbers that divide the number exactly, excluding the number itself.
# - Then I will compare if:
#     sum of proper divisors of a == b
#     AND sum of proper divisors of b == a
# - If both conditions are true, then the two numbers are amicable.

# -------------------- FUNCTION TO FIND SUM OF PROPER DIVISORS --------------------
def sum_of_divisors(n):
    """
    Returns the sum of all proper divisors of a number 'n'.
    Proper divisors are numbers less than 'n' that divide it exactly.
    """
    total = 1  # 1 is a proper divisor for all integers > 1

    # Loop from 2 up to square root of n (for performance)
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:  # i is a divisor
            total += i
            if i != n // i:  # avoid adding square roots twice (e.g., 4 * 4 = 16)
                total += n // i  # also add the paired divisor

    return total  # return the total sum of divisors

# -------------------- FUNCTION TO CHECK IF TWO NUMBERS ARE AMICABLE --------------------
def are_amicable(a, b):
    """
    Returns True if numbers 'a' and 'b' are amicable, else False.
    Uses the sum_of_divisors helper function.
    """
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

# -------------------- INPUT: EXAMPLE AMICABLE PAIR --------------------
num1 = 220
num2 = 284

# -------------------- FUNCTION CALL AND FINAL OUTPUT --------------------
if are_amicable(num1, num2):
    print(f"{num1} and {num2} are amicable numbers.")
else:
    print(f"{num1} and {num2} are not amicable numbers.")

# -------------------- EXPLANATION PARAGRAPH --------------------
# This program checks if two given numbers are amicable.
# A helper function calculates the sum of proper divisors by looping only up to the square root of the number.
# The are_amicable() function uses this to check if both numbers satisfy the amicable condition.
# If the sum of divisors of the first number equals the second, and vice versa, they are amicable.

# -------------------- MANUAL TRACE / ITERATION EXAMPLE --------------------
# Example: num1 = 220
# Proper divisors of 220 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
#
# Loop steps for 220:
# i = 2 → 220 % 2 == 0 → add 2 and 110
# i = 4 → 220 % 4 == 0 → add 4 and 55
# i = 5 → 220 % 5 == 0 → add 5 and 44
# i = 10 → 220 % 10 == 0 → add 10 and 22
# i = 11 → 220 % 11 == 0 → add 11 and 20
#
# total = 1 + 2 + 110 + 4 + 55 + 5 + 44 + 10 + 22 + 11 + 20 = 284

# Example: num2 = 284
# Proper divisors of 284 = 1 + 2 + 4 + 71 + 142 = 220
#
# Loop steps for 284:
# i = 2 → 284 % 2 == 0 → add 2 and 142
# i = 4 → 284 % 4 == 0 → add 4 and 71
#
# total = 1 + 2 + 142 + 4 + 71 = 220

# -------------------- TIME AND SPACE COMPLEXITY --------------------
# Let n be the input number

# sum_of_divisors(n):
# - Time Complexity: O(√n) because we iterate only up to sqrt(n)
# - Space Complexity: O(1) since we use only a few variables

# are_amicable(a, b):
# - Calls sum_of_divisors twice → Total Time Complexity: O(√a + √b)
# - Space Complexity: O(1)

# Overall, this is an efficient solution for checking if two numbers are amicable.
