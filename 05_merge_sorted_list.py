# 🎤 1️⃣ Clarifying questions to ask before coding
# 🟣 Are the input lists always sorted in ascending order?
#  (This affects merge logic.)

# 🟣 Lenght of both list will be same or it can be different as well?

# 🟣 Should I return a new list, or modify one of the input lists in-place?
#  (Could save space if in-place is allowed.)

# 🟣 How much time i have to solve this problem


# ✅ Approach (in simple language for interview):
# I start by comparing the first elements of both sorted lists.
# I always pick the smaller element and add it to the result list.
# Then I move to the next element in the list from which I picked the value.
# I continue this process until I reach the end of one of the lists.
# Once one list is finished, I simply add the remaining elements from the other list.
# Because the original lists are sorted, the final result is also sorted without needing extra sorting.

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    """

    merged = []  # This will hold the final sorted merged result
    i = 0        # Pointer to track current index in list1
    j = 0        # Pointer to track current index in list2

    # Compare elements of both lists one by one
    while i < len(list1) and j < len(list2):
        # If current element in list1 is smaller, add it to merged list
        if list1[i] < list2[j]:
            merged.append(list1[i])  # Add smaller element from list1
            i += 1  # Move to next element in list1
        else:
            merged.append(list2[j])  # Add smaller or equal element from list2
            j += 1  # Move to next element in list2

        # 🔄 Example trace for list1 = [1, 2, 4], list2 = [1, 3, 4]
        # Initial: i=0, j=0 → list1[0]=1, list2[0]=1 → take list2[0]=1 → merged=[1] → i=0, j=1
        # Step 2: i=0, j=1 → list1[0]=1, list2[1]=3 → take list1[0]=1 → merged=[1,1] → i=1, j=1
        # Step 3: i=1, j=1 → list1[1]=2, list2[1]=3 → take list1[1]=2 → merged=[1,1,2] → i=2, j=1
        # Step 4: i=2, j=1 → list1[2]=4, list2[1]=3 → take list2[1]=3 → merged=[1,1,2,3] → i=2, j=2
        # Step 5: i=2, j=2 → list1[2]=4, list2[2]=4 → take list2[2]=4 → merged=[1,1,2,3,4] → i=2, j=3
        # Remaining: j=3 (end), but list1 still has i=2 → take list1[2]=4 → merged=[1,1,2,3,4,4] → i=3, j=3


    # Add remaining elements from list1 if any
    while i < len(list1):
        merged.append(list1[i])
        i += 1
        # Step 6: list1[2]=4 is left → merged becomes [1,1,2,3,4,4]

    # Add remaining elements from list2 if any
    while j < len(list2):
        merged.append(list2[j])
        j += 1
        # (For this input, list2 is already exhausted, so this won't run)

    return merged  # Return the final sorted merged list

# 🔽 Example usage:
l1 = [1, 2, 4]
l2 = [1, 3, 4]
print("Merged list:", merge_sorted_lists(l1, l2))
# Output: Merged list: [1, 1, 2, 3, 4, 4]

# Explaination
# ▶️ This function merges two sorted lists into one sorted list.
# ▶️ It's designed to work without using Python’s built-in sort function.

# ✅ Step 1: Function definition
# The function is named merge_sorted_lists and takes two sorted lists as input.

# ✅ Step 2: Initialize result and pointers
# We create an empty list called 'merged' to store the final sorted result.
# We also initialize two pointers: 'i' for list1 and 'j' for list2, both starting at 0.

# ✅ Step 3: Begin merging
# We use a while loop to compare elements from both lists as long as neither list is finished.
# If list1's current element is smaller, we add it to 'merged' and move 'i' forward.
# Otherwise, we add the element from list2 and move 'j' forward.
# This ensures that the smallest available element from both lists is added each time.

# ✅ Step 4: Handle remaining elements
# Once one list is completely traversed, we exit the loop.
# We then check if list1 has any remaining elements — if yes, we add them all to 'merged'.
# We do the same for list2 if it has remaining elements.
# This ensures no element is left out of the final result.

# ✅ Step 5: Return result
# Finally, we return the 'merged' list, which contains all elements from both input lists in sorted order.

# =================
# ✅ Time Complexity:
# O(n + m), where n and m are the sizes of the two input lists.

# ✅ Space Complexity:
# O(n + m), because we create a new list to store the merged result.



# ✅ Time Complexity (with N = total number of elements in both lists):
# Let N = n + m, where n is the size of list1 and m is the size of list2.
# We go through each element from both lists once.
# So total operations = N (adding one element at a time to the merged list).
# ➤ Time Complexity = O(N)

# ✅ Space Complexity (with N = total number of elements in both lists):
# We are storing the merged result in a new list that contains all elements from both input lists.
# So we are using space proportional to N.
# ➤ Space Complexity = O(N)

# 💡 Summary:
# This algorithm is very efficient because it processes each element only once (linear time).
# It doesn't modify the original lists and builds a new sorted list from two sorted inputs.

