# Find the elements that occurs only 2 times 
# Approach:
# The goal is to find the numbers in a list that occur exactly two times.
# 1. Initialize an empty dictionary to store the count of each number.
# 2. Loop through the input list and count how many times each number appears.
# 3. Once we have the count of each number, loop through the dictionary and find the numbers that have a count of exactly 2.
# 4. Store those numbers in a list and return the list as the result.

def find_values_occurring_twice(nums):
    """
    This function finds values that occur exactly 2 times in the list.
    
    Parameters:
    nums (List[int]): The input list to check for occurrences.
    
    Returns:
    List[int]: A list containing elements that occur exactly 2 times.
    """
    
    # Step 1: Initialize an empty dictionary to store the count of each number
    count_dict = {}  # This will hold numbers as keys and their counts as values.
    
    # Step 2: Loop through the input list and count occurrences
    for num in nums:
        if num in count_dict:
            # If the number is already in the dictionary, increment its count by 1
            count_dict[num] += 1
        else:
            # If it's the first time the number appears, initialize its count to 1
            count_dict[num] = 1
    
    # Step 3: Initialize an empty list to store numbers that occur exactly 2 times
    result = []  # This list will store numbers that appear exactly twice
    
    # Step 4: Loop through the dictionary to check counts
    for num in count_dict:
        if count_dict[num] == 2:
            # If the count is 2, append the number to the result list
            result.append(num)
    
    # Step 5: Return the list of elements that occur exactly 2 times
    return result


# Example call to test the function
print(find_values_occurring_twice([1, 2, 4, 2]))  # Expected output: [2]

# Additional example call to test the function
print(find_values_occurring_twice([1, 2, 3, 4]))  # Expected output: [] (no duplicates)

# Iteration Trace for input [1, 2, 4, 2]:
# count_dict = {}
# Iteration 1: num = 1 → num is not in count_dict → add count_dict[1] = 1
# count_dict = {1: 1}
# Iteration 2: num = 2 → num is not in count_dict → add count_dict[2] = 1
# count_dict = {1: 1, 2: 1}
# Iteration 3: num = 4 → num is not in count_dict → add count_dict[4] = 1
# count_dict = {1: 1, 2: 1, 4: 1}
# Iteration 4: num = 2 → num is already in count_dict → increment count_dict[2] = 2
# count_dict = {1: 1, 2: 2, 4: 1}

# Now, we check the counts in count_dict:
# count_dict = {1: 1, 2: 2, 4: 1}
# 1 appears 1 time, so we skip it.
# 2 appears exactly 2 times, so it is added to result.
# 4 appears 1 time, so we skip it.
# Final result: [2]

# Iteration Trace for input [1, 2, 3, 4]:
# count_dict = {}
# Iteration 1: num = 1 → num is not in count_dict → add count_dict[1] = 1
# count_dict = {1: 1}
# Iteration 2: num = 2 → num is not in count_dict → add count_dict[2] = 1
# count_dict = {1: 1, 2: 1}
# Iteration 3: num = 3 → num is not in count_dict → add count_dict[3] = 1
# count_dict = {1: 1, 2: 1, 3: 1}
# Iteration 4: num = 4 → num is not in count_dict → add count_dict[4] = 1
# count_dict = {1: 1, 2: 1, 3: 1, 4: 1}

# Now, we check the counts in count_dict:
# count_dict = {1: 1, 2: 1, 3: 1, 4: 1}
# 1 appears 1 time, so we skip it.
# 2 appears 1 time, so we skip it.
# 3 appears 1 time, so we skip it.
# 4 appears 1 time, so we skip it.
# Final result: []

# Time Complexity:
# 1. Counting occurrences: The loop that counts the occurrences takes O(n) time, where n is the length of the list.
# 2. Finding elements with exactly 2 occurrences: The loop that checks the dictionary also takes O(m) time, where m is the number of unique elements in the dictionary (in practice, m <= n).
# Therefore, the overall time complexity is O(n), as both loops run sequentially and at most we will loop through the list and dictionary.
#
# Space Complexity:
# 1. The dictionary stores counts for each unique element, which takes O(n) space in the worst case (if all elements are unique).
# 2. The result list will contain a subset of elements, which is also O(n) in the worst case (if all elements appear exactly 2 times).
# Thus, the space complexity is O(n).

