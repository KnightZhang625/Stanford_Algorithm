# coding:utf-8

class Node(object):
  def __init__(self, value=None, is_word=False):
    self.value = value
    self.is_word = is_word
    self.suffix_char = {}

class trieTree(object):
  def __init__(self):
    self.root = Node()
  
  def insert(self, word):
    node = self.root
    for w in word:
      if w not in node.suffix_char:
        node.suffix_char[w] = Node(value=w)
      node = node.suffix_char[w]
    node.is_word = True
  
  def search(self, word):
    node = self.root
    for w in word:
      if w not in node.suffix_char:
        return False
      node = node.suffix_char[w]
    # the w maybe at the middle of the tree, not a word
    if node.is_word:
      return True
    return False
  
  def traverse(self, node, word_cand):
    if len(node.suffix_char) == 0:
      # the node has no son, which indicates it must be the leaf
      self.candidates.append(word_cand + node.value)
      return

    for _, son_node in node.suffix_char.items():
      self.traverse(son_node, word_cand + node.value)
    
    if node.is_word:
      self.candidates.append(word_cand + node.value)
       
  def findCandidates(self, prefix):
    node = self.root
    for w in prefix:
      if w not in node.suffix_char:
        return None
      node = node.suffix_char[w]
    if len(node.suffix_char) == 0:
      return prefix
    else:
      self.candidates = []
      self.traverse(node, prefix[:-1])
      return self.candidates

if __name__ == '__main__':
  trie_tree = trieTree()
  trie_tree.insert('ab')
  trie_tree.insert('abc')
  trie_tree.insert('abde')
  trie_tree.insert('bc')

  for word in ['ab', 'abc', 'abde', 'bc', 'ac', 'abd', 'ba']:
    print(trie_tree.search(word))
  
  print(trie_tree.findCandidates('a'))