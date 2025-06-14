'''
    There are n people in a queue. Given each person's age, find the largest sum of two people's ages, such that those people are standing at most k positions away from each other.
'''

class MaxHeap:
    def __init__(self):
        self.t = [None]
        self.n = 0

    def insert(self, e):
        self.n += 1
        self.t.append(e)
        w = self.n
        while w > 1 and self.t[w][0] > self.t[w // 2][0]:
            self.t[w], self.t[w // 2] = self.t[w // 2], self.t[w]
            w //= 2

    def top(self):
        return self.t[1] if self.n > 0 else None

    def pop(self):
        if self.n == 0:
            return None
        top_elem = self.t[1]
        self.t[1] = self.t[self.n]
        self.n -= 1
        self.t.pop()
        self._restore(1)
        return top_elem

    def _restore(self, i):
        lewy = 2 * i
        prawy = 2 * i + 1
        maks = i

        if lewy <= self.n and self.t[lewy][0] > self.t[maks][0]:
            maks = lewy
        if prawy <= self.n and self.t[prawy][0] > self.t[maks][0]:
            maks = prawy
        if maks != i:
            self.t[i], self.t[maks] = self.t[maks], self.t[i]
            self._restore(maks)

    def empty(self):
        return self.n == 0


def maks_suma_wiekow_with_heap(wiek, k):
    heap = MaxHeap()
    deleted = set()
    max_sum = 0

    for i in range(len(wiek)):
        heap.insert((wiek[i], i))

        while not heap.empty() and heap.top()[1] < i - k:
            outdated = heap.pop()

        if i >= 1:
            valid = []
            while not heap.empty() and len(valid) < 2:
                val = heap.top()
                if val[1] < i - k:
                    heap.pop()
                else:
                    valid.append(val)
                    heap.pop()

            if len(valid) == 2:
                max_sum = max(max_sum, valid[0][0] + valid[1][0])

            for v in valid:
                heap.insert(v)

    return max_sum


# Example
n, k = 5, 2
wiek = [4, 3, 2, 6, 1]
print(maks_suma_wiekow_with_heap(wiek, k))  # Output: 9
