'''
Bitek is tired of his name. He's always one of the first to be called in the attendance list,
and as any reasonable student knows, nobody wants to be the first to answer.

But... starting today, everything will change. When someone calls him "Bitek", he will hand out
a card with his new name. The problem is, his only pencil broke, so the only thing he can do
is collect all the sheets of paper where he previously wrote nonsense and use an eraser to remove
some letters.

Of course, all the cards should have the same name on them, and he has to use all the available sheets,
because it would be a disaster if the boy formerly known as Bitek ran out of cards.
The new name doesn't have to make logical sense. It just needs to be as close to the end of the
alphabet as possible (i.e., lexicographically greatest).

Input
The first line contains a single number n (1 ≤ n ≤ 1000), the number of sheets.
Each of the following n lines contains a word written on a sheet, consisting of lowercase English letters.
The total length of all words will not exceed 100,000 characters.

Output
Output a single word – the lexicographically greatest name that can be formed by erasing letters
(possibly none) from each of the sheets, such that the same name appears on every one.
If such a name is lexicographically smaller than "bitek", print "bitek" instead.

Examples:
Input:
3
zygzaki
zabawawkapitana
zgryzkamienny

Output:
zki

Input:
2
blablabla
nicwaznego

Output:
bitek

Input:
1
zapomnianywojownik

Output:
zywwnk

https://szkopul.edu.pl/problemset/problem/CNrWfGt3eL5nu1HJ_Og05_v4/site/?key=statement
'''

def find_best_name(n, tab): 
    d = []
    for i in range(n):
        w = tab[i]
        d.append(len(w))

    pocz = [-1] * n
    kon = [0] * n
    wynik = []

    for a in range(25, -1, -1):  # From 'z' to 'a'
        while True:
            cj = True
            for b in range(n):
                if pocz[b] + 1 == d[b]:
                    cj = False
                    break
                for c in range(pocz[b] + 1, d[b]):
                    if ord(tab[b][c]) == a + 97:
                        kon[b] = c
                        break
                    elif c == d[b] - 1:
                        cj = False
                        break
                if not cj:
                    break
            if not cj:
                break
            wynik.append(chr(a + 97))
            for b in range(n):
                pocz[b] = kon[b]

    wynik_str = ''.join(wynik)

    if wynik_str < "bitek":
        return "bitek"
    else:
        return wynik_str


n = int(input())
words = []

for _ in range(n):
    w = input()
    words.append(list(w))

print(find_best_name(n, words))
