# Questions to be asked 
#  👉 “Can I assume the list contains only integers?”
#  👉 “Does the list need to stay in the same order in the output?”
#  👉 “Is using extra space like a set or dictionary okay, or should I avoid extra space?”
#  👉 Confirming that duplicate will occure only atmost twice in input”

# Note: if an element occures more than 2 times it will appear in this program as many times it comes 
# if 3 times it is there it will in out put 2 times
# if it is 4 times it will be in out put 3 times

# Approch i will follow 
# I will go through the list one number at a time. 
# I will keep track of the numbers I have already seen using a set.
# If I come across a number that I have already seen, I will add it to another list for duplicates. 
# In the end, I will return the list of numbers that appeared more than once. 

def find_duplicates(nums):
    """
    This function finds duplicate elements in a list of integers.
    If no duplicates are found, it returns [].

    Parameters:
    nums (List[int]): The input list to check for duplicates.

    Returns:
    List[int]: A list containing the duplicates found or [-1] if none found.
    """

    seen = []       # This list will store numbers we have seen so far.
    duplicates = [] # This list will store numbers that are duplicates.

    # Loop through each number in the input list
    for num in nums:
        if num in seen:
            duplicates.append(num)
            # We've seen this number before — it's a duplicate.
        else:
            seen.append(num)
            # First time seeing this number — add to seen.

        # Example trace for [1, 2, 4, 2]:
        # num = 1 → not in seen → add to seen → seen = {1}, duplicates = {}
        # num = 2 → not in seen → add to seen → seen = {1, 2}, duplicates = {}
        # num = 4 → not in seen → add to seen → seen = {1, 2, 4}, duplicates = {}
        # num = 2 → in seen → add to duplicates → seen = {1, 2, 4}, duplicates = {2}

    # If no duplicates found, return empty list []
    if not duplicates:
        return [] # if asked to return [-1] array than return [-1]

    # Otherwise, return the duplicates as a list
    return duplicates

# Example calls
print(find_duplicates([1, 2, 4, 2]))  # Expected output: [2]
print(find_duplicates([1, 2, 3, 4]))  # Expected output: [] (no duplicates)

# Trace table for input [1, 2, 4, 2]:
# +------------+---------+----------------+--------------------+---------------------------+-----------------+-------------------+
# | Iteration  | num     | seen before     | duplicates before   | action                    | seen after       | duplicates after   |
# +------------+---------+----------------+--------------------+---------------------------+-----------------+-------------------+
# | 1          | 1       | {}              | {}                  | add 1 to seen             | {1}              | {}                |
# | 2          | 2       | {1}             | {}                  | add 2 to seen             | {1, 2}           | {}                |
# | 3          | 4       | {1, 2}          | {}                  | add 4 to seen             | {1, 2, 4}        | {}                |
# | 4          | 2       | {1, 2, 4}       | {}                  | 2 in seen → add to dupes  | {1, 2, 4}        | {2}               |
# +------------+---------+----------------+--------------------+---------------------------+-----------------+-------------------+


# 🎤 Time complexity
# 👉 “The time complexity is O(N), where N is the number of elements in the input list. 
# That’s because we go through the list once, and for each element, 
# we either check if it’s in the list or add it to the list — both of which are O(1) on average. 
# So overall, we do about 2N constant-time operations — one lookup and possibly one insert for 
# each number — which is still O(N).”
# 🎤 Space complexity
# 👉 “The space complexity is O(N) because in the worst case, if all numbers are unique, 
# we store all of them in the list  . We also have the duplicates list, 
# but it would at most contain N elements too in the extreme case where all numbers are duplicates. 
# So overall, the space used is O(N)
# 
# Improvement
#I would replace the seen list with a set because checking if a number is in a set is very fast —
#  it takes the same short time no matter how big the set is. But with a list, 
# the program has to look through each item one by one, so it takes longer as the list gets bigger. Using a set would make the program work faster, especially if we have a lot of numbers.
# Checking membership in a set is O(1) on average,
#  while checking in a list is O(N). This change would make the program much more efficient, 
#  especially for large lists.
# in this case seen.append() will be changed to seen.add()
# # =======================
# Example trace for [1, 2, 3, 4]:

def find_duplicates(nums):
    """
    Finds duplicate elements in a list of integers.
    If no duplicates found, returns [-1].

    Parameters:
    nums (List[int]): The input list.

    Returns:
    List[int]: A list of duplicates or [-1].
    """

    seen = []
    duplicates = []

    for num in nums:
        if num in seen:
            duplicates.append(num)
        else:
            seen.append(num)

        # Example trace for [1, 2, 3, 4]:
        # num = 1 → not in seen → add to seen → seen = {1}, duplicates = {}
        # num = 2 → not in seen → add to seen → seen = {1, 2}, duplicates = {}
        # num = 3 → not in seen → add to seen → seen = {1, 2, 3}, duplicates = {}
        # num = 4 → not in seen → add to seen → seen = {1, 2, 3, 4}, duplicates = {}

    if not duplicates:
        return []

    return duplicates

# Example calls
print(find_duplicates([1, 2, 3, 4]))  # Expected: [-1]
