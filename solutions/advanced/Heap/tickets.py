'''
    A man is going on a trip consisting of n consecutive segments. 
    Before entering each segment, there is a ticket booth where he must buy 
    and validate a ticket in order to continue the journey.

    Additionally, at each booth, he can purchase a limited number of extra tickets 
    for future use. Ticket prices may vary at each booth, and each person 
    can buy only a limited number of tickets from each booth.

    Your task is to calculate the **minimum total cost** of the entire journey.

    Input:
    - An integer n — the number of segments (n >= 1)
    - Followed by n lines, each containing two integers:
        price — the price of a single ticket at that booth,
        count — the maximum number of tickets that can be bought at that booth

    Output:
    - One integer: the minimum total cost of the journey (i.e., buying n tickets, one per segment)

    Example:
    Input:
    4
    3 2
    1 2
    2 1
    5 3

    Output:
    7

    Explanation:
    The best strategy is to buy cheap tickets in advance when possible:
    - From booth 1, buy 2 tickets at 3
    - From booth 2, buy 2 tickets at 1
    - From booth 3, buy 1 ticket at 2
    - From booth 4, buy 3 tickets at 5
    During the journey, always use the cheapest available ticket:
    3 + 1 + 1 + 2 = 7
'''
import heapq

def minimalny_koszt_podrozy(n, bilety):
    heap = []
    koszt = 0

    for i in range(n):
        cena, liczba = bilety[i]
        heapq.heappush(heap, (cena, liczba))

        najtanszy_cena, ilosc = heapq.heappop(heap)
        if ilosc > 0:
            koszt += najtanszy_cena
            if ilosc > 1:
                heapq.heappush(heap, (najtanszy_cena, ilosc - 1))

    return koszt

n = 4
bilety = [
    (3, 2),
    (1, 2),
    (2, 1),
    (5, 3)
]

print(minimalny_koszt_podrozy(n, bilety))  # Output: 7
