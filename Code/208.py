class TrieNode:
    def __init__(self):
        self.children = dict()


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.words = set()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self._get_last_node(prefix)
        return node is not None

    def _get_last_node(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children.get(char)
        return current

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("word")
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
