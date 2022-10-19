from math import *
#################1##################

x0=1
x=x0
deltax=x0
while deltax>1e-6:
    x_prime=sqrt(9*x-7)
    deltax=abs(x_prime-x)
    x=x_prime
print(x)

#################2##################

x=[i for i in range(1,100)]
l=[(a,b,c) for a in x for b in x for c in x if a**2+b**2==c**2]

##################3##################

x=[i for i in range(10)]
l=[a*100+b*10+c for a in x for b in x for c in x if pow(a,3)+pow(b,3)+pow(c,3)==a*100+b*10+c and a]

####################4################

#!!! use of filter
l=[12,3,4,56,7]
def func(x):
    return x%2
res=filter(func,l)
list(res)

week=['Sat','Son','Mon','Tue','Wed','Thu','Fri']
months=[31,28,31,30,31,30,31,31,30,31,30,31]
wml=[week[m%len(week):]+week*(m//len(week))+week[:m%len(week)]for m in months]
Input=input("Input month,day")
m,d=Input.split(',')
m=int(m)
d=int(d)

print('the date is '+ wml[m-1][d-1])
