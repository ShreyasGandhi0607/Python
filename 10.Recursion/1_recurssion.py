# fsctorial example is good one  for the recurssion 
# For example 
# 5! = 5*4*3*2*1
# factorial(n) = n * factorial(n-1)

def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

# how recurssion works 
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1