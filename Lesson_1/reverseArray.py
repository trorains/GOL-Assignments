# . Reverse Array In-place
# Write a function reverseArray(A) that takes in an array A and reverses it, without using another array or collection data structure; in-place.

# Example:

# A = [10, 5, 6, 9] reverseArray(A) A // [9, 6, 5, 10]
# Share the Github link to your solution.

# def reverseArray(lst):
#     reversal = lst[::-1]
#     return reversal
    


# names = [1, 2, "Lewis", "Peter"]
# print(reverseArray(names))

def reverseArray(lst):
    beginning = 0
    end = len(lst)-1


    while(beginning < end):
        # temp = lst[beginning]
        # lst[beginning] = lst[end]
        # lst[end] = temp
        lst[beginning],lst[end] = lst[end],lst[beginning]
        beginning = beginning+1
        end = end -1
    return lst
    


names = [1, 2, 3, 4]
print(reverseArray(names))