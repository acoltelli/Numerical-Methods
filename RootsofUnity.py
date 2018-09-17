import math 
import cmath
import unittest

#compute roots of unity of some positive int n 
def rootsOfUnity(n):
	if n <= 0: exit("n must be a positive integer")
	list = []
	var = math.pi * 2 / n 
	for i in range(n):
		real = round(math.cos(i * var), 10) # round for aesthetics 
		imaginary = round(math.sin(i * var), 10) 
		list.append(complex(real,imaginary))
	return list 

# An nth root of unity is primitive if it is not a kth root of unity for some smaller k:
# If n is a prime number, all nth roots of unity, except 1, are primitive.	


###test###

class Test(unittest.TestCase): 
	def testRootsOfUnity(self):
		with self.assertRaises(SystemExit): rootsOfUnity(-1)
		self.assertEqual(rootsOfUnity(1),[(1+0j)])
		self.assertEqual(rootsOfUnity(2),[(1+0j), (-1+0j)])
		self.assertEqual(rootsOfUnity(3), [(1+0j), (-0.5+0.8660254038j), (-0.5-0.8660254038j)])
		self.assertEqual(rootsOfUnity(27),[(1+0j), (0.9730448706+0.2306158707j), 
												(0.8936326403+0.4487991802j), (0.7660444431+0.6427876097j), 
												(0.5971585917+0.8021231928j), (0.396079766+0.9182161069j), 
												(0.1736481777+0.984807753j), (-0.0581448289+0.9983081583j), 
												(-0.2868032327+0.9579895123j), (-0.5+0.8660254038j), 
												(-0.6862416379+0.7273736416j), (-0.8354878114+0.5495089781j), 
												(-0.9396926208+0.3420201433j), (-0.9932383577+0.1160929141j), 
												(-0.9932383577-0.1160929141j), (-0.9396926208-0.3420201433j), 
												(-0.8354878114-0.5495089781j), (-0.6862416379-0.7273736416j), 
												(-0.5-0.8660254038j), (-0.2868032327-0.9579895123j), 
												(-0.0581448289-0.9983081583j), (0.1736481777-0.984807753j), 
												(0.396079766-0.9182161069j), (0.5971585917-0.8021231928j), 
												(0.7660444431-0.6427876097j), (0.8936326403-0.4487991802j), (
												0.9730448706-0.2306158707j)])

	#root of unity is defined as a complex number which gives 1 when raised to some positive integer power n 
	def testProofOfDef(self):
		#roots for one and two are trivial 
		#testing roots for n = 3 
		self.assertAlmostEqual(complex(1,0) ** 3, 1)
		self.assertAlmostEqual(complex(-0.5, 0.8660254038) ** 3, 1)
		self.assertAlmostEqual(complex(-0.5, 0.8660254038) ** 3, 1)
		#test random roots for n = 27 result 
		self.assertAlmostEqual(complex(0.9730448706, 0.2306158707) ** 27, 1)
		self.assertAlmostEqual(complex(-0.0581448289,-0.9983081583) ** 27, 1)
		self.assertAlmostEqual(complex(0.396079766,0.9182161069) ** 27, 1)


if __name__ == "__main__":
    unittest.main()