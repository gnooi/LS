# Pseudocode:
# Define a function with 1 parameter
# Set new_lst = []
# Set a count = 0
# Iterate through each element starting at index 1
# Add list[index] to count
# Append to running total
# return running_total

def running_total(nums):

    new_lst = []
    count = 0

    for num in nums:
        count += num
        new_lst.append(count)
    
    return new_lst

print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True