# 🎤 Questions to ask before coding
# 👉 “Is the list guaranteed to be sorted, or can it be unsorted?”
# 👉 “What should I return if the target isn’t found — [-1, -1] okay?” [Ask only if not provided in input]
# 👉 “Is it possible to have multiple instances of the target?”
# 👉 How much time i have to solve this problem


#🎤 Approach in simple language
#👉 “I loop through the list with a basic index-based loop. 
# If I see the target, I set the first index if it hasn’t been set yet, 
# and I keep updating the last index. This way I track both positions efficiently.”

def find_first_last_indices(nums, target):
    """
    Finds the first and last index where target appears in nums.

    Parameters:
    nums (List[int]): The input list of integers.
    target (int): The number to search for.

    Returns:
    List[int]: [first_index, last_index] or [-1, -1] if target not found.
    """

    first_index = -1  # Default if target not found
    last_index = -1

    # Loop through the list using index
    for i in range(len(nums)):
        num = nums[i]

        if num == target:
            if first_index == -1:
                first_index = i  # First time we see target
            last_index = i       # Always update last seen index

        # Trace for [5, 7, 7, 8, 8, 10], target = 8
        # i=0, num=5 → not target → first=-1, last=-1
        # i=1, num=7 → not target → first=-1, last=-1
        # i=2, num=7 → not target → first=-1, last=-1
        # i=3, num=8 → first=-1 → set first=3, last=3
        # i=4, num=8 → update last=4
        # i=5, num=10 → not target → first=3, last=4


      
    return [first_index, last_index]

# Example calls
print(find_first_last_indices([5, 7, 7, 8, 8, 10], 8))  # Expected: [3, 4]
print(find_first_last_indices([5, 7, 7, 8, 8, 10], 6))  # Expected: [-1, -1]

# 🎤 Time complexity
# 👉 “The time complexity is O(N), where N is the number of elements in the list.
#  This is because we go through the list once from start to end, checking each element exactly once.”

# 🎤 Space complexity
# 👉 “The space complexity is O(1) because we only use a few variables (first_index, last_index) 
# regardless of the input size. We don’t use any extra data structures that grow with the input.”
# =================================
# [5, 7, 7, 8, 8, 10], target = 6:

def find_first_last_indices(nums, target):
    """
    Finds the first and last index where target appears in nums.

    Parameters:
    nums (List[int]): The input list of integers.
    target (int): The number to search for.

    Returns:
    List[int]: [first_index, last_index] or [-1, -1] if target not found.
    """

    first_index = -1  # Initialize first_index to -1 (default if target not found)
    last_index = -1   # Initialize last_index to -1 (default if target not found)

    # Loop through the list using index
    for i in range(len(nums)):
        num = nums[i]  # Get the current number at index i

        if num == target:
            # If this is the first occurrence of target
            if first_index == -1:
                first_index = i  # Set first_index to current index

            # Update last_index to current index (will keep updating as we find more occurrences)
            last_index = i

        # Example trace for [5, 7, 7, 8, 8, 10], target = 6:
        # i = 0, num = 5 → not target → first_index = -1, last_index = -1
        # i = 1, num = 7 → not target → first_index = -1, last_index = -1
        # i = 2, num = 7 → not target → first_index = -1, last_index = -1
        # i = 3, num = 8 → not target → first_index = -1, last_index = -1
        # i = 4, num = 8 → not target → first_index = -1, last_index = -1
        # i = 5, num = 10 → not target → first_index = -1, last_index = -1


        # Example trace for [], target = 6:
        # The list is empty → len(nums) = 0
        # The loop does not run at all → first_index = -1, last_index = -1
        # No elements to check → directly return [-1, -1]

    # Return the first and last indices as a list
    return [first_index, last_index]

# Example call 1: target is present
# Expected output: [3, 4] because 8 appears at index 3 and 4

# Example call 2: target is not present
# Expected output: [-1, -1] because 6 does not appear in the list
print(find_first_last_indices([5, 7, 7, 8, 8, 10], 6))
print(find_first_last_indices([], 6))

