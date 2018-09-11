from math import *
import unittest 

def Simpson(f, a, b, n): #params: function, lower bound, upper bound, num of partitions 
    h = float(b - a)/n 
    sumE = 0
    sumO = 0
    for i in range(1, n/2): sumE += 2*f(a + 2*i*h) #even valued n partitions
    for i in range(1, n/2 + 1): sumO += 4*f(a + (2*i - 1)*h) #odd valued n partitions 
    return h/3.0 * (f(a) + f(b) + sumE + sumO)

def Trapezoid(f, a, b, n):
    h = float(b-a)/n
    sum = 0
    for i in range(1,n): sum += f(a + i*h)
    return h * ((f(a) + f(b)) / 2 + sum) 
     

###tests###

class Test(unittest.TestCase):
    def testSimpsonsMethod(self):
        f = lambda x: 12*x**60
        self.assertAlmostEqual(Simpson(f, 0 , 1 ,100), 12./61., 3) 
        self.assertAlmostEqual(Simpson(f, 0 , 1 ,1000), 12./61.)

        var = lambda x: sin(x)**2
        self.assertAlmostEqual(Simpson(var, 0 , 2 * pi ,100), pi)
        self.assertAlmostEqual(Simpson(var, 0 , pi ,100), pi/2)

        y = lambda x: log(4*x)
        self.assertAlmostEqual(Simpson(y, 1 , 2 ,100), 2*log(8)-log(4)-1)

        g = lambda x: e ** x ** 2 
        self.assertAlmostEqual(Simpson(g, 0 , 2 ,100), 16.45262776550723, 3)

    def testTrapezoidMethod(self):
        f = lambda x: 12*x**60
        self.assertAlmostEqual(Trapezoid(f, 0 ,1, 1000), 12./61., 3)   

        var = lambda x: sin(x)**2
        self.assertAlmostEqual(Trapezoid(var, 0 , 2 * pi ,100), pi)
        self.assertAlmostEqual(Trapezoid(var, 0 , pi ,100), pi/2)

        y = lambda x: log(4*x)
        self.assertAlmostEqual(Trapezoid(y, 1 , 2 ,1000), 2*log(8)-log(4)-1)

        g = lambda x: e ** x ** 2 
        self.assertAlmostEqual(Trapezoid(g, 0 , 2 ,1000), 16.45262776550723, 3)

if __name__ == "__main__":
    unittest.main()
