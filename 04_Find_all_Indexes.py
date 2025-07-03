# 🎤 Questions to ask before coding
# 👉 “Should I return all indices where the target appears or just the first one?”
# 👉 “If the target isn’t found at all, do you want an empty list or something else?”
# 👉 “Is the list always integers?”
# 👉 “Is the list always sorted or could it be unsorted?”

# 🎤 Approach in simple language
# 👉 “I will go through the list one number at a time. Every time I see the target number, 
# I will save its index in a result list. In the end, I will return this list of indices. If the target doesn’t appear at all, I will return an empty list.”

def find_all_indices(nums, target):
    """
    Finds all indices where target appears in nums.

    Parameters:
    nums (List[int]): The input list of integers.
    target (int): The number to find.

    Returns:
    List[int]: A list of indices where target appears. Empty list if not found.
    """

    # Initialize an empty list to store indices where target is found
    indices = []

    # Loop through the list using both index and value
    for i, num in enumerate(nums):

        # Check if current number is the target
        if num == target:
            # Add the index to our result list
            indices.append(i)

        # Example trace for [5, 7, 7, 8, 8, 10], target = 8:
        # i = 0, num = 5 → not equal → do nothing
        # i = 1, num = 7 → not equal → do nothing
        # i = 2, num = 7 → not equal → do nothing
        # i = 3, num = 8 → equal → indices = [3]
        # i = 4, num = 8 → equal → indices = [3, 4]
        # i = 5, num = 10 → not equal → do nothing

    # Return the list of indices found (could be empty if no target found)
    return indices

# Example call:
# Input: [5, 7, 7, 8, 8, 10], target = 8
# Expected output: [3, 4]
print(find_all_indices([5, 7, 7, 8, 8, 10], 8))

# 🎤 Time and space complexity
# 👉 “Time complexity is O(N) because we look at each element once. Space complexity is O(N) because in the worst case, if every number matches the target, we could store up to N indices in the list.”

