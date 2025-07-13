# Questions to be asked 
#  👉 “Can I assume the list contains only integers?”
#  👉 “Any restriction on the datastucture i use ” - 
#  👉 Confirming that duplicate will occure only atmost twice in input” 
#      if more than 2 it will give n-1 occurance
#  👉 How much time i have to solve this problem”

# Note:  for this solution if an element occures more than 2 times it 
# will appear in this program as many times it comes 
# if 3 times it is there it will in out put 2 times
# if it is 4 times it will be in out put 3 times
# this will work on both sorted or unsorted list
# go slow little start 
# 👉 Approach: I am going to use 2 lists here and i will iterate through the input
# first List for seen element : This will store the numbers we've already
#  encountered
# while iterating through the list.
# let me think
# second List duplicates for storing the duplicate: This will store
#  the numbers that are 
# repeated (i.e., the duplicates).

# For each element in the list, check if it’s already in the seen list:
# If it is, add it to the duplicates list.
# If it’s not, add it to the seen list.
# Finally, i will return the duplicates list. 
# If no duplicates are found, return [].

def find_duplicates(nums):
    """
    This function finds duplicate elements in a list of integers.
    If no duplicates are found, it returns [].
    Parameters:
    nums (List[int]): The input list to check for duplicates.
    Returns:
    List[int]: A list containing the duplicates found or [] if none found.
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
        # num = 1 → not in seen → add to seen → seen = [1], duplicates = []
        # num = 2 → not in seen → add to seen → seen = [1, 2], duplicates = []
        # num = 4 → not in seen → add to seen → seen = [1, 2, 4], duplicates = []
        # num = 2 → in seen → add to duplicates → seen = [1, 2, 4], duplicates = [2]

        # Example trace for [1, 2, 3, 4]:
        # num = 1 → not in seen → add to seen → seen = [1], duplicates = []
        # num = 2 → not in seen → add to seen → seen = [1, 2], duplicates = []
        # num = 3 → not in seen → add to seen → seen = [1, 2, 3], duplicates = []
        # num = 4 → not in seen → add to seen → seen = [1, 2, 3, 4], duplicates = []


    # If no duplicates found, the code automatically return empty list []
    # this is not needed only if asked to return [-1] 
    
    # if not duplicates:
    #     return [-1] # if asked to return [-1] array than return [-1]

    # Otherwise, return the duplicates as a list
    return duplicates
       
# Example calls
print(find_duplicates([1, 2, 4, 2]))  # Expected output: [2]
print(find_duplicates([1, 2, 3, 4]))  # Expected output: [] (no duplicates)
# print(find_duplicates([1,2,2,3,2,4,5,4]))  # Expected output: [2,2,4] 
# (it will give multiple time as our req is to have max 2 element)



# Find an element in an array which is occuring exactly twice



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
# 👉 “The time complexity is O(N), where N is the number of elements in 
# the input list. 
# That’s because we go through the list once, and for each element, 
# we either check if it’s in the list or add it to the list — 
# both of which are O(1) on average. 
# So overall, we do about 2N constant-time operations — one lookup
#  and possibly one insert for 
# each number — which is still O(N).”
# 🎤 Space complexity
# 👉 “The space complexity is O(N) because in the worst case, 
# if all numbers are unique, 
# we store all of them in the list  . We also have the duplicates list, 
# but it would at most contain N elements too in the extreme case where all numbers 
# are duplicates. 
# So overall, the space used is O(N)
# 
# Improvement
#I would replace the seen list with a set because checking 
# if a number is in a set is very fast —
#  it takes the same short time no matter how big the set is.
#  But with a list, 
# the program has to look through each item one by one,
#  so it takes longer as the list gets bigger. Using a 
# set would make the program work faster, especially
#  if we have a lot of numbers.
# Checking membership in a set is O(1) on average,
#  while checking in a list is O(N). 
# This change would make the program much more efficient, 
#  especially for large lists.
# in this case seen.append() will be changed to seen.add()
# # =======================

