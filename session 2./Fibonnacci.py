n = input('Introduce the number of the Fibonacci´s series that you want to know: ')
n=int(n)
def fib(n):
    a,b=1,1
    for i in range (n-2):
        a,b=b,a+b
    return a
print(fib(n))