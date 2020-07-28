# coding:utf-8

# 动态规划的穷举有点特别，因为这类问题存在「重叠子问题」, 如果暴力穷举的话效率会极其低下,
# 所以需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算。
# 只有列出正确的「状态转移方程」才能正确地穷举。
# 重叠子问题、最优子结构、状态转移方程就是动态规划三要素,
# 状态转移方程: 明确 base case -> 明确「状态」-> 明确「选择」 -> 定义 dp 数组/函数的含义。

"""
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)
"""

# 递归动态规划
def fibonacci(number, cache={}):
  if number < 1:
    return 0
  elif number == 1:
    return 1
  elif number in cache:
    return cache[number]
  else:
    cache[number] = fibonacci(number-1, cache) + fibonacci(number-2, cache)
    return cache[number]

# 传统动态规划
def fibonacci_dp(number):
  array = [0]
  array.extend([1, 1])
  if 0 <= number <= 2:
    return array[number]
  for i in range(3, number+1):
    array.append(array[i-1]+array[i-2])
  return array[number]

# 状态压缩, 空间复杂度 -> O(1)
# 如果我们发现每次状态转移只需要 DP table 中的一部分，那么可以尝试用状态压缩来缩小 DP table 的大小，只记录必要的数据。
def fibonacci_update(number):
  if number <= 2:
    return 1
  pprev_num = 1
  prev_num = 1
  res = 0
  for _ in range(3, number+1):
    res = pprev_num + prev_num
    pprev_num = prev_num
    prev_num = res
  return res
  
def coinChange(coins, amount):
  cache = {}

  def dp(n):
    if n in cache:
      return cache[n]
    if n == 0:
      return 0
    if n < 0:
      return -1
    res = 1e10
    for coin in coins:
      subproblem = dp(n - coin)
      if subproblem == -1:
        continue
      res = min(res, 1 + subproblem)
    cache[n] = res if res != 1e-10 else -1
    return cache[n]
  
  return dp(amount)

def coinChangeWithBack(coins, amount):
  array = [amount+1 for i in range(amount+1)]
  array[0] = 0
  batch_trace = {}
  for i in range(1, amount + 1):
    for c in coins:
      if i - c < 0:
        continue
      # array[i] = min(array[i], array[i-c] + 1)
      if array[i] < (array[i-c] + 1):
        batch_trace[i] = i
        array[i] = array[i]
      else:
        batch_trace[i] = i - c
        array[i] = array[i-c] + 1
  
  prev_amount = batch_trace[amount]
  if prev_amount == amount:
    selected_coins = []
  else:
    selected_coins = [amount - prev_amount]
    while prev_amount > 0:
      selected_coins.append(prev_amount - batch_trace[prev_amount])
      prev_amount = batch_trace[prev_amount]
      
  return array[amount] if array[amount] != amount+1 else -1, selected_coins

if __name__ == '__main__':
  print(fibonacci(50))
  print(fibonacci_dp(50))
  print(fibonacci_update(50))

  print(coinChange((1, 2, 5), 11))
  print(coinChangeWithBack((1, 2, 5), 11))