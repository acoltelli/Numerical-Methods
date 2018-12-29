import unittest 

def gcd(a,b):   #find greatest common divisor of a,b
	if b == 0:
		return a
	else:
		return gcd(b, a % b) #gcd(a,b) = gcd(b, a % b)



class Test(unittest.TestCase):   
	def testGCD(self):
		self.assertEqual(gcd(12, 144), 12)
		self.assertEqual(gcd(500000, 500000), 500000)
		self.assertEqual(gcd(0, 0), 0)
		self.assertEqual(gcd(1, 1), 1)


if __name__ == "__main__":
    unittest.main()