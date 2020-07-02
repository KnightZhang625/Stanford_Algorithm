# coding:utf-8

class Node(object):
  def __init__(self, value):
    self.value = value
    self.p_parent = None
    self.p_left = None
    self.p_right = None
    self.size = 1

  def __str__(self):
    return str(self.value)

  def __eq__(self, other):
    return self.value == other.value
  
  def __lt__(self, other):
    return self.value < other.value

class BinaryTree(object):
  def __init__(self, root):
    if not isinstance(root, Node):
      raise ValueError
    
    self.root = root
  
  def insert(self, value):
    self._insert(self.root, value)
    
  def _insert(self, node, value):
    if node.value == value:
      raise ValueError('\'{}\' exists.'.format(value))
    if value < node.value:
      if node.p_left is None:
        new_node = Node(value)
        new_node.p_parent = node
        node.p_left = new_node
        node.size += 1
      else:
        node.size += 1
        self._insert(node.p_left, value)
    else:
      if node.p_right is None:
        new_node = Node(value)
        new_node.p_parent = node
        node.p_right = new_node
        node.size += 1
      else:
        node.size += 1
        self._insert(node.p_right, value)

  def search(self, value):
    return self._search(value, self.root)

  def _search(self, value, node):
    if node is None:
      return (False, None)
    elif node.value == value:
      return (True, node)
    elif value < node.value:
      return self._search(value, node.p_left)
    else:
      return self._search(value, node.p_right)

  def minimum(self):
    return self._minimum(self.root)

  def _minimum(self, node):
    if node.p_left is None:
      return node
    return self._minimum(node.p_left)
  
  def maximum(self):
    return self._maximum(self.root)

  def _maximum(self, node):
    if node.p_right is None:
      return node
    return self._maximum(node.p_right)
  
  def next_node(self, value):
    is_exist, node = self.search(value)
    if is_exist:
      if node.p_right is not None:
        return self._minimum(node.p_right)
      else:
        return self._next_node(node, node.p_parent)
    else:
      raise ValueError('\'{}\' does not exist.'.format(value))
  
  def _next_node(self, base_node, node):
    if node is None:
      return 'Not Exist.'
    if node > base_node:
      return node
    return self._next_node(base_node, node.p_parent)
  
  def previous_node(self, value):
    is_exist, node = self.search(value)
    if is_exist:
      if node.p_left is not None:
        return self._maximum(node.p_left)
      else:
        return self._previous_node(node, node.p_parent)
    else:
      raise ValueError('\'{}\' does not exist.'.format(value))
  
  def _previous_node(self, base_node, node):
    if node is None:
      return 'Not Exist.'
    if node < base_node:
      return node
    return self._previous_node(base_node, node.p_parent)

  def display(self):
    self._display(self.root)

  def _display(self, node):
    if node is None:
      return
    self._display(node.p_left)
    print(node, node.size)
    self._display(node.p_right)

if __name__ == '__main__':
  binary_tree = BinaryTree(Node(10))
  binary_tree.insert(3)
  binary_tree.insert(20)
  binary_tree.insert(1)
  binary_tree.insert(30)
  binary_tree.insert(12)
  binary_tree.display()

  print(binary_tree.search(30))
  print('Minimum: ', binary_tree.minimum())
  print('Maximum: ', binary_tree.maximum())
  print(binary_tree.previous_node(12))
  print(binary_tree.next_node(10))