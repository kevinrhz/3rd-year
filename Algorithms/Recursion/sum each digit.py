def sum_digits(n):
  if n < 10:
    return n
  else:
    last_digit = n % 10
    
    return last_digit + sum_digits(n // 10)
  


  
  ex1 = sum_digits(12)
  # 3
  ex2 = sum_digits(194)
  # 14

  print(sum_digits(18374859))

  print(ex1)
  print(ex2)