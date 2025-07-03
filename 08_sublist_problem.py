# 🎯 About the sublist definition
# 👉 “Should the sublist start and end with N and have no N in between, or is it okay if there are other Ns inside?”
# 👉 “If multiple sublists are tied for shortest or longest, do you want all of them or just one?”

# 📝 About the output
# 👉 “Do you want me to return just the sublist elements, or also their start and end indices?”
# 👉 “If no valid sublist is found, what should I return — empty list, None, or an error message?”

# ⚡ About constraints
# 👉 “Can I assume the list has at least one N, or do I need to handle lists where N is missing?”
# 👉 “Can the list be large (e.g., thousands of elements), or is efficiency not a major concern here?”

# 📌 About additional requirements
# 👉 “Should I print the results or just return them from the function?”
# 👉 “Do you want the solution to handle negative numbers or just positive integers?”

# ==================
# Approch 
# “My approach is to first loop through the list to find positions where N occurs. For each such start, 
# I’ll look for end positions where N appears again, making sure no N appears in between. I’ll collect all valid sublists, 
# then use min and max by length to find the shortest and longest. I’ll return these as the result.”




def find_shortest_longest_sublists(lst, N):
    """
    Finds all sublists that:
    - start with N
    - end with N
    - have no N in between
    Returns the shortest and longest such sublists.
    """

    sublists = []  # This will store all valid sublists we find

    # Loop over the list to find starting positions where value == N
    for start in range(len(lst)):
        if lst[start] == N:
            # From each valid start position, look for an end position
            for end in range(start + 1, len(lst)):
                if lst[end] == N:
                    # Check if N appears between start+1 and end-1
                    # We want no N between start and end
                    if N not in lst[start + 1:end]:
                        # If valid, add the sublist (including end) to our list
                        sublists.append(lst[start:end + 1])

    # If no valid sublists were found, return empty lists
    if not sublists:
        return [], []

    # Find the shortest sublist using min + length as key
    shortest = min(sublists, key=len)

    # Find the longest sublist using max + length as key
    longest = max(sublists, key=len)

    # Return both sublists
    return shortest, longest

# Example usage
lst = [3, 1, 2, 3, 4, 3, 5, 3, 6, 3, 7]  # Our input list
N = 3                                     # Target number

# Call the function to get shortest and longest valid sublists
shortest, longest = find_shortest_longest_sublists(lst, N)

# Print the shortest sublist result
print(f"Shortest sublist: {shortest}")

# Print the longest sublist result
print(f"Longest sublist: {longest}")
# ==================
# ---------------------------------------------------------------
# Complexity Analysis
# ---------------------------------------------------------------
# Time Complexity:
# - Outer loop runs O(N): we look at each index as potential start
# - Inner loop runs O(N): for each start, we look for end points
# - For each (start, end) pair, we check if N is in lst[start+1:end]
#   which takes O(N) time in the worst case (length of sublist)
# - So total time complexity is:
#   O(N) * O(N) * O(N) = O(N^3)
#
# Space Complexity:
# - We store all valid sublists
# - In the worst case, there could be O(N^2) sublists if many pairs of N exist
# - Each sublist could be up to O(N) long, but overall space is driven by
#   the number of sublists: O(N^2)
#
# Summary:
#   Time: O(N^3)
#   Space: O(N^2)
# ---------------------------------------------------------------
