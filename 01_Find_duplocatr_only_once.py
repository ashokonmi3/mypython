
# In this code doesnot matter how many time the value occures it will give only once in output
def find_duplicates(nums):
    """
    This function finds duplicate elements in a list of integers.
    Each duplicate appears only once in the result.
    If no duplicates are found, it returns [].

    Parameters:
    nums (List[int]): The input list to check for duplicates.

    Returns:
    List[int]: A list containing unique duplicates or [] if none found.
    """

    seen = set()         # Use a set for faster lookup of seen numbers
    duplicates = set()   # Use a set to store unique duplicates

    # Start looping through each number in nums
    for num in nums:
        if num in seen:
            # If we've seen this number before, it's a duplicate — add to duplicates set
            duplicates.add(num)
        else:
            # First time seeing this number — add to seen set
            seen.add(num)

        # Example trace for input [1, 2, 4, 2]:
        # Iteration 1: num = 1
        #   1 not in seen -> add 1 to seen -> seen = {1}, duplicates = {}
        # Iteration 2: num = 2
        #   2 not in seen -> add 2 to seen -> seen = {1, 2}, duplicates = {}
        # Iteration 3: num = 4
        #   4 not in seen -> add 4 to seen -> seen = {1, 2, 4}, duplicates = {}
        # Iteration 4: num = 2
        #   2 in seen -> add 2 to duplicates -> seen = {1, 2, 4}, duplicates = {2}

        # Example trace for input [1, 2, 3, 4]:
        # Iteration 1: num = 1
        #   1 not in seen -> add 1 to seen -> seen = {1}, duplicates = {}
        # Iteration 2: num = 2
        #   2 not in seen -> add 2 to seen -> seen = {1, 2}, duplicates = {}
        # Iteration 3: num = 3
        #   3 not in seen -> add 3 to seen -> seen = {1, 2, 3}, duplicates = {}
        # Iteration 4: num = 4
        #   4 not in seen -> add 4 to seen -> seen = {1, 2, 3, 4}, duplicates = {}

    # After looping through, check if we found any duplicates
    if not duplicates:
        return []  # No duplicates found

    # Convert the duplicates set to a list and return
    return list(duplicates)

# Example calls:
print(find_duplicates([1, 2, 4, 2]))        # Expected output: [2] (order may vary)
print(find_duplicates([1, 2, 3, 4]))        # Expected output: []
print(find_duplicates([1, 2,4,4,4, 3, 4]))        # Expected output: [4]

