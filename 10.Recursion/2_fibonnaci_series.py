def fibonnaci(n):
    sum = 1
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
    
print(fibonnaci(0))
print(fibonnaci(1))
print(fibonnaci(2))
print(fibonnaci(3))
print(fibonnaci(4))
print(fibonnaci(5))
print(fibonnaci(6))
