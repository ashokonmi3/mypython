# ✅ Questions to ask interviewer before writing code:
# 1️⃣ Is the list guaranteed to have only integers (temperatures)?
# 2️⃣ What should I return if all temperatures are the same? (Return all 0s?)
# 3️⃣ Can the input list be empty?
# 4️⃣ Are negative temperatures possible, or only positive?
# How much time i have for this 
# -------------------- APPROACH IN SIMPLE LANGUAGE --------------------
# 👉 I go through the list of temperatures one day at a time.
# 👉 I use a list (acting as a stack) to remember the indices of the days 
#    for which I'm still waiting to find a warmer temperature.
# 👉 I also create a result list called `answer` and initialize all values to 0, 
#    assuming by default that there's no warmer day ahead.

# 👉 As I move through the list:
#     - If the current day's temperature is warmer than the temperature on top of the stack
#       (i.e., a previous cooler day), then:
#         🔹 I pop that index from the stack.
#         🔹 I calculate how many days I had to wait by subtracting the indices: current_index - previous_index.
#         🔹 I store that number in the corresponding position in the `answer` list.

# 👉 If I don't find a warmer temperature for a day, its value in `answer` stays 0,
#    which is fine because I initialized it that way.

# 👉 This approach is efficient because each index is pushed onto the stack once 
#    and popped at most once — giving us linear time complexity.

# -------------------- FUNCTION DEFINITION --------------------0
def daily_temperatures(temperatures):
    """
    For each day, calculate how many days you have to wait for a warmer temperature.
    If no warmer day is ahead, keep it as 0.
    """

    # Initialize result list with 0s (default = no warmer day ahead)
    answer = [0] * len(temperatures)

    # Stack to store indices of days waiting for a warmer temperature
    stack = []

    # Iterate through the temperature list using index
    for i in range(len(temperatures)):
        current_temp = temperatures[i]  # Temperature of the current day

        # Check if current day is warmer than the top of the stack
        while stack and current_temp > temperatures[stack[-1]]:
            prev_day = stack.pop()  # Get the index of the previous cooler day
            answer[prev_day] = i - prev_day  # Calculate wait duration

        # Push the current day's index onto the stack
        stack.append(i)

    # Any index left in the stack had no warmer temperature later, so answer stays 0
    return answer
print(daily_temperatures([73, 74, 72, 75]))  # Output: [1, 2, 1, 0]

# -------------------- TRACE EXPLANATION FOR INPUT [73, 74, 72, 75] --------------------
# Initial state:
# temperatures = [73, 74, 72, 75]
# answer = [0, 0, 0, 0]  # result list initialized with zeros
# stack = []             # stack to store indices of unresolved days

# Day 0:
# current_temp = 73
# stack is empty → push index 0
# → stack = [0]
# → answer = [0, 0, 0, 0]

# Day 1:
# current_temp = 74
# temperatures[stack[-1]] = 73 < 74 → pop 0 → answer[0] = 1 - 0 = 1
# push 1 → stack = [1]
# → answer = [1, 0, 0, 0]

# Day 2:
# current_temp = 72
# temperatures[stack[-1]] = 74 > 72 → no pop → push 2 → stack = [1, 2]
# → answer = [1, 0, 0, 0]

# Day 3:
# current_temp = 75
# temperatures[2] = 72 < 75 → pop 2 → answer[2] = 3 - 2 = 1
# temperatures[1] = 74 < 75 → pop 1 → answer[1] = 3 - 1 = 2
# push 3 → stack = [3]
# → answer = [1, 2, 1, 0]

# Final result:
# answer = [1, 2, 1, 0]
# → Day 0: wait 1 day for 74
# → Day 1: wait 2 days for 75
# → Day 2: wait 1 day for 75
# → Day 3: no warmer day → 0

# -------------------- EXAMPLE USAGE --------------------
print(daily_temperatures([73, 74, 72, 75]))  # Output: [1, 2, 1, 0]
print(daily_temperatures([73, 80, 72, 75]))  # Output: [1, 0, 1, 0]


        
# Explanation of the daily_temperatures Code:
# "Let me walk you through my code for solving the daily temperatures problem."

# Initialization:

# First, I create a list called wait_time that has the same length 
# as the input temperatures list, 
# and I initialize it with zeroes. This list will store, for each day, 
# how many days we need to wait until we see a warmer temperature. 
# If no warmer day comes, the value will remain zero.

# Use waiting_days to Track Days Waiting for Warmer Temperatures:

# Next, I use a list called waiting_days to keep track of the indices of days that are
#  waiting for a warmer temperature. This helps me remember the days for which I haven't 
# yet found a warmer temperature.

# As I loop through each temperature in the list, I compare the current day's temperature 
# with the temperature at the index stored at the top of the waiting_days list.

# Check for Warmer Day:

# If the current day's temperature is warmer than the temperature of the day at the
#  top of waiting_days, this means we have found a warmer day for the day stored at the 
# top of the waiting_days list.

# I then pop that day's index from waiting_days and calculate how many days we had to 
# wait by subtracting their positions (i.e., i - prev_day).

# I update the corresponding position in the wait_time list with this value,
#  representing the number of days it took to find a warmer day.

# Repeat the Process:

# I continue to check in a while loop as long as there are elements in waiting_days
#  and the current temperature is warmer than the one at the top of the waiting_days.

# Once the waiting_days stack is either empty or the current temperature is no longer warmer,
#  I stop the process for that particular day.

# Add the Current Day's Index to waiting_days:

# After checking for warmer days, I push the current day's index onto the waiting_days list, 
# so that this day can "wait" for a warmer temperature on subsequent iterations.

# Handle Days with No Warmer Temperature:

# At the end of the loop, any index still remaining in the waiting_days list did 
# not find a warmer day ahead, so the corresponding value in wait_time stays zero.

# Return the Result:

# Finally, I return the wait_time list, which contains how many days each day had to
#  wait for a warmer temperature. If a day did not find a warmer temperature, its value will remain 0.


   
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
# print(daily_temperatures([73, 80, 72, 75]))  # Output: [1, 0, 1, 0]

# -------------------- TRACE EXPLANATION FOR INPUT [73, 80, 72, 75] --------------------
# Initial state:
# temperatures = [73, 80, 72, 75]
# answer       = [0, 0, 0, 0]  # result initialized to 0s
# stack        = []           # stack holds indices of unresolved temps

# Day 0 (i=0):
# current_temp = 73
# stack is empty → push 0
# stack = [0]
# answer = [0, 0, 0, 0]

# Day 1 (i=1):
# current_temp = 80
# compare with temperatures[stack[-1]] = temperatures[0] = 73
# 80 > 73 → pop 0 → answer[0] = 1 (1 - 0)
# push 1
# stack = [1]
# answer = [1, 0, 0, 0]

# Day 2 (i=2):
# current_temp = 72
# compare with temperatures[stack[-1]] = temperatures[1] = 80
# 72 < 80 → not warmer → push 2
# stack = [1, 2]
# answer = [1, 0, 0, 0]

# Day 3 (i=3):
# current_temp = 75
# compare with temperatures[stack[-1]] = temperatures[2] = 72
# 75 > 72 → pop 2 → answer[2] = 1 (3 - 2)
# compare with temperatures[stack[-1]] = temperatures[1] = 80
# 75 < 80 → stop
# push 3
# stack = [1, 3]
# answer = [1, 0, 1, 0]

# Final state:
# stack = [1, 3] → these had no warmer days ahead → their answer stays 0
# Final answer = [1, 0, 1, 0]

# -------------------- EXAMPLE USAGE --------------------

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

# ======================
def daily_temperatures(temperatures):
    """
    For each day, calculate how many days to wait for a warmer temperature.
    """

    # 📝 Create result list filled with 0 — by default assume no warmer day
    wait_time = [0] * len(temperatures)

    # ⏳ Waiting_days to store indices of days waiting for a warmer day
    waiting_days = []

    # 🔄 Loop through each day's temperature
    for i in range(len(temperatures)):
        current_temp = temperatures[i]  # 🌡 Get the temperature for the current day (index i)

        # 🔥 Check if current_temp is warmer than the day at top of waiting_days
        while waiting_days and current_temp > temperatures[waiting_days[-1]]:
            prev_day = waiting_days.pop()  # 🔽 Remove the index from top of waiting_days
            wait_time[prev_day] = i - prev_day  # 🕒 Calculate how many days we waited

            # 📍 **Trace for input [73, 80, 72, 75]:**
            # When i=1 (74):
            #   waiting_days=[0], temperatures[0]=73
            #   74 > 73 → pop 0 → wait_time[0]=1
            #
            # When i=3 (75):
            #   waiting_days=[1,2], temperatures[2]=72
            #   75 > 72 → pop 2 → wait_time[2]=1
            #   75 > 74 → pop 1 → wait_time[1]=2

        # ⬆️ Push current day's index onto waiting_days
        waiting_days.append(i)
        
        # 📊 **Trace for [73, 80, 72, 75]**
        
        # 1️⃣ **First iteration (i = 0, num = 73)**: 
        #   - current_temp = 73
        #   - 73 is not in waiting_days, so we add 73 to waiting_days.
        #   - waiting_days = [0], wait_time = [0, 0, 0, 0] (no change)

        # 2️⃣ **Second iteration (i = 1, num = 80)**: 
        #   - current_temp = 80
        #   - 80 > 73 (temperature at index 0 in waiting_days).
        #   - Pop index 0 from waiting_days and calculate how many days `73` had to wait:
        #     - wait_time[0] = 1 - 0 = 1
        #   - waiting_days = [], wait_time = [1, 0, 0, 0]
        #   - Add index 1 to waiting_days.
        #   - waiting_days = [1]

        # 3️⃣ **Third iteration (i = 2, num = 72)**: 
        #   - current_temp = 72
        #   - 72 is not greater than 80 (temperature at index 1 in waiting_days).
        #   - Add 72 to waiting_days without popping anything.
        #   - waiting_days = [1, 2], wait_time = [1, 0, 0, 0] (no change)

        # 4️⃣ **Fourth iteration (i = 3, num = 75)**: 
        #   - current_temp = 75
        #   - 75 > 72 (temperature at index 2 in waiting_days).
        #   - Pop index 2 from waiting_days and calculate how many days `72` had to wait:
        #     - wait_time[2] = 3 - 2 = 1
        #   - waiting_days = [1], wait_time = [1, 0, 1, 0]
        #   - 75 > 74 (temperature at index 1 in waiting_days).
        #   - Pop index 1 from waiting_days and calculate how many days `74` had to wait:
        #     - wait_time[1] = 3 - 1 = 2
        #   - waiting_days = [], wait_time = [1, 2, 1, 0]
        #   - Add index 3 to waiting_days.
        #   - waiting_days = [3]

    # 🔚 Return the result list — any days left in waiting_days had no warmer day ahead, so stay 0
    return wait_time

# Example calls:
print(daily_temperatures([73, 80, 72, 75]))  # Expected output: [1, 0, 1, 0]
