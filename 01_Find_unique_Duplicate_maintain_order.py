def find_duplicates(nums):
    """
    This function finds duplicate elements in a list of integers.
    Each duplicate appears only once in the result, in the order they first appear as duplicates.
    If no duplicates are found, it returns [].

    Parameters:
    nums (List[int]): The input list of integers.

    Returns:
    List[int]: A list of unique duplicates in the order they first appear as duplicates.
    """

    seen = set()         # A set to store numbers we've seen so far (for fast lookup)
    duplicates = []      # A list to store unique duplicates in order of first appearance

    # Loop through each number in the input list
    for num in nums:
        if num in seen:
            # If num is already in seen set, it's a duplicate
            if num not in duplicates:
                # Add to duplicates list only if not already added
                duplicates.append(num)
        else:
            # First time seeing this num, add it to seen set
            seen.add(num)

        # Trace for input [1, 2, 4, 2]:
        # Iteration 1: num = 1
        #   1 not in seen -> add 1 to seen -> seen = {1}, duplicates = []
        # Iteration 2: num = 2
        #   2 not in seen -> add 2 to seen -> seen = {1, 2}, duplicates = []
        # Iteration 3: num = 4
        #   4 not in seen -> add 4 to seen -> seen = {1, 2, 4}, duplicates = []
        # Iteration 4: num = 2
        #   2 in seen -> 2 not in duplicates -> add 2 to duplicates -> seen = {1, 2, 4}, duplicates = [2]

        # Trace for input [1, 2, 3, 4]:
        # Iteration 1: num = 1
        #   1 not in seen -> add 1 to seen -> seen = {1}, duplicates = []
        # Iteration 2: num = 2
        #   2 not in seen -> add 2 to seen -> seen = {1, 2}, duplicates = []
        # Iteration 3: num = 3
        #   3 not in seen -> add 3 to seen -> seen = {1, 2, 3}, duplicates = []
        # Iteration 4: num = 4
        #   4 not in seen -> add 4 to seen -> seen = {1, 2, 3, 4}, duplicates = []

    # After looping through the list, return the duplicates list
    return duplicates  # If empty, means no duplicates were found

# Example calls:

# Input: [1, 2, 4, 2]
# Expected output: [2]
print(find_duplicates([1, 2, 4, 2]))

# Input: [1, 2, 3, 4]
# Expected output: []
print(find_duplicates([1, 2, 3, 4]))

