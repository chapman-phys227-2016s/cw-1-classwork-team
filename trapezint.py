#Assignment cw-1 by Andrew Malfavon
#Problem 3.6 pg130
#2/10/2016
import math

def trapezint1(f, a, b):
    return ((b-a)/2.0)*(f(a) + f(b))

print trapezint1(math.sin, 0, math.pi)
print trapezint1(math.cos, 0, math.pi)
print trapezint1(math.sin, 0, math.pi/2)

def trapezint2(f, a, b):
    return (float((b-a))/4.0)*(f(a) + f(b) + 2*f((a+b)/2.0))

print trapezint2(math.sin, 0, math.pi)
print trapezint2(math.cos, 0, math.pi)
print trapezint2(math.sin, 0, math.pi/2)

def trapezint3(f, a, b, n):
    sum = 0
    h = (b-a)/float(n)
    for i in range(1, n-2):
        sum += (h/2.0)*(f(a + i*h) + f(a + (i+1)*h));
    return sum

print trapezint3(math.sin, 0, math.pi, 1000);
print trapezint3(math.cos, 0, math.pi, 1000);
print trapezint3(math.sin, 0, math.pi/2, 1000);

#Unit Tests
def func(x):
    return x**2;

def test_trapezint():
    assert trapezint1(func, 2, 3) == 13.0/2.0
    assert trapezint2(func, 2, 3) == 51.0/8.0
    #used round function solely for testing.
    assert round(trapezint3(func, 2, 5, 100000)) == 39.0
