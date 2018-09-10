from numpy import * 
from numpy.linalg import *
import unittest

#convergence to a local minimum can be guaranteed. When the function 
#is convex, all local minima are also global minima, 
#so in this case gradient descent can converge to the global solution.

#TODO: add test for convergence 
#TODO: refactor method of entering gradient
#TODO: test multivariable cases 
def gradientDescent(grad,n):
	x1 = 1 # start x value
	gamma = 0.01 # step size multiplier
	
	for i in range(n):
		x0 = x1 
		x1 -= gamma * grad(x0)
		if (abs(x1 - x0) < 0.000001): #desired precision of result, compared with error term
			return x1
	return x1

#gradient must be entered as lambda, numpy does not support symbolic computations
gradient = lambda x: 8 + 18 * x
print gradientDescent(gradient,100)


