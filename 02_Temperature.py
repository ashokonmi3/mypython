# 🎤 Clarifying questions to ask the interviewer
# 🟣 “Are the temperatures always positive integers?”
# 👉 (Not necessary for the algorithm, but good to confirm)

# 🟣 “What should I return if no warmer temperature comes after a day?”
# 👉 Usually return 0 for that day.

# 🟣 “Should I optimize for time/space, or is a simple solution okay?”
# 👉 Lets you choose between brute-force and efficient solutions.

# 🟣 “How large can the input array be?”
# 👉 Important to justify why you choose an O(N) approach.

# Approach in simple language
# 👉 “I go through the list of temperatures one day at a time. 
# I use a stack to remember the days where I’m still waiting for a warmer temperature.
# Whenever I find a warmer temperature than a previous day stored on the stack, 
# I calculate how many days I had to wait by subtracting the indices. 
# I fill this value into the result list.
# If I don’t find a warmer temperature for a day, 
# I leave its value as zero, since we initialized the answer list with zeros. 
# This approach is efficient because each day’s index goes into the stack once and comes out once.”

def daily_temperatures(temperatures):
    """
    For each day, calculate how many days to wait for a warmer temperature.
    """

    # Initialize result list with 0s
    answer = [0] * len(temperatures)

    # Initialize stack to keep indices of temperatures waiting for a warmer day
    stack = []

    # Loop through each day
    for current_day, current_temp in enumerate(temperatures):

        # Check if current temperature is warmer than the temperature at top of stack
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()
            answer[prev_day] = current_day - prev_day

            # Example trace for input [73, 74, 72, 75]
            # Day 1 (74) > Day 0 (73): pop 0, answer[0] = 1 - 0 = 1
            # Day 3 (75) > Day 2 (72): pop 2, answer[2] = 3 - 2 = 1
            # Day 3 (75) > Day 1 (74): pop 1, answer[1] = 3 - 1 = 2

        # If not warmer or after resolving warmer, push current day
        stack.append(current_day)

        # Detailed trace of each step:
        # current_day = 0, current_temp = 73
        #   stack = [0]
        #   answer = [0, 0, 0, 0]
        #
        # current_day = 1, current_temp = 74
        #   74 > 73 → pop 0 → answer[0] = 1
        #   stack = [1]
        #   answer = [1, 0, 0, 0]
        #
        # current_day = 2, current_temp = 72
        #   72 not warmer → push 2
        #   stack = [1, 2]
        #   answer = [1, 0, 0, 0]
        #
        # current_day = 3, current_temp = 75
        #   75 > 72 → pop 2 → answer[2] = 1
        #   75 > 74 → pop 1 → answer[1] = 2
        #   stack = [3]
        #   answer = [1, 2, 1, 0]

    # Return final answer list
    return answer

# Example call:
# Input: [73, 74, 72, 75]
# Expected output: [1, 2, 1, 0]
print(daily_temperatures([73, 74, 72, 75]))

# 🎤 Time complexity
# 👉 “The time complexity is O(N), where N is the number of days or temperatures. 
# This is because we go through the list once, and each day’s index is added to the stack at 
# most once and removed from the stack at most once. So, no day’s index is processed more than
#  twice — once when pushed and once when popped.”

# 🎤 Space complexity
# 👉 “The space complexity is O(N) because in the worst case — for example 
# if temperatures are strictly decreasing — we might end up putting all N days onto the
#  stack before finding a warmer day or finishing the loop. We also use an answer list of size N.”

