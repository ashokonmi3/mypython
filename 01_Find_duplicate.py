# Questions to be asked 
#  👉 “Can I assume the list contains only integers?”
#  👉 “Do you want all duplicates listed once, or do you want a count of how many times each 
#      number is duplicated?”
#  👉 “Does the list need to stay in the same order in the output?”
#  👉 “What if there is no duplicate can i return 0 or -1”
#  👉 “Is using extra space like a set or dictionary okay, or should I avoid extra space?”


# Approch i will follow 
# I will go through the list one number at a time. 
# I will keep track of the numbers I have already seen using a set.
#  If I come across a number that I have already seen, I will add it to another list for duplicates. 
# In the end, I will return the list of numbers that appeared more than once. 

def find_duplicates(nums):
    """
    This function finds duplicate elements in a list of integers.
    If no duplicates are found, it returns [-1].

    Parameters:
    nums (List[int]): The input list to check for duplicates.

    Returns:
    List[int]: A list containing the duplicates found or [-1] if none found.
    """

    seen = set()       # This set will store numbers we have seen so far.
    duplicates = set() # This set will store numbers that are duplicates.

    # Loop through each number in the input list
    for num in nums:
        if num in seen:
            duplicates.add(num)
            # We've seen this number before — it's a duplicate.
        else:
            seen.add(num)
            # First time seeing this number — add to seen.

        # Example trace for [1, 2, 4, 2]:
        # num = 1 → not in seen → add to seen → seen = {1}, duplicates = {}
        # num = 2 → not in seen → add to seen → seen = {1, 2}, duplicates = {}
        # num = 4 → not in seen → add to seen → seen = {1, 2, 4}, duplicates = {}
        # num = 2 → in seen → add to duplicates → seen = {1, 2, 4}, duplicates = {2}

    # If no duplicates found, return [-1]
    if not duplicates:
        return [-1]

    # Otherwise, return the duplicates as a list
    return list(duplicates)

# Example calls
print(find_duplicates([1, 2, 4, 2]))  # Expected output: [2]
print(find_duplicates([1, 2, 3, 4]))  # Expected output: [-1] (no duplicates)

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
# we either check if it’s in the set or add it to the set — both of which are O(1) on average. 
# So overall, we do about 2N constant-time operations — one lookup and possibly one insert for 
# each number — which is still O(N).”
# 🎤 Space complexity
# 👉 “The space complexity is O(N) because in the worst case, if all numbers are unique, 
# we store all of them in the seen set. We also have the duplicates set, 
# but it would at most contain N elements too in the extreme case where all numbers are duplicates. 
# So overall, the space used is O(N)
