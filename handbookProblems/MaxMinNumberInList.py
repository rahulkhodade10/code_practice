# Find max and min unsorted list
# 1 By using min,max function
my_list = [2, 6, 8, 14, 3, 77, 63]
print(min(my_list))
print(max(my_list))


# 2 Without using function
# Pass a list to this function to check for maximum number
def max_check(x):
  max_val = x[0]
  for check in x:
    if check > max_val:
      max_val = check
  return max_val

# Pass a list to this function to check for minimum number
def min_check(x):
  min_val = x[0]
  for check in x:
    if check < min_val:
      min_val = check
  return min_val


print("Maximum of the list", max_check(my_list))
print("Minimum of the list", min_check(my_list))