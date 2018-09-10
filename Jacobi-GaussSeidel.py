from numpy import * 
from numpy.linalg import *
import unittest

#TODO: add terminating statment if convergence does not occur 
#TODO: add contraint that A does not have zeros in the diagonal 
def jacobi(A, b, n):  
    D = diag(A) 
    var = A - diag(D)
    x= zeros(len(b)) # initial guess is a zero vector
    for i in range(n):	
        x = (b - dot(var, x)) / D 
    residual = norm(b - dot(A, x))
    if residual > 1: #choose residual value of 1 to test for nonconvergence. This condition is sufficient for large enough values of n. 
		exit("No Convergence")   
    return x 

def gaussSeidel(A, b, n):
    lower = tril(A) #lower, triangular matrix, including diagonal
    upper = triu(A,1) #upper triangular matrix sitting on top of, and not including, diagonal 
    x = zeros(len(b))

    for i in range(n):
        x = dot(inv(lower), b - dot(upper, x)) 
    residual = norm(b - dot(A, x))
    if residual > 1: 
		exit("No Convergence")
    return x




####tests #####

class Test(unittest.TestCase):  
	def testJacobi(self):
		A = array([[12.0,2.0],[3.0,4.0]])
		b = array([7.0,39.0])
		self.assertEqual(str(jacobi(A,b, 20)),'[-1.19047619 10.64285713]') 
	
	def testJacobi_(self):
		A = array([[1.0,1.0],[1.0,3.0]])
		b = array([6.0,12.0])
		self.assertEqual(str(jacobi(A,b, 40)), '[3. 3.]')

	def testGaussSeidel(self):
		A = array([[2.0,1.0,4.0],[5.0,2.0,4.0],[9.0,10.0,11.0]])
		b = array([30.0,70.0,110.0])

		self.assertEqual(str(gaussSeidel(A,b,100)), '[14.38361661 -3.15080888  1.09595812]')

	def testNonConvergence(self):
		A = array([[2.0,1.0,4.0],[5.0,2.0,4.0],[9.0,10.0,11.0]])
		b = array([30.0,70.0,110.0])
		with self.assertRaises(SystemExit): jacobi(A,b,50)
if __name__ == "__main__":
    unittest.main()

