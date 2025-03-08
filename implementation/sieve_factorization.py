def sieve_factorization(n):
    F = [0] * (n + 1)
    
    for i in range(2, int(n**0.5) + 1):
        if F[i] == 0:
            for k in range(i * i, n + 1, i):
                if F[k] == 0:
                    F[k] = i
    
    for i in range(2, n + 1):
        if F[i] == 0:
            F[i] = i
    
    return F

n = int(input())
factors = sieve_factorization(n)
print(factors)
