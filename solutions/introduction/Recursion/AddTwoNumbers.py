def add_recursive(l1, l2, carry=0, index=0):
    if index >= len(l1) and index >= len(l2) and carry == 0:
        return []

    a = l1[index] if index < len(l1) else 0
    b = l2[index] if index < len(l2) else 0

    total = a + b + carry
    new_digit = total % 10
    new_carry = total // 10

    result = add_recursive(l1, l2, new_carry, index + 1)
    result.insert(0, new_digit)
    return result

# Input
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# Compute result
result = add_recursive(l1, l2)

# Output
print(result)
