# 🎤 1️⃣ Clarifying questions to ask before coding
# 👉 These show that you’re thoughtful and not jumping into code blindly:
# 🟣 Are the input lists always sorted in ascending order?
#  (This affects merge logic.)


# 🟣 Do I need to handle duplicates, or should the merged list remove them?
#  (If not specified, keep all elements.)


# 🟣 Should I return a new list, or modify one of the input lists in-place?
#  (Could save space if in-place is allowed.)


# 🟣 What should happen if one or both lists are empty?
#  (Clarify edge cases.)


# 🟣 Is there a constraint on list sizes (e.g. very large lists)?
#  (Optimization matters more if lists are huge.)

# 🎤 How to explain this in interview
# 👉 “I compare one element at a time from both lists and add the smaller one to the merged list. 
# If they’re equal, I choose either; here we pick from list2 first. 
# When one list finishes, I add the remaining elements from the other list.”



def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    """

    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

        # Trace for l1 = [1,2,4], l2 = [1,3,4]
        # Step 1: list1[0]=1, list2[0]=1 → take list2[0]=1 → merged=[1], j=1
        # Step 2: list1[0]=1, list2[1]=3 → take list1[0]=1 → merged=[1,1], i=1
        # Step 3: list1[1]=2, list2[1]=3 → take list1[1]=2 → merged=[1,1,2], i=2
        # Step 4: list1[2]=4, list2[1]=3 → take list2[1]=3 → merged=[1,1,2,3], j=2
        # Step 5: list1[2]=4, list2[2]=4 → take list2[2]=4 → merged=[1,1,2,3,4], j=3

    # Add remaining elements from list1 (if any)
    while i < len(list1):
        merged.append(list1[i])
        i += 1
        # Step 6: list1[2]=4 left → merged=[1,1,2,3,4,4]

    while j < len(list2):
        merged.append(list2[j])
        j += 1
        # No remaining elements in list2 for this input

    return merged

# Example call
l1 = [1, 2, 4]
l2 = [1, 3, 4]
print("Merged list:", merge_sorted_lists(l1, l2))

# 🎤 Time complexity
# 👉 “The time complexity is O(N + M), where N is the length of the first list and M is the length
#  of the second list. This is because we look at each element from both lists exactly once as we build the merged list.”

# 🎤 Space complexity
# 👉 “The space complexity is O(N + M) because we create a new merged list that contains all 
# elements from both input lists. We use extra space for this merged list, but no additional space that grows beyond that.”

