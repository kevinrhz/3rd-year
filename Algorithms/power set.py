# Let’s compare two solutions to a single problem: producing a power set. 
# A power set is a list of all subsets of the values in a list.

# Iterative approach
# def power_set(set):
#   power_set_size = 2**len(set)
#   result = []

#   for bit in range(0, power_set_size):
#     sub_set = []
#     for binary_digit in range(0, len(set)):
#       if((bit & (1 << binary_digit)) > 0):
#         sub_set.append(set[binary_digit])
#     result.append(sub_set)
#   return result


#Recursive approach
def power_set(my_list):
  if len(my_list) == 0:
    return [[]]
  power_set_without_first = power_set(my_list[1:])         #recursive step where the list is copied with one less element
  with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
  return with_first + power_set_without_first



#These algorithms run in O(2^N) so fun to test how quickly it becomes slow

universities = ['MIT', 'UCLA', 'Stanford', 'NYU', 'UOP', 'PIMP', 'KEVMO', 'DADDY', 'JOHN', 'SHREK', 'RICK', 'LONG', 'BATMAN', 'ROBIN', 'SPIDERMAN', 'THOR']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)


