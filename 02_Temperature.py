
    # ✅ Questions to ask interviewer before writing code:
    # 1️⃣ Is the list guaranteed to have only integers (temperatures)?
    # 2️⃣ What should I return if all temperatures are the same? (Return all 0s?)
    # 3️⃣ Can the input list be empty?
    # 4️⃣ Are negative temperatures possible, or only positive?

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
    # Each position corresponds to a day. 0 means no warmer day ahead by default.
    answer = [0] * len(temperatures)

    # Initialize an empty stack
    # The stack will store indices of days that are waiting for a warmer temperature
    stack = []

    # Loop over temperatures using enumerate, to get both index (current_day) and value (current_temp)
    for current_day, current_temp in enumerate(temperatures):

        # While stack is not empty AND the current temperature is warmer than
        # the temperature at the index stored at top of stack:
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()  # Remove the top element (previous day index)
            answer[prev_day] = current_day - prev_day  # Compute how many days we waited

            # Example trace for input [73, 74, 72, 75]:
            # Iteration when current_day = 1, current_temp = 74
            #   stack = [0], temperatures[0]=73
            #   74 > 73 → pop 0 → answer[0] = 1 - 0 = 1
            #
            # Iteration when current_day = 3, current_temp = 75
            #   stack = [1, 2], temperatures[2]=72
            #   75 > 72 → pop 2 → answer[2] = 3 - 2 = 1
            #   75 > 74 → pop 1 → answer[1] = 3 - 1 = 2

        # Push the current day's index to stack to process later when warmer temp is found
        stack.append(current_day)

        # Detailed trace of each iteration for [73, 74, 72, 75]:
        # current_day = 0, current_temp = 73
        #   stack = [0], answer = [0, 0, 0, 0]
        #
        # current_day = 1, current_temp = 74
        #   pop 0 → answer[0]=1 → stack=[1], answer=[1,0,0,0]
        #
        # current_day = 2, current_temp = 72
        #   stack=[1,2], answer=[1,0,0,0]
        #
        # current_day = 3, current_temp = 75
        #   pop 2 → answer[2]=1
        #   pop 1 → answer[1]=2
        #   stack=[3], answer=[1,2,1,0]

    # Remaining indices in stack mean no warmer day found → answer stays 0

    return answer

# Example call
print(daily_temperatures([73, 74, 72, 75]))  # Expected output: [1, 2, 1, 0]

# ✅ Complexity explanation:
# Time complexity:
#   O(N) because we process each element at most twice:
#   once when we push its index onto the stack,
#   once when we pop it from the stack.
#
# Space complexity:
#   O(N) because in the worst case (e.g., decreasing temperatures)
#   we might have to store all indices in the stack at once.
#   Also, the answer list is of size N.

