'''
    Check if a given binary tree is a BST (binary search tree).
'''

def is_bst_list(tree):
    n = len(tree)

    def helper(i, low, high):
        if i >= n or tree[i] is None:
            return True
        
        val = tree[i]
        if not (low < val < high):
            return False
        
        left = helper(2 * i, low, val)
        right = helper(2 * i + 1, val, high)
        return left and right

    return helper(1, float("-inf"), float("inf"))

# Example usage:

# Index:  0   1    2    3    4    5    6
tree1 = [None, 10,   5,   15,  2,   7,  12, 20]  # valid BST
print(is_bst_list(tree1))  # True

tree2 = [None, 10,   5,   15,  2,   12, None, None]  # not BST
print(is_bst_list(tree2))  # False
