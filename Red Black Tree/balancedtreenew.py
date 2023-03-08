# Time complexity = O(logN)
# Space complexity = O(n)
class Node:

    def __init__(self, value):
        self.left = None
        self.parent = None
        self.right = None
        self.value = value
        self.colour = 'R'

class redblacktree:

    def __init__(self):
        self.empty = Node("xyz")
        self.empty.colour = 'B'
        self.empty.left = None
        self.empty.right = None
        self.root = self.empty


    def insert(self, data):
        node = Node(data)
        node.parent = None
        node.value = data
        node.colour = 'R'
        node.left = self.empty
        node.right = self.empty

        tempval = None
        rt = self.root

        while rt != self.empty:
            tempval = rt
            if node.value < rt.value:
                rt = rt.left
            else:
                rt = rt.right

        node.parent = tempval

        if tempval == None:
            self.root = node
        elif node.value < tempval.value:
            tempval.left = node
        else:
            tempval.right = node

        if node.parent == None:
            node.colour = 'B'
            return

        if node.parent.parent == None:
            return

        self.insertcontinue(node)

    def search(self, node, value):
        if node == self.empty:
            return False
        elif value == node.value:
            return True
        if value < node.value:
            return self.search(node.left, value)
        return self.search(node.right, value)

    def leftrotate(self, rotateval):
        rchild = rotateval.right
        rotateval.right = rchild.left
        if rchild.left != self.empty:
            rchild.left.parent = rotateval
        rchild.parent = rotateval.parent
        if rotateval.parent == None:
            self.root = rchild
        elif rotateval == rotateval.parent.left:
            rotateval.parent.left = rchild
        else:
            rotateval.parent.right = rchild
        rchild.left = rotateval
        rotateval.parent = rchild

    def rightrotate(self, rotateval):
        lchild = rotateval.left
        rotateval.left = lchild.right
        if lchild.right != self.empty:
            lchild.right.parent = rotateval
        lchild.parent = rotateval.parent
        if rotateval.parent == None:
            self.root = lchild
        elif rotateval == rotateval.parent.right:
            rotateval.parent.right = lchild
        else:
            rotateval.parent.left = lchild
        lchild.right = rotateval
        rotateval.parent = lchild

    def colourswap(self, a, l):
        if a.colour == 'R':
            a.colour = 'B'
            l.parent.colour = 'B'
            l.parent.parent.colour = 'R'
            l = l.parent.parent

    def insertcontinue(self, leaf):
        while leaf.parent.colour == 'R':
            if leaf.parent == leaf.parent.parent.right:
                aunt = leaf.parent.parent.left
                if aunt.colour == 'R':
                    self.colourswap(aunt, leaf)
                    leaf = leaf.parent.parent
                else:
                    if leaf == leaf.parent.left:
                        leaf = leaf.parent
                        self.rightrotate(leaf)
                    leaf.parent.colour = 'B'
                    leaf.parent.parent.colour = 'R'
                    self.leftrotate(leaf.parent.parent)
            else:
                aunt = leaf.parent.parent.right
                if aunt.colour == 'R':
                    self.colourswap(aunt, leaf)
                    leaf = leaf.parent.parent
                else:
                    if leaf == leaf.parent.right:
                        leaf = leaf.parent
                        self.leftrotate(leaf)
                    leaf.parent.colour = 'B'
                    leaf.parent.parent.colour = 'R'
                    self.rightrotate(leaf.parent.parent)
            if leaf == self.root:
                break
            self.root.colour = 'B'

            # intended order of values : (3,1,5,7,6,8,9,10)

    def searchtree(self, a):
        return self.search(self.root, a)

    def printTree(self, node, last):
            if node != self.empty:
                if last:
                    print("R: ", end=' ')

                else:
                    print("L: ", end=' ')
                s_color = "RED" if node.colour == 'R' else "BLACK"
                print(str(node.value) + "(" + s_color + ")")
                self.printTree(node.left, False)
                self.printTree(node.right, True)

        # Function to call print
    def display(self):
            self.printTree(self.root, True)

if __name__ == "__main__":
        tree = redblacktree()
        file = open("./test1-mobydick.txt", "r")
        #test_file = open("./test-search.txt", "r")
        for line in file:
            for word in line.split():
                tree.insert(word)
        print(tree.searchtree("kremlin"))

    

