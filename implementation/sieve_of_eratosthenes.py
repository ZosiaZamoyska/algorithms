def sieve_of_eratosthenes(n):
    sito = [False] * (n + 1)
    primes = []
    
    for i in range(2, int(n**0.5) + 1):
        if not sito[i]:
            for k in range(i * i, n + 1, i):
                sito[k] = True
    
    for i in range(2, n + 1):
        if not sito[i]:
            primes.append(i)
    
    return primes

n = int(input())
print(sieve_of_eratosthenes(n))
