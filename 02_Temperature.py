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

    # Create result list filled with 0 — by default assume no warmer day
    answer = [0] * len(temperatures)

    # Stack to store indices of days waiting for a warmer day
    stack = []

    # Loop using index
    i = 0
    for i in range(len(temperatures)):
        current_temp = temperatures[i]  # Get the temperature for the current day (index i)

        # Check if current_temp is warmer than the day at top of stack
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()  # Remove the index from top of stack
            answer[prev_day] = i - prev_day  # Compute how many days we waited

            # Example trace for [73, 74, 72, 75]:
            # When i=1 (74):
            # stack=[0], temperatures[0]=73
            # 74 > 73 → pop 0 → answer[0]=1
            #
            # When i=3 (75):
            # stack=[1,2], temperatures[2]=72
            # 75 > 72 → pop 2 → answer[2]=1
            # 75 > 74 → pop 1 → answer[1]=2

        # Push current day's index onto stack
        stack.append(i)

                # Detailed trace for input [73, 74, 72, 75]
        # ----------------------------------------------------------
        # i = 0, temp = 73
        # → stack was empty, push 0
        # → stack = [0]
        # → answer = [0, 0, 0, 0]
        #
        # i = 1, temp = 74
        # → temp 74 > temp at stack[-1] (73 at index 0)
        # → pop 0, answer[0] = 1 - 0 = 1
        # → stack = []
        # → push 1
        # → stack = [1]
        # → answer = [1, 0, 0, 0]
        #
        # i = 2, temp = 72
        # → temp 72 not warmer than temp at stack[-1] (74 at index 1)
        # → push 2
        # → stack = [1, 2]
        # → answer = [1, 0, 0, 0]
        #
        # i = 3, temp = 75
        # → Check top of stack: index 2, temp = 72
        # → 75 > 72 → means day 3 is warmer than day 2
        # → pop 2 from stack
        # → calculate days waited: 3 - 2 = 1
        # → set answer[2] = 1 → day 2 waited 1 day for warmer temp
        # → stack after pop: [1]

        # → Check new top of stack: index 1, temp = 74
        # → 75 > 74 → means day 3 is warmer than day 1
        # → pop 1 from stack
        # → calculate days waited: 3 - 1 = 2
        # → set answer[1] = 2 → day 1 waited 2 days for warmer temp
        # → stack after pop: []

        # → No more previous days to resolve (stack empty now)
        # → push current day (3) onto stack → waiting for future warmer day
        # → stack = [3]

        # → current answer = [1, 2, 1, 0]
        #     day 0 waited 1 day for warmer temp
        #     day 1 waited 2 days for warmer temp
        #     day 2 waited 1 day for warmer temp
        #     day 3 no warmer day ahead yet → 0


        i += 1  # Move to the next day

    # Return the result list — any days left in stack had no warmer day ahead, so stay 0
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

# =========================
# improved solution 

def daily_temperatures(temperatures):
    """
    For each day, calculate how many days to wait for a warmer temperature.
    Builds the answer list dynamically without pre-filling with zeros.
    """

    answer = []  # We'll build the list dynamically
    stack = []   # Stack to store indices of days waiting for warmer temp

    # Use a basic for loop with index (no enumerate)
    for i in range(len(temperatures)):
        current_temp = temperatures[i]  # Get current day's temperature

        # Check if this temp resolves any previous days waiting for a warmer day
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()  # Take out the previous cooler day
            # Fill answer up to prev_day index if needed
            while len(answer) <= prev_day:
                answer.append(0)
            # Set the number of days waited
            answer[prev_day] = i - prev_day

        # Push current day index onto the stack
        stack.append(i)

    # After finishing the loop, fill remaining positions with 0
    # (days that never had a warmer day ahead)
    for index in stack:
        while len(answer) <= index:
            answer.append(0)

    return answer

# Example call
print(daily_temperatures([73, 74, 72, 75]))  # Expected: [1, 2, 1, 0]
print(daily_temperatures([70, 71, 69, 72]))  # Expected: [1, 2, 1, 0]
print(daily_temperatures([73, 72, 71, 70]))  # Expected: [0, 0, 0, 0]
