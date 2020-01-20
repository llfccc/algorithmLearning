
class Node():
    def __init__(self, item, lchild = None, rchild = None):
        self.item = item
        self.lchild = lchild 
        self.rchild = rchild


class Tree():
    # 先定义一个带默认值None的根节点
    def __init__(self, root = None):
        self.root = root
    # 定义添加元素的方法
    def add(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
        else:
            # 注意这里是用队列的方式来循环判断当前节点有没有可加入位置的
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
    # 定义广度优先遍历(层次遍历)方法
    def breadth_travel(self):
        if self.root == None:
            return
        else:
            # 仍然是用队列的方式实现遍历，末端按遍历顺序逐个添加节点，首端逐个弹出先读到的节点
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                print(cur.item, end = " ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)
    # 定义深度优先遍历中的先序遍历
    def preorder(self, node):
        if node == None:
            return 
        else:
            print(node.item, end = " ")
            self.preorder(node.lchild)
            self.preorder(node.rchild)
    # 定义深度优先遍历中的中序遍历
    def inorder(self, node):
        if node == None:
            return
        else:
            self.inorder(node.lchild)
            print(node.item, end = " ")
            self.inorder(node.rchild)
    # 定义深度优先遍历中的后序遍历
    def postorder(self, node):
        if node == None:
            return
        else:
            self.postorder(node.lchild)
            self.postorder(node.rchild)

if __name__ == "__main__":
    t = Tree()
    t.add(0)
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    t.add(6)
    t.add(7)
    t.add(8)
    t.add(9)
    t.breadth_travel()
    print("")
    t.preorder(t.root)
    print("")
    t.inorder(t.root)
    print("")
    t.postorder(t.root)
    print("")
