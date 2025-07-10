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
# ==============
#first iteration i= 0, current_temp=73, stack=[0], answer=[0,0,0,0]
#2nd iteration , i=1 , current_temp=74, 74>73, prev_day=0, answer[0]=1-0=1 --> answer=[1,0,0,0], stack=[1],i=2
#3rd iteration,i=2, current_temp=72, 72>74, stack =[1,2] , i=3, answer= [1,0,0,0]
#4th iteration,i=3, current_temp=75 > 72
                    # prev_day =2
					# answer[2] =3-2=1  ---> answer=[ 1,0,1,0]
					
					# current_temp=75>74
					# prev_day=1
					# answer[1]=3-1=2----> answer=[1,2,1,0]


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

# 1. Initialization:
# - The function takes an input list 'temperatures', where each element represents the temperature of a particular day.
# - A list called 'answer' is initialized with the same length as 'temperatures', filled with zeroes.
#   This will store, for each day, how many days you need to wait for a warmer temperature.
#   If no warmer day is ahead, the value remains 0.

# 2. Using a Stack to Track Days Waiting for Warmer Temperatures:
# - A stack (a list) called 'stack' is used to keep track of the indices of days that are waiting for a warmer temperature.
# - The stack helps track which days have been processed but haven't yet found a warmer temperature.
# - During each iteration, the temperature of the current day is compared to the temperature of the day stored at the top of the stack.

# 3. Checking for Warmer Day:
# - If the current day's temperature is warmer than the one at the top of the stack, it means the current day provides a warmer temperature for the day at the top of the stack.
# - The index of that cooler day is popped from the stack, and the wait time is calculated by subtracting the positions (i - prev_day).
# - The corresponding index in the 'answer' list is updated with this value, representing how many days the cooler day had to wait for a warmer temperature.

# 4. Repeat the Process:
# - The process continues in a while loop as long as there are indices in the stack and the current day's temperature is warmer than the one at the top of the stack.
# - For each condition, the cooler day's index is popped from the stack, and the wait time is updated in the 'answer' list.

# 5. Adding the Current Day's Index to the Stack:
# - After checking for warmer days, the current day's index is added to the stack.
# - This allows the current day to "wait" for a warmer temperature in subsequent iterations.

# 6. Handling Days with No Warmer Temperature:
# - At the end of the loop, any index left in the stack did not find a warmer temperature ahead.
# - For these days, their corresponding value in the 'answer' list remains 0, indicating that there is no warmer day ahead for them.

# 7. Returning the Result:
# - The 'answer' list is returned, containing how many days each day had to wait for a warmer temperature.
# - If a day did not find a warmer temperature, its value remains 0 in the 'answer' list.

# Example:
# Input: [73, 74, 72, 75]
# Output: [1, 2, 1, 0]


   
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
