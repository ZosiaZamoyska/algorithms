'''
    What is a minimum perimeter of a rectangle with a area of exactly p?

    Example
    30
    Answer 
    22
'''

def min_perimeter(p):
    ans = 2 * (p + 1)
    a = 2
    while a * a <= p:
        if p % a == 0:
            b = p / a
        ans = min(ans, 2*(a+b))
        a += 1
    return int(ans)

p = int(input())
print(min_perimeter(p))