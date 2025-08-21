'''
    For a given BST, find how many nodes are there with value between given range of (a, b).
'''

def count_in_range(tree, a, b):
    n = len(tree)

    def helper(i):
        if i >= n or tree[i] is None:
            return 0
        
        val = tree[i]
        if val < a:
            return helper(2 * i + 1)  # only right subtree
        elif val > b:
            return helper(2 * i)      # only left subtree
        else:
            # count this node + explore both sides
            return 1 + helper(2 * i) + helper(2 * i + 1)

    return helper(1)


# Example usage:
# Tree:       10
#           /    \
#          5      15
#         / \    /  \
#        2   7  12  20

tree = [None, 10, 5, 15, 2, 7, 12, 20]

print(count_in_range(tree, 5, 15))   # 4  (nodes: 5,7,10,15)
print(count_in_range(tree, 6, 13))   # 2  (nodes: 7,12)
print(count_in_range(tree, 1, 100))  # 7  (all nodes)
