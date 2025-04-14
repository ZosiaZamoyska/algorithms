'''
    Given an array a, and a value array w, for each index i find a radius r_i, such that the sum of all values within that radius from the index point does not exceed w[i].
'''

def minimal_radii(a, w):
    n = len(a)
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]

    def get_sum(l, r):
        l = max(0, l)
        r = min(n - 1, r)
        return prefix[r + 1] - prefix[l]

    result = []

    for i in range(n):
        left = 0
        right = n
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            total = get_sum(i - mid, i + mid)

            if total >= w[i]:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        result.append(answer)

    return result


a = [2, 3, 1, 4, 2, 1]
w = [6, 3, 8, 8, 10, 14]
print(minimal_radii(a, w))  # Output: [2, 0, 1, 2, 3, -1]
