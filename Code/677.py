class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.count = 0
        self.children = dict()
        self.end = False
        self.end_val = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root_nodes = dict()
        self.key = dict()

    def insert(self, key: str, val: int) -> None:
        val = val - self.key.get(key, 0)
        self.key[key] = val

        self._insert_in_trie(key, val, self.root_nodes)

    def sum(self, prefix: str) -> int:
        node = self._get_last_node(prefix)
        return node.count if node else 0

    def _insert_in_trie(self, key, val, trie_node_dict):

        start = key[0]
        node = trie_node_dict.get(start, TrieNode(start))
        node.count += val
        trie_node_dict[start] = node
        if key[1:]:
            self._insert_in_trie(key[1:], val, node.children)

    def _get_last_node(self, key):
        start_dict = self.root_nodes
        node = None
        for val in key:
            node = start_dict.get(val, None)
            if not node:
                return None
            start_dict = node.children
        return node


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("key", 3)
print(obj.sum("ke"))
obj.insert("ke", 3)
obj.insert("key", 6)
obj.insert("kez", 6)
print(obj.sum("ke"))
obj.insert("kez", 3)
print(obj.sum("ke"))
