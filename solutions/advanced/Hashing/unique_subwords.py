'''
    For a given word, count all unique subwords inside that word.

    Example:
    ABAB

    Answer:
    7 
    (A, B, AB, BA, ABA, BAB, ABAB)
'''

MOD1 = 10**9 + 7
MOD2 = 10**9 + 9
G1 = 59
G2 = 313

def policz_podslowa(word):
    n = len(word)
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)
    
    for i in range(1, n + 1):
        power1[i] = (power1[i - 1] * G1) % MOD1
        power2[i] = (power2[i - 1] * G2) % MOD2

    hash1 = [0] * (n + 1)
    hash2 = [0] * (n + 1)

    for i in range(n):
        hash1[i + 1] = (hash1[i] + ord(word[i]) * power1[i]) % MOD1
        hash2[i + 1] = (hash2[i] + ord(word[i]) * power2[i]) % MOD2

    unique_hash = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            dl = j - i
            h1 = (hash1[j] - hash1[i] + MOD1) % MOD1
            h1 = (h1 * power1[n - i - dl]) % MOD1

            h2 = (hash2[j] - hash2[i] + MOD2) % MOD2
            h2 = (h2 * power2[n - i - dl]) % MOD2

            unique_hash.add((h1, h2))

    return len(unique_hash)

word = "ABAB"
print(policz_podslowa(word))

