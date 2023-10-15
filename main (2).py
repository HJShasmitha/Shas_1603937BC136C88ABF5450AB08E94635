def fact_gen(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_gen(n-1)
    
    number = int(input("Enter a number:"))
    
    res = fact_rec(number)
    print("The factorial of {} is {}.".format(number,res))
