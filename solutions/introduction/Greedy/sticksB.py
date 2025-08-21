def minimal_breaks(sticks):
    from collections import defaultdict

    costs_per_stick = []
    for a in sticks:
        cost = {}
        k = 0
        while True:
            L = a // (1 << k)
            R = (a + (1 << k) - 1) // (1 << k)
            if R < 1:
                break
            L = max(L, 1)
            print("aa")
            for t in range(L, R + 1):
                print(t)
                if t not in cost:
                    cost[t] = k
            if L == 1 and R == 1:
                break
            k += 1

        costs_per_stick.append(cost)

    common_ts = set(costs_per_stick[0].keys())
    for c in costs_per_stick[1:]:
        common_ts &= set(c.keys())

    best = min(sum(c[t] for c in costs_per_stick) for t in common_ts)
    return best

# Przykłady
print(minimal_breaks([5,6,5,6]))  # 4
print(minimal_breaks([2,21]))     # 2
