from collections import deque

# -------------------------------
# TreeNode definition
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------
# Build binary tree from list
# (level-order representation)
# -------------------------------
def buildTree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root
class Solution():
    def subtreeWithAllDeepest(self, root):
        def dfs(node):
            if not node:
                return (0 , None)
            left_depth, left_node = dfs(node.left)
            right_depth, right_node = dfs(node.right)
            if left_depth > right_depth:
                return left_depth + 1, left_node
            elif right_depth > left_depth:
                return right_depth + 1, right_node
            else:
                return left_depth + 1, node

        return dfs(root)[1]
        

# -------------------------------
# MAIN (run examples)
# -------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    arr1 = [3,5,1,6,2,0,8,None,None,7,4]
    root1 = buildTree(arr1)
    result1 = sol.subtreeWithAllDeepest(root1)
    print("Example 1 Output:", result1.val)  # Expected: 2

    # Example 2
    arr2 = [1]
    root2 = buildTree(arr2)
    result2 = sol.subtreeWithAllDeepest(root2)
    print("Example 2 Output:", result2.val)  # Expected: 1

    # Example 3
    arr3 = [0,1,3,None,2]
    root3 = buildTree(arr3)
    result3 = sol.subtreeWithAllDeepest(root3)
    print("Example 3 Output:", result3.val)  # Expected: 2