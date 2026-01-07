class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxProduct(self, root):
        MOD = 10**9 + 7
        self.max_product = 0

        # Step 1: Calculate total sum of tree
        def totalSum(node):
            if not node:
                return 0
            return node.val + totalSum(node.left) + totalSum(node.right)

        total = totalSum(root)

        # Step 2: DFS to calculate subtree sums and max product
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            subtree_sum = node.val + left + right

            # Product if we cut above this node
            product = subtree_sum * (total - subtree_sum)
            self.max_product = max(self.max_product, product)

            return subtree_sum

        dfs(root)
        return self.max_product % MOD

from collections import deque

def buildTree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root

# Input
arr = [1, 2, 3, 4, 5, 6]

# Build tree
root = buildTree(arr)

# Run solution
sol = Solution()
result = sol.maxProduct(root)

print(result)
