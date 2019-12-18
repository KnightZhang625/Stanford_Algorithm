"""Merge Sort"""
def merge(array_left, array_right):
	i, j = 0, 0
	merged_array = []

	while (i < len(array_left)) and (j < len(array_right)):
		if array_left[i] < array_right[j]:
			merged_array.append(array_left[i])
			i +=1
		else:
			merged_array.append(array_right[j])
			j +=1

	if i < len(array_left):
		merged_array.extend(array_left[i :])
	if j < len(array_right):
		merged_array.extend(array_right[j :])

	return merged_array

def sort(array):
	print(array)
	if len(array) < 2:
		return array

	mid = len(array) // 2
	array_left = sort(array[: mid])
	array_right = sort(array[mid :])
	return merge(array_left, array_right)

"""Point Object"""
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __setattr__(self, name, value):
		if name in self.__dir__():
			raise ValueError('{} exists'.format(name))
		return super().__setattr__(name, value)

	def __getattr__(self, name):
		if name not in self.__dir__():
			raise AttributeError('{} nit exists'.format(name))
		return super().__getattr__(name)

	def __str__(self):
		return '({},{})'.format(self.x, self.y)

	def __gt__(self, others):
		if isinstance(others, Point):
			return self.x > others.x
		else:
			raise ValueError

	def __eq__(self, others):
		if isinstance(others, Point):
			return self.x == others.x
		else:
			raise ValueError

"""Euclidean Distance"""
calculate_distance = lambda p1, p2: (p1.x - p2.x) **2 + (p1.y - p2.y) **2

"""Closest Pairs"""
def brute_force(points):
	if len(points) == 2:
		return calculate_distance(points[0], points[1]), points

	best = -1
	best_pair = None
	for i in range(len(points)):
		for j in range(1, len(points)):
			p1, p2 = points[0], points[1]
			distance = calculate_distance(p1, p2)
			if distance > best:
				best = distance
				best_pair = [p1, p2]
	return best, best_pair

def closestSplitPair(px, py, delta):
	mid_idx = len(px) // 2
	x_bar = px[mid_idx]
	candidates = [x for i, x in enumerate(py) if abs(x_bar.x - x.x) <= delta]
	
	best = delta
	best_pair = None
	for i in range(len(candidates)-1):
		for j in range(1, min(7, len(candidates)-i)):
			p, q = candidates[i], candidates[i+j]
			distance = calculate_distance(p, q)
			if distance < best:
				best = distance
				best_pair = [p, q]
	
	return best, best_pair

def closestPair(points_x, points_y):
	assert len(points_x) == len(points_y)
	if len(points_x) <= 3:
		return brute_force(points)

	mid = len(points_x) // 2
	LX = points_x[: mid]
	RX = points_x[mid :]

	LY = []
	RY = []
	mid_x = points_x[mid].x
	# this step is curcial, it ensures that the sorted Y of left and right splitted by mid_x
	# to be saved, however, in y sorted rank.
	for py in points_y:
		if py.x < mid_x:
			LY.append(py)
		else:
			RY.append(py)

	d_l, p_l = closestPair(LX, LY)
	d_r, p_r = closestPair(RX, RY)
	if d_l < d_r:
		delta = d_l
		best_pair = p_l
	else:
		delta = d_r
		best_pair = p_r

	best, best_p = closestSplitPair(points_x, points_y, delta)
	if best_p is not None:
		best_pair = best_p

	return best, best_pair

if __name__ == '__main__':
	import copy

	# array = [5, 2, 1, 6, 7, 12, 20, 15]
	# sorted_array = sort(array)
	# print(sorted_array)

	points = [Point(1, 2), Point(100, 200), Point(1000, 2000), 
			  Point(150, 2000.1), Point(100.1, 250), Point(123, 567), 
			  Point(12, 65), Point(3, 100), Point(20.1, 3), 
			  Point(50.1, 100.1), Point(1.1, 2.2), Point(5, 6), 
			  Point(8, 12), Point(20, 30), Point(50, 60)]
	points_copy = copy.deepcopy(points)

	points_x = sorted(points, key=lambda p: p.x)
	points_y = sorted(points, key=lambda p: p.y)

	best, best_pair = closestPair(points_x, points_y)
	print(best)
	print(best_pair[0], best_pair[1])