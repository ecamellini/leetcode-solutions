from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode', right: 'TreeNode'):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        depth = 1  # If we have even a single node, depth is one

        currentLevelNodes = [root]

        nextLevelNodes = []  # children of the nodes at the current level/depth

        while len(currentLevelNodes) > 0:

            # we find all the children of the nodes we have at this level
            for node in currentLevelNodes:
                if node.right is not None:
                    nextLevelNodes.append(node.right)

                if node.left is not None:
                    nextLevelNodes.append(node.left)

            if len(nextLevelNodes) > 0:  # If we have some nodes one level further
                depth += 1  # then we can go deeper, we descend one level
                # we descended, current level becomes the previous next level
                currentLevelNodes = nextLevelNodes
                nextLevelNodes = []  # we reset nextLevelNodes, we still don't know if we have any
            else:
                return depth


treeFromLeetCodeExample = TreeNode(
    3,
    TreeNode(
        9,
        None,
        None
    ),
    TreeNode(
        20,
        TreeNode(15, None, None),
        TreeNode(7, None, None)
    )
)

s = Solution()

assert s.maxDepth(None) == 0
assert s.maxDepth(treeFromLeetCodeExample) == 3
assert s.maxDepth(TreeNode(11, None, None)) == 1
assert s.maxDepth(TreeNode(11, None, TreeNode(11, None, TreeNode(11, None, TreeNode(
    11, None, TreeNode(11, None, TreeNode(11, None, TreeNode(11, None, None)))))))) == 7

print("All tests have passed!")
