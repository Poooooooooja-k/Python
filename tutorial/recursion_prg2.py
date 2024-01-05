# f0=0
# f1=1
# f2=f1+f0
# f(n)=f(n-1)+f(n-2)
# fibonacci sequence
def fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=5
for i in range(n):
    print(fibonacci(i))