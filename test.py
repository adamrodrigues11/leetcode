data = [75, 100, 34, 72, 23, 86, 98, 38]

def min_max(arr):
  """
  Take a non-empty array of integers, and return the min and max values as a tuple (max, min).
  """
  curr_min = arr[0]
  curr_max = arr[0]
  for i in range(1, len(arr)):
    if arr[i] > curr_max:
      curr_max = arr[i]
    elif arr[i] < curr_min:
      curr_min = arr[i]
  return curr_max, curr_min

result = min_max(data)
print(result)
print(type(result))

my_set = set([1, 2, 3])
print(my_set.pop())