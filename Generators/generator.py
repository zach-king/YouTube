

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
        yield a

fibGenerator = fibonacci(10000)
for i in range(10):
    # First 10 fib. numbers
    print(next(fibGenerator))

inline = (x**2 for x in range(2, 10))
print(next(inline)) # First square in range(2, 10)