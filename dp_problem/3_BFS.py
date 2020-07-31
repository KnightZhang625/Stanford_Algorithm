# coding:utf-8

from queue import Queue

class TreeNode:
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None

def findMinDepth(tree):
	tree.insert(0, None)
	for i, x in enumerate(tree):
		if i == 0:
			continue
		elif i == 1:
			tree[i] = TreeNode(x)
		elif x != 'null':
			tree[i] = TreeNode(x)
			parent = tree[i // 2]
			if i % 2 == 0:
				parent.left = tree[i]
			else:
				parent.right = tree[i]
	
	# return tree[1]

	q = Queue()
	q.put(tree[1])
	depth = 1

	while not q.empty():
		for _ in range(q.qsize()):
			cur_node = q.get()
			if cur_node.left is None and cur_node.right is None:
				return depth
			if cur_node.left is not None:
				q.put(cur_node.left)
			if cur_node.right is not None:
				q.put(cur_node.right)
		depth +=1

def iterate(node):
	if node is None:
		return
	iterate(node.left)
	print(node.val)
	iterate(node.right)


from queue import Queue

def upRotate(code, idx):
		code = [int(c) for c in code]
		if code[idx] == 9:
				code[idx] = 0
		else:
				code[idx] = code[idx] + 1
		return ''.join([str(c) for c in code])

def downRotate(code, idx):
		code = [int(c) for c in code]
		if code[idx] == 0:
				code[idx] = 9
		else:
				code[idx] = code[idx] - 1
		return ''.join([str(c) for c in code])

class Solution:
	def openLock(self, deadends: list, target: str) -> int:
		candidates = Queue()
		candidates.put('0000')
		visits = ['0000']
		step = 0
		while not candidates.empty():
			for _ in range(candidates.qsize()):
				cur_code = candidates.get()
				if cur_code in deadends:
					continue
				if cur_code == target:
					return step

				for idx in range(4):
					up_code = upRotate(cur_code, idx)
					if up_code not in visits:
						candidates.put(up_code)
						visits.append(up_code)
					down_code = downRotate(cur_code, idx)
					if down_code not in visits:
						candidates.put(down_code)
						visits.append(down_code)
			step +=1
	
		return -1

	def openLockFast(self, deadends: list, target: str) -> int:
		cand_a = {'0000': None}
		cand_b = {target: None}
		temp = {}
		visits = set()
		step = 0

		while len(cand_a) != 0 and len(cand_b) != 0:
			if len(cand_a) == len(cand_b):
				cand_a, cand_b = cand_b, cand_a
			for code in cand_a:
				if code in deadends:
					continue
				if code in cand_b:
					return step
				visits.add(code)
				for idx in range(4):
					up_code = upRotate(code, idx)
					if up_code not in visits:
						temp[up_code] = None
					down_code = downRotate(code, idx)
					if down_code not in visits:
						temp[down_code] = None
			cand_a = cand_b
			cand_b = temp
			temp = {}
			step +=1
	
		return -1

if __name__ == '__main__':
	print(findMinDepth([1, 2, 3, 4, 5, 6, 7, 8, 9]))
	solution = Solution()
	print(solution.openLock(['8888'], '0009'))
	print(solution.openLockFast(["0201","0101","0102","1212","2002"], '0202'))