# ✅ Questions to ask interviewer before writing code:
# 1️⃣ Is the list guaranteed to have only integers (temperatures)?
# 2️⃣ What should I return if all temperatures are the same? (Return all 0s?)
# 3️⃣ Can the input list be empty?
# 4️⃣ Are negative temperatures possible, or only positive?
# How much time i have for this 

# Approach in simple language
# 👉 “I go through the list of temperatures one day at a time. 
# I use a stack to remember the days where I’m still waiting for a warmer temperature.
# Whenever I find a warmer temperature than a previous day stored on the stack, 
# I calculate how many days I had to wait by subtracting the indices. 
# I fill this value into the result list.
# If I don’t find a warmer temperature for a day, 
# I leave its value as zero, since we initialized the answer list with zeros. 
# This approach is efficient because each day’s index goes into the stack once 
# and comes out once.”

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
        current_temp = temperatures[i]  # 
        # Get the temperature for the current day (index i)

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
        # [73, 74, 72, 75]
        #first iteration i= 0, current_temp=73, stack=[0], answer=[0,0,0,0]
        #2nd iteration , i=1 , current_temp=74, 74>73, prev_day=0, 
        # answer[0]=1-0=1 --> answer=[1,0,0,0], stack=[1],i=2
        #3rd iteration,i=2, current_temp=72, 72>74, stack =[1,2] , i=3, answer= [1,0,0,0]
        #4th iteration,i=3, current_temp=75 > 72
                    # prev_day =2
					# answer[2] =3-2=1  ---> answer=[ 1,0,1,0]
					
					# current_temp=75>74
					# prev_day=1
					# answer[1]=3-1=2----> answer=[1,2,1,0]

        
# "Let me walk you through my code for solving the daily temperatures problem.

# First, I create a list called answer that has the same length as the input temperatures list, and I fill it with zeroes. This list will store, for each day, how many days we need to wait until we see a warmer temperature. If no warmer day comes, the value stays zero.

# Next, I use a stack to keep track of the indices of days that are waiting for a warmer temperature. As I loop through each temperature in the list, I compare the current day’s temperature with the temperature at the index stored at the top of the stack.

# If the current day’s temperature is warmer, that means we’ve found a warmer day for the previous day stored in the stack. I pop that day’s index from the stack, calculate how many days we had to wait by subtracting their positions, and I update the answer list for that day.

# I repeat this check in a while loop until either the stack is empty or the current temperature is not warmer than the one at the top of the stack.

# After that, I push the current day’s index onto the stack so it can wait for its future warmer day.

# At the end of the loop, any index still in the stack did not get a warmer day, so the corresponding value in answer stays zero.
# Finally, I return the answer list."

    # Return the result list — any days left in stack had no warmer day ahead, so stay 0
    return answer

# Example call
print(daily_temperatures([73, 74, 72, 75]))  # Expected output: [1, 2, 1, 0]
print(daily_temperatures([73, 80, 72, 75]))  # Expected output: [1, 0, 1, 0]

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
