def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

# input
n = int(input())

# output
hanoi(n, "A", "C", "B")
