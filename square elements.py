# Write a python program  to square the elements of a list using map() functions.

# sample_num(n): [4, 5, 2, 9]

def square_num(n):
    return n*n
nums = [4, 5, 2, 9]
print("original list: ",nums)
result = map(square_num, nums)
print("square the elements of the said list using map():")
print(list(result))
