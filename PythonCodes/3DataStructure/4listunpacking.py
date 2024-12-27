numbers = [1, 2, 3]
first, second, third = numbers

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first, second, *other = nums
print(first)
print(other)

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
first, *other, last = nums1  # keep +other in between for first and last if want to get first and last exclusively
print(first, last)
print(other)