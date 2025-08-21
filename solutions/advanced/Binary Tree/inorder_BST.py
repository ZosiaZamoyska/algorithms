'''
    Print the values of BST, sorted. 
'''
def inorder_traversal(tree):
    n = len(tree)
    result = []

    def dfs(i):
        if i >= n or tree[i] is None:
            return
        dfs(2 * i)          # left child
        result.append(tree[i])
        dfs(2 * i + 1)      # right child

    dfs(1)  # root at index 1
    return result


# Example BST:
#        10
#       /  \
#      5    15
#     / \   / \
#    2   7 12  20
tree = [None, 10, 5, 15, 2, 7, 12, 20]

print(inorder_traversal(tree))  
# Output: [2, 5, 7, 10, 12, 15, 20]  (sorted)
