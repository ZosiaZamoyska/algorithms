'''
    Count how many common nodes two BST have.
'''

def inorder_traversal(tree):
    n = len(tree)
    result = []
    def dfs(i):
        if i >= n or tree[i] is None:
            return
        dfs(2 * i)
        result.append(tree[i])
        dfs(2 * i + 1)
    dfs(1)
    return result

def count_common_nodes(tree1, tree2):
    arr1 = inorder_traversal(tree1)  # sorted
    arr2 = inorder_traversal(tree2)  # sorted
    
    # merge-like traversal to count intersection
    i = j = count = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            count += 1
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return count


# Example usage:
# Tree 1:        10
#               /  \
#              5    15
#             / \   / \
#            2   7 12  20
tree1 = [None, 10, 5, 15, 2, 7, 12, 20]

# Tree 2:       8
#              / \
#             5   12
#            /     \
#           2       20
tree2 = [None, 8, 5, 12, 2, None, None, 20]

print(count_common_nodes(tree1, tree2))  
# Common nodes = {2,5,12,20} → 4
