def isprime(n):
    if n<3: return True
    for i in range(2,n):
        if n%i==0:
            return False 
    return True

def generator():
    n=2
    while True:
        if isprime(n):
            yield n
        n+=1

g=generator()

for i in range(100):
    print(next(g))

