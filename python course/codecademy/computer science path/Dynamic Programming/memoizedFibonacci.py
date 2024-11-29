memo = {}

def fibonacci(num):
  answer = None
  
  if num in memo:
    answer = memo[num]
    return answer
  elif num == 0 or num == 1:
    answer = num
  else:
    answer = fibonacci(num - 1) + fibonacci(num - 2)
    memo[num] = answer

  print(memo)
  return answer


print(fibonacci(20))
# print(fibonacci(200))