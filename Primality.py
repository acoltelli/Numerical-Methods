import unittest 

#test for primality, generate primes up to n 
def isPrime(n):
    if n is not 2 and n % 2 == 0 or n < 2: return False # 0 and 1 are not prime
    # test for primality using square root of n, increment using only odd numbers
    for i in range(3, int(n ** 0.5) + 1, 2):   
        if n % i == 0:
            return False    
    return True   

#returns generator object listing primes up to n 
def primesUpTo(n):
    var = [i for i in range(n)]
    for i in var:
        if isPrime(i) is True:
            yield i 




###tests###

class Test(unittest.TestCase):   
    def testIsPrime(self):
      self.assertEqual(isPrime(0), False)
      self.assertEqual(isPrime(1), False)
      self.assertEqual(isPrime(2), True)
      self.assertEqual(isPrime(3), True)

      self.assertEqual(isPrime(144), False)
      self.assertEqual(isPrime(1000000000000000000000), False)
      self.assertEqual(isPrime(17), True)

    def testPrimesUpTo(self):
        var = [i for i in primesUpTo(10)] 
        self.assertEqual(var, [2, 3, 5, 7])
        self.assertEqual(var, [2,   3,  5,  7,  11, 13, 17, 19, 23,
29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
71, 73, 79, 83, 89, 97, 101,    103,    107,    109,
113,    127,    131,    137,    139,    149,    151,    157,    163,    167,
173,    179,    181,    191,    193,    197,    199,    211,    223,    227,
229,    233,    239,    241,    251,    257,    263,    269,    271,277,
281,    283,    293 ,307    ,311    ,313    ,317    ,331    ,337    ,347,
349 ,353    ,359    ,367    ,373    ,379    ,383    ,389    ,397    ,401,
409,    419,    421,    431,    433,    439,    443,    449,    457,    461,
463,    467,    479,    487,    491,    499,    503,    509,    521,    523,
541,    547,    557,    563,    569,    571,    577,    587,    593,    599,
601,    607,    613,    617,    619,    631,    641,    643,    647,    653,
659,    661,    673,    677,    683,    691,    701,    709,    719,    727,
733,    739,    743,    751,    757,    761,    769,    773,    787,    797,
809,    811,    821,    823,    827,    829,    839,    853,    857,    859,
863,    877,    881,    883,    887,    907,    911,    919,    929,    937,
941,    947,    953,    967,    971,    977,    983,    991,    997]) 
        

if __name__ == "__main__":
    unittest.main()