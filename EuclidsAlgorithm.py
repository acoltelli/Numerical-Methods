
def gcd(a,b):   #find greatest common divisor of a,b
	if b == 0:
		return a
	else:
		return gcd(b, a % b) #gcd(a,b) = gcd(b, a % b)







