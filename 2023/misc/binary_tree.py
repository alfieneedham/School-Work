# The first node inserted is the root node.
class Binary_Tree():
    def __init__(self):
        self.tree = []
        self.root = None

    def create_node(self, item):
        self.tree.append(Node(item))

    def __find_node(self, item):
        for node in self.tree:
            if node.item == item:
                return(node)
        return(None)

    def add_children(self, parentNode, childNode, direction):
        parent = self.__find_node(parentNode)
        child = self.__find_node(childNode)
        if direction.lower() == "l":
            parent.insert_left_child(child)
        if direction.lower() == "r":
            parent.insert_right_child(child)

    def pre_order_traversal(self, root="default"):
        if root == "default": 
            root = self.tree[0]
        if root == None:
            return()
        print(root.item)
        self.pre_order_traversal(root.leftChild)
        self.pre_order_traversal(root.rightChild)

    def post_order_traversal(self, root="default"):
        if root == "default": 
            root = self.tree[0]
        if root == None:
            return()
        self.post_order_traversal(root.leftChild)
        self.post_order_traversal(root.rightChild)
        print(root.item)

    def in_order_traversal(self, root="default"):
        if root == "default": 
            root = self.tree[0]
        if root == None:
            return()
        self.in_order_traversal(root.leftChild)
        print(root.item)  
        self.in_order_traversal(root.rightChild)

class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.leftChild = None
        self.rightChild = None

    def insert_left_child(self, other):
        self.leftChild = other
        other.parent = self

    def insert_right_child(self, other):
        self.rightChild = other
        other.parent = self

def create_all_nodes():
    while True:
        nodeItem = input("Enter value of node (leave empty to end node creation): ")
        if len(nodeItem) == 0:
            print("")
            break
        t.create_node(nodeItem)

def add_children():
    print("Enter parent, child, and child direction (l/r) in that order.")
    print("Leave empty to end children creation: ")
    print("")
    while True:
        try:
            parent, child, direction = input("Enter parent, child, child direction: ").split()
            t.add_children(parent, child, direction)
        except:
            break

if __name__ == "__main__":
    t = Binary_Tree()
    create_all_nodes()
    add_children()
    t.pre_order_traversal()
    print("")
    t.post_order_traversal()
    print("")
    t.in_order_traversal()