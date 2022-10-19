import math
pi=3.14
def circle(radius):
    return 2*pi*radius,pi*radius**2

l,s=circle(12)

print(l,s)



def solution(a,b,c):
    if a :
        return (-b+math.sqrt(b**2-4*a*c))/2/a,(-b-math.sqrt(b**2-4*a*c))/2/a
    elif b:
        return -c/b
    elif c==0: return None

while True:
    x=input('Input parameters (a,b,c):')
    a,b,c=list(map(float,x.split(',')))
    res=solution(a,b,c)
    if res is None:  break
    elif len(res)==1: print(res)
    elif len(res)==2:print(res[0],res[1])
    


def capital_index(s='Hello World'):
    return [i for i,c in enumerate(s) if c.isupper()]
print(capital_index())
print(capital_index('I Have A Dream'))


def longword(l):
    ll=[s for s in l if s.count('i') if s[s.index('i'):].count('n')]
    return sorted(ll,key=lambda x:len(x))[-1] 
s='Find the longest word in a given text that contains letter'
print(longword(s.split(' ')))

def median_filter(a,b,c):
    return sorted([a,b,c])[1]
l=[1,2,3,3,9,2,2,1,2,5,12,3,1,4]
a,b=0,0
for i,c in enumerate(l):
    #print(median_filter(a,b,c))
    a,b=b,c

############recursive!!!#############
def factorial(n):
    if isinstance(n,int):
        if n==0: return 1
        return factorial(n-1)*n
    else : return 0
print(factorial(4))

def fibonacci(n):
    if n==0: return 0
    elif n==1:return 1
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))
