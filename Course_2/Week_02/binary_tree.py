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
  
  def delete(self, value):
    is_exist, node = self.search(value)
    if is_exist:
      if node.p_left is None and node.p_right is None:
        self._deleteNoChild(node)
      elif node.p_left is None or node.p_right is None:
        self._deleteOneChild(node)
      else:
        self._deleteTwoChildren(node)
    else:
      raise ValueError('\'{}\' not exist.'.format(value))

    self.updateSize(self.root)
  
  def _deleteNoChild(self, node):
    parent_node = node.p_parent
    if node < parent_node:
      parent_node.p_left = None
    else:
      parent_node.p_right = None
    
    node.p_parent = None

  def _deleteOneChild(self, node):
    parent_node = node.p_parent
    swap_node = node.p_right if node.p_right is not None else node.p_left

    if node > parent_node:
      parent_node.p_right = swap_node
    else:
      parent_node.p_left = swap_node
    
    node.p_parent, node.p_left, node.p_right = None, None, None
  
  def _deleteTwoChildren(self, node):
    prev_node = self.previous_node(node.value)
    parent_node, left_node, right_node = node.p_parent, node.p_left, node.p_right

    if node < parent_node:
      parent_node.p_left = prev_node
    else:
      parent_node.p_right = prev_node
    if prev_node != left_node:
      left_node.p_parent = prev_node
    right_node.p_parent = prev_node

    prev_node_parent, prev_node_left = prev_node.p_parent, prev_node.p_left
    if prev_node != left_node:
      prev_node.p_left = left_node
    prev_node.p_right = right_node

    if prev_node_left is not None:
      if prev_node != left_node:
        prev_node_parent.p_right = prev_node_left
      else:
        prev_node.p_left = prev_node_left
    else:
      prev_node_parent.p_right = None

    node.p_parent, node.p_left, node.p_right = None, None, None

  def updateSize(self, node):
    if node.p_left is None and node.p_right is None:
      node.size = 1
      return 1
    elif node.p_left is None:
      node.size = self.updateSize(node.p_right) + 1
      return node.size
    elif node.p_right is None:
      node.size = self.updateSize(node.p_left) + 1
      return node.size
    else:
      node.size = self.updateSize(node.p_left) + self.updateSize(node.p_right) + 1
      return node.size
    
  def select(self, i):
    return self._select(self.root, i)
  
  def _select(self, node, i):
    left_node = node.p_left
    right_node = node.p_right
    a = 0 if left_node is None else left_node.size

    if a == i - 1:
      return node
    elif a >= i:
      return self._select(left_node, i)
    else:
      return self._select(right_node, i - a - 1)

  def display(self):
    self._display(self.root)

  def _display(self, node):
    if node is None:
      return
    self._display(node.p_left)
    print(node, ' Size: ', node.size)
    self._display(node.p_right)

if __name__ == '__main__':
  """
        10
      3     20
    1     12     30
  """
  print('*** Insert ###')
  binary_tree = BinaryTree(Node(10))
  binary_tree.insert(3)
  binary_tree.insert(20)
  binary_tree.insert(1)
  binary_tree.insert(30)
  binary_tree.insert(12)
  binary_tree.insert(11)
  binary_tree.insert(15)
  binary_tree.insert(25)
  binary_tree.insert(35)
  binary_tree.insert(14)
  binary_tree.display()

  print('*** Search ###')
  print(binary_tree.search(30))
  print('Minimum: ', binary_tree.minimum())
  print('Maximum: ', binary_tree.maximum())
  print(binary_tree.previous_node(12))
  print(binary_tree.next_node(10))

  print('*** Delete ###')
  binary_tree.delete(12)
  binary_tree.display()

  print('*** Select ***')
  print(binary_tree.select(5))