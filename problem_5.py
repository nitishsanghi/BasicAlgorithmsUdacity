class TrieNode:
    def __init__(self):
        # Initialize this node in the Trie
        self.children = {}
        self.is_word = False
    
    def insert(self, x):
        ## Add a child node in this Trie
        self.children[x] = TrieNode()
    
    def suffixes_helper(self, result, suffix = ''):
        # Recursive function that collects the suffix for
        # all complete words below this point
        if self.children:
            for x, node in self.children.items():
                if node.is_word:
                    result.append(suffix + x)
                node.suffixes_helper( result, suffix + x)
                
    
    def suffixes(self):
        result = []
        self.suffixes_helper(result)
        return result
    
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if word is None:
            print("Invalid None type object detected")
            return
        node = self.root
        for x in word:
            if x not in node.children:
                node.insert(x)
            node = node.children[x]
        node.is_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        if prefix is "":
            return
        node = self.root
        for x in prefix:
            if x not in node.children:
                return None
            node = node.children[x]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

MyTrie1 = Trie()
wordList1 = [
    None,"a", "an", 
    "fun", "fund", 
    "trie", "tried", "trig"
]
for word in wordList1:
    MyTrie1.insert(word)

MyTrie2 = Trie()
wordList2 = [
    "", "an", 
    "fun", "fund", 
    "trie", "tried", "trig"
]
for word in wordList2:
    MyTrie2.insert(word)
    

from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');

def g(prefix):
    if prefix != '':
        prefixNode = MyTrie1.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(g,prefix='');

def h(prefix):
    if prefix != '':
        prefixNode = MyTrie2.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(h,prefix='');