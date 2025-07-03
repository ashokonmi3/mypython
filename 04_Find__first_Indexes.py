# 🎤 Questions to ask before coding
# 👉 “Should I return all indices where the target appears or just the first one?”
#  👉 “If the target isn’t found at all, do you want an empty list or something else?”
#  👉 “Is the list always integers?”
#  👉 “Is the list always sorted or could it be unsorted?”

def find_first_index(nums, target):
    """
    Finds the index of the first occurrence of target in nums.
    
    Parameters:
    nums (List[int]): The input list of integers.
    target (int): The number to find.

    Returns:
    int: The index of the first occurrence of target, or -1 if not found.
    """

    # Loop through each index and value in nums
    for i, num in enumerate(nums):

        # Check if current number matches target
        if num == target:
            # Found the target, return its index
            return i

        # Example trace for input [5, 7, 7, 8, 8, 10], target = 8:
        # i = 0, num = 5 -> not equal to 8
        # i = 1, num = 7 -> not equal to 8
        # i = 2, num = 7 -> not equal to 8
        # i = 3, num = 8 -> equal to 8 -> return 3

    # Target not found after going through the list
    return -1

# Example call:
# Input: [5, 7, 7, 8, 8, 10], target = 8
# Expected output: 3 (first occurrence of 8 is at index 3)
print(find_first_index([5, 7, 7, 8, 8, 10], 8))

# 🎤 Time and space complexity
# 👉 “Time complexity is O(N) because in the worst case we may look at every element once. Space complexity is O(1) because we only use a few variables regardless of the input size.”