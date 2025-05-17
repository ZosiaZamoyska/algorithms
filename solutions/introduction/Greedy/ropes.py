'''
Exercise: Strings (Ropes)

A boy received `n` strings from his grandfather, laid out in a straight line, one after another.
He noticed that he can freely tie any two adjacent strings together to form one longer string.
The resulting string has a length equal to the sum of the two original strings, and it can again be tied with the next adjacent string.

The boy wants to end up with as many strings as possible, with the constraint that each resulting string must be at least as long as his height `h`.

Input:
- First line: Two integers `n` and `h` — the number of strings and the boy's height.
- Second line: `n` integers representing the lengths of the strings in order.

Output:
- One integer — the maximum number of strings (after tying some adjacent ones if needed) such that each of them is at least `h` long.

Example:
Input:
8 4
1 2 3 4 8 1 1 3

Output:
4
'''

def max_valid_strings(n, h, lengths):
    suma = 0
    wynik = 0
    for i in range(n):
        suma += lengths[i]
        if suma >= h:
            wynik += 1
            suma = 0
    return wynik


# Example usage:
n, h = 8, 4
lengths = [1, 2, 3, 4, 8, 1, 1, 3]
print(max_strings_at_least_h(n, h, lengths))  # Output: 4
