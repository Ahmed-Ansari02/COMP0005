class Binary_search_tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def get(self, value):
        if (value == self.value):
            return value
        elif (value > self.value and self.right):
            return self.right.get(value)
        elif (value < self.value and self.left):
            return self.left.get(value)  
        else:
            return -1
    def put(self, value):
        if (value == self.value):
            return
        if (value > self.value):
            if (self.right == None):
                self.right = Binary_search_tree(value)
            else:
                self.right.put(value)
        elif (value < self.value):
            if (self.left == None):
                self.left = Binary_search_tree(value)
            else:
                self.left.put(value)


file = open("./test3-dickens.txt", "r")
binary_search_tree = None
test_file = open("./test-search.txt", "r")

for line in file:
    for word in line.split():
        if (binary_search_tree == None):
            binary_search_tree = Binary_search_tree(word)
        else:
            binary_search_tree.put(word)
for word in test_file:
    word = word.strip('\n');
    if(binary_search_tree.get(word) == -1):
        print(word + " not found")