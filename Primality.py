import unittest 

#test for primality, generate primes up to n 
def isPrime(n):
    if n is not 2 and n % 2 == 0 or n < 2: return False # 0 and 1 are not prime
    # test for primality using square root of n, increment using only odd numbers
    for i in range(3, int(n ** 0.5) + 1, 2):   
        if n % i == 0:
            return False    
    return True


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


if __name__ == "__main__":
    unittest.main()