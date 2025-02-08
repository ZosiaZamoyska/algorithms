"""
A boy is last in the queue at the candy store. Since he is in a hurry, he decides to swap places 
with some people in front of him, even if he has to pay for it.

- Each person is willing to swap, but moving a person `i` one place back in the queue costs `c[i]`.
- If the boy is `k` places away from person `i` (where `k > 0`), swapping with them costs `k * c[i]`.
- Bajtoś wants to be first in the queue while minimizing the total cost.

Input:
- N (1 ≤ N ≤ 1,000,000) — number of people in front of the boy.
- C[0], C[1], ..., C[N-1] (1 ≤ C[i] ≤ 10^9) — cost per position for each person.

Output:
- Print the minimum cost required for the boy to become first in the queue.

Example:
Input:
4
5 2 4 3

Output:
10
"""

def min_cost_to_front(costs):
    min_cost = float('inf')
    total_cost = 0

    for i in range(n-1, -1, -1):        
        min_cost = min(min_cost, costs[i])
        total_cost += min_cost

    return total_cost

n = int(input())
costs = list(map(int, input().split()))

print(min_cost_to_front(costs))
