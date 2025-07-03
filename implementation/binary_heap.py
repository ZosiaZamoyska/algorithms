N = 1000 * 1000 + 6
tree = [0] * N

def insert(v):
    global size_n
    size_n += 1
    tree[size_n] = v
    k = size_n
    while k>1 and tree[k] > tree[k//2]:
        tree[k], tree[k//2] = tree[k//2], tree[k]
        k = k // 2

def max_heap():
    return tree[1]

def restore(node):
    global size_n
    
    left = 2*node;
    right = 2*node + 1;
    maxi = node;
    
    if left <= size_n and tree[left] > tree[maxi]:
        maxi = left
    if right <= size_n and tree[right] > tree[maxi]:
        maxi = right
    if maxi > node:
        tree[node], tree[maxi] = tree[maxi], tree[node]
        restore(maxi)
        
def delete_max():
    global size_n
    tree[1] = tree[size_n]
    size_n -= 1
    restore(1)
    
def operations():
    m = int(input())
    for _ in range(m):
        a = int(input())
        if a == 0:
            print(max_heap())
        if a == 1:
            delete_max()
        if a == 2:
            b = int(input())
            insert(b)
            print_heap()

def print_heap():
    global size_n
    for i in range(1, size_n+1): 
        print(tree[i], end=' ')
    print()

n = int(input())
for i in range(n):
    tree[i+1] = int(input())
size_n = n
for i in range(n//2, 0, -1):
    restore(i)
    
print_heap()
operations()
print_heap()