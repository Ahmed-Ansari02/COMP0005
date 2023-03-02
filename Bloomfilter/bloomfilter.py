
class bloomfilter:
        def __init__(self,size, hash_count):
                self.size = size
                self.hash_count = hash_count
                self.bit_array = [0] * size
                self.hash_functions = self.generate_hash_functions()
        def generate_hash_functions(self):
            hash_fuctions = []
            for i in range(1,self.hash_count+1):
                hash_fuctions.append(self.generate_hash_function(i))
            return hash_fuctions
        def generate_hash_function(self,seed):
            def hash_function(value):
                return hash(value + str(seed)) % self.size
            return hash_function
        def add(self, value):
            for hash_function in self.hash_functions:
                self.bit_array[hash_function(value)] = 1
        def contain(self,value):
            for hash_function in self.hash_functions:
                if self.bit_array[hash_function(value)] == 0:
                    return False
            return True

file = open("./test3-dickens.txt", "r")
test_file = open("./test-search.txt","r")
my_bloomfilter = bloomfilter(9217517, 6)
for line in file:
    for word in line.split():
        my_bloomfilter.add(word)


for search_word in test_file:
    search_word = search_word.strip('\n')
    if not my_bloomfilter.contain(search_word):
        print(search_word + " Not Found")
