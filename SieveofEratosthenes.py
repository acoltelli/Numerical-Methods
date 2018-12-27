def sieve(n):   #returns generator object containing primes up to n 
    L = [True] * n   #initialize all values to True                        
    L[0] = L[1] = False   #0,1 are not prime

    for index, value in enumerate(L):
        if value is True:
            yield index   #return index of enumerated list only when index value is True
            #sets multiples of the prime to False begininng with its square  
            for j in range(index ** 2, n, index):    
                L[j] = False
