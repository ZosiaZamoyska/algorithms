def calculate_prefix(n, m, matrix):
    pref = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            pref[i][j] = (
                pref[i - 1][j]
                + pref[i][j - 1]
                - pref[i - 1][j - 1]
                + matrix[i - 1][j - 1]
            )
    return pref

def query(pref, x1, y1, x2, y2):
    return (
        pref[x2][y2]
        - pref[x1 - 1][y2]
        - pref[x2][y1 - 1]
        + pref[x1 - 1][y1 - 1]
    )

#input 
n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

pref = calculate_prefix(n, m, matrix)

#queries
q = int(input())
for _ in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    print(query(pref, x1, y1, x2, y2))