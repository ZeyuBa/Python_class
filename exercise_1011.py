import math

factor=[pow(-1,i)*1/math.factorial(2*(i+1)-1) for i in range(10)]

def sinx(theta):
    theta=theta/180*math.pi
    sin_value=0
    for i,f in enumerate(factor):
        sin_value+=math.pow(theta,2*(i+1)-1)*f
    return sin_value

print(sinx(30),sinx(60),sinx(90))


