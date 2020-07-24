class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for char in word:
            node = current.children.get(char, TrieNode())
            current.children[char] = node
            current = node
        current.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        current = [self.root]
        return self._search_recursive(word, current)

    def _search_recursive(self, word, possible_list):
        for current in possible_list:
            if not word:
                if current.end:
                    return True
                return False
            char = word[0]
            if char == "." and current.children:
                possible_list = [value for key, value in current.children.items()]
            elif char in current.children:
                possible_list = [current.children[char]]
            else:
                continue
            possible = self._search_recursive(word[1:], possible_list)
            if possible:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("base")
print(obj.search("b..."))
