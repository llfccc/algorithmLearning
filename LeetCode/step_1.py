class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(3)
level_1 = TreeNode(9)
level_2 = TreeNode(20)
level_1_1 = TreeNode(99)
level_2_1 = TreeNode(15)
level_2_2 = TreeNode(7)

root.left = level_1
root.right = level_2
level_1.left = level_1_1
level_2.left = level_2_1
level_2.right = level_2_2


class method1.method2.Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, res = [], []
        queue.append(root)

        while queue:
            cl = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                cl.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cl)
        return res


s = method1.method2.Solution()
result = s.levelOrder(root)
print(result)