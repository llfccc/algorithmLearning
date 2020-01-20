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
            print("当前正在遍历",self.print_node(queue),"这一层")
            cl = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                print(self.print_node(node),"正在出队")
                cl.append(node.val)
                self.print_node(node)
                if node.left:
                    queue.append(node.left)
                    print(self.print_node(node.left),"正在入队")
                    print("当前队列的值为",self.print_node(queue))
                if node.right:
                    queue.append(node.right)
                    print(self.print_node(node.right),"正在入队")
                    print("当前队列的值为",self.print_node(queue))
            res.append(cl)
        return res

    def print_node(self,node_list):
        node_val=[]
        if isinstance(node_list,list):
            for node in node_list:
                node_val.append(node.val)
            return node_val
        elif isinstance(node_list,TreeNode):
            return node_list.val

s = method1.method2.Solution()
result = s.levelOrder(root)
print("******************")
print("最终结果是",result)