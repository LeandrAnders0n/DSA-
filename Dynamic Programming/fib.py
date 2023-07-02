#brute force with recursion
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))

#memoization
def fib_memo(n,memo={}):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    
    memo[n]= fib_memo(n-1)+fib_memo(n-2)
    return memo[n]


print(fib_memo(10))

#tabulation

def fib_tab(n):
    table=[0]*(n+1)
    table[1]=1

    for i in range(2,n+1):
        table[i]=table[i-1]+table[i-2]
    
    return table[n]
print(fib_tab(10))


