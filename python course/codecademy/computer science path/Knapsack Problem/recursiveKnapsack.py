# O(2^n) time complexity
def recursive_knapsack(weight_cap, weights, values, i):
  if weight_cap == 0 or i == 0:
    return 0
  elif weights[i - 1] > weight_cap:
    return recursive_knapsack(weight_cap, weights, values, i - 1)
  else:
    include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1)

    exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1)

    return max(include_item, exclude_item)
  

weight_cap = 5 
weights = [1, 3, 5]
values = [250, 300, 500]

print(recursive_knapsack(weight_cap, weights, values, len(weights)))