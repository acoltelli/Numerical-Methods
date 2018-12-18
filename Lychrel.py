import unittest

#is number a palindrome 
def isPalidrome(n):
	n = str(n) 
	if n[::-1] == n:
		return True
	else:
		return False  

#is number a Lychrel number, recursion terminates after 50 calls
def Lychrel(n, r=1):
	n= str(n)
	sum = int(n) + int(n[::-1])
	
	if isPalidrome(sum) == True:
		return False
	elif r < 50:
		return Lychrel(sum, r+1)
	else:
		return True


###tests###

class Test(unittest.TestCase):   
    def testLychrel(self):
    	self.assertEqual(Lychrel(349), False)
    	self.assertEqual(Lychrel(196), True)
    	#10,677 is a Lychrel number only within these parameters
    	#it creates the paldrome 4,668,731,596,684,224,866,951,378,664 after 53 iterations
    	self.assertEqual(Lychrel(10677), True) 


if __name__ == "__main__":
    unittest.main()

