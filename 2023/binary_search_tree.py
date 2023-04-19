if __name__ == "__main__":

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

    def in_order_traversal(rootNode):
        if rootNode is None:
            return()
        in_order_traversal(rootNode.leftChild)
        print(rootNode.item)  
        in_order_traversal(rootNode.rightChild)

    def pre_order_traversal(rootNode):
        if rootNode is None:
            return()
        print(rootNode.item)  
        pre_order_traversal(rootNode.leftChild)
        pre_order_traversal(rootNode.rightChild)
    
    def post_order_traversal(rootNode):
        if rootNode is None:
            return()
        post_order_traversal(rootNode.leftChild)
        post_order_traversal(rootNode.rightChild)
        print(rootNode.item)  

    values = []
    while True:
        value = input("Enter value (leave empty to end): ")
        if len(value) == 0:
            break
        values.append(int(value))

    root = Node(values[0])
    values.pop(0)
    for value in values:
        parent = root
        while True:
            if value > parent.item:
                if parent.rightChild is None:
                    parent.insert_right_child(Node(value))
                    break
                else:
                    parent = parent.rightChild
            else:
                if parent.leftChild is None:
                    parent.insert_left_child(Node(value))
                    break
                else:
                    parent = parent.leftChild

    in_order_traversal(root)
    print("")
    pre_order_traversal(root)
    print("")
    post_order_traversal(root)
