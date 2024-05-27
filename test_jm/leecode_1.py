# -*- coding: utf-8 -*-
# __author__:jean
# 2024/4/18 14:28

import numpy as np

# 快速排序
class Solution(object):
    def sortArray(self,nums):
        """
        :type nums: List[int]
        :type: List[int]
        """
        # n = len(nums)
        # for i in range(n):
        #     for j in range(0,n-i-1):
        #         if nums[j] - nums[j+1] > 0:
        #             nums[j+1], nums[j] = nums[j], nums[j+1]
        # return nums

        if len(nums) <= 1:
            return nums
        else:

            pick_ele = nums[0]
            lefts = [i for i in nums[1:] if i <= pick_ele]
            rights = [j for j in nums[1:] if j > pick_ele]

            return self.sortArray(lefts) + [pick_ele] + self.sortArray(rights)


    ## 冒泡排序【1，23，4，5，7，19】
    def rankBubble(self, list_num):
        for i in range(len(list_num) - 1):
            for j in range(i + 1, len(list_num)):
                if list_num[j] > list_num[i]:
                    list_num[i], list_num[j] = list_num[j], list_num[i]
        return list_num

    def bubble_sort(self, arr):
        n = len(arr)
        # 遍历所有数组元素
        for i in range(n):
            # 最后 i 个元素已经排好序，不需要再次比较
            for j in range(0, n - i - 1):
                # 如果当前元素大于下一个元素，则交换它们
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


# 矩阵反转
def rotate(matrix):
    n = len(matrix)
    # 先沿对角线镜像对称二维矩阵
    for i in range(n):
        for j in range(i, n):
            # 同时赋值
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    # 然后反转二维矩阵的每一行
    list_final = []
    for row in matrix:
        row_new = reverse(row)
        list_final.append(row_new)
    return list_final


def reverse(arr):
    i, j  = 0, len(arr)-1
    while j > i:
        arr[j], arr[i] = arr[i], arr[j]
        i = i + 1
        j = j - 1
    return arr

# 回文串
class Solution2:

    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 返回以 left 和 right 为中心的最长回文子串
            return s[left + 1:right]

        longest = ''
        for i in range(len(s)):
            # 以单个字符为中心
            palindrome1 = expandAroundCenter(i, i)
            # 以两个相邻字符之间的空隙为中心
            palindrome2 = expandAroundCenter(i, i + 1)
            # 更新最长回文子串
            longest = max(longest, palindrome1, palindrome2, key=len)

        return longest

# 回文串
def centerAround(str1, le_index, rt_index):
    # 左边和右边
    while str1[le_index] == str1[rt_index] and le_index >= 0 and rt_index < len(str1):
        le_index = rt_index - 1
        rt_index = rt_index + 1
    return str1[le_index+1 : rt_index]


def findPalindrome(str1):
    if len(str1) < 2:
        return str1
    longest = ''
    for i in range(len(str1)):
        # dcbcd 单个字符为中心
        p1 = centerAround(str1, i, i)
        p2 = centerAround(str1, i, i+1)
        longest = max(p1, p2, key=len)
    return longest

# 零钱问题: dp[i]至少需要多少枚硬币凑出来
def money_pbm():
    ele_coin = [1,2,5]
    total = 32

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for i in range(1, total+1):
        for cin in ele_coin:
            if i >= cin:
                dp[i] = min(dp[i], dp[i - cin] + 1)  # 上个状态的最优解+1

    # 如果dp[amount]仍然是float('inf')，说明无法凑出该金额，返回-1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]

# 最长公共子串
def longest_common_str(str1,str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            pass


# 双指针
class ListNode():

    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):
    slow = head
    fast = head

    while ((fast is not None) and (fast.next is not None)):
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


from collections import deque
def find_min_path():
    pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1-2-3-4
def listnodereverse_no(head):
    pre = None
    cur = head
    while cur is not None:
        next_node = cur.next
        cur.next = pre
        pre = cur
        cur = next_node
    return pre

# 1-2-3-4
def listnodereverse_no1(head):
    pre = None
    cur = head
    while cur is not None:
        next_node = cur.next
        cur.next = pre
        # 更新 pre
        pre = cur
        # 更新当前节点
        cur = next_node
    return pre

## 递归

def listnodereverse_circle(head):
    if head is None or head.next is None:
        return head

    last = listnodereverse_circle(head.next)
    head.next.next = head
    head.next = None

    return last

def test_listnodereverse_circle():
    # 示例：创建一个链表 1 -> 2 -> 3 -> 4 -> 5，然后反转它
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    reversed_head = listnodereverse_circle(head)
    while reversed_head is not None:
        print(reversed_head.val)
        reversed_head = reversed_head.next


import math
def binary_find(needed_list, num):
    le = 0
    rt = len(needed_list) - 1

    while le <= rt :
        mid_index = ( le + rt ) // 2 # 向下取证好算一些
        if needed_list[mid_index] < num:
            le = mid_index + 1
        elif needed_list[mid_index] > num :
            rt = mid_index - 1
        else:
            return mid_index

    return -1


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.traverse(root, 0)
        return self.res

    # 遍历二叉树
    def traverse(self, root, depth):
        if not root:
            return
        # 前序遍历位置
        depth += 1
        # 遍历的过程中记录最大深度
        self.res = max(self.res, depth)
        self.traverse(root.left, depth)
        self.traverse(root.right, depth)
        # 后序遍历位置
        depth -= 1

def test_max_depth():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # 创建一个Solution3对象
    solution = Solution3()
    # 调用maxDepth方法，得到最大深度
    print(solution.maxDepth(root))  # 输出: 3


def minCoins(coins, amount):
    # 创建一个数组来保存凑出每个金额所需的最少硬币数量
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 凑出金额为 0 不需要硬币

    # for i in range (1, amount + 1):
    #     for coin in coins:
    #         if coin <= i:
    #             dp[i] = min(dp[i], dp[i-coin] + 1)


    # 遍历每个金额，求出凑出该金额所需的最少硬币数量
    for i in range(1, amount + 1):
        # 遍历每个面额的硬币
        for coin in coins:
            # 如果当前面额的硬币可以凑出金额 i
            if coin <= i:
                # 更新凑出金额 i 所需的最少硬币数量
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # 如果凑不出目标金额，则返回 -1，否则返回凑出目标金额所需的最少硬币数量
    return dp[amount] if dp[amount] != float('inf') else -1



def merge1( nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        return nums2
    if n == 0:
        return nums1[0:m]
    num1_sub = nums1[0:m]
    num2_sub = nums2[0:n]
    num_all = num1_sub + num2_sub
    print(num_all)
    aaaa = sorted(num_all)
    return aaaa


class SolutionQ1(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m==0 and n==0:
            nums1 = []
            return nums1
        if m==0 and n != 0:
            return nums2

        if n==0:
            return nums1[0:m-1]

        i = 0
        j = 0
        nums_new = []
        # or 有一个真会执行，必须都真
        while (i < m) and (j < n):
            # print(i, j)
            if nums1[i] < nums2[j]:
                nums_new.append(nums1[i])
                i = i + 1
            elif nums1[i] == nums2[j]:
                nums_new.append(nums1[i])
                nums_new.append(nums2[j])
                i = i + 1
                j = j + 1
            else:
                nums_new.append(nums2[j])
                j = j + 1
        if i <= m-1:
            print('nums1 没完')
            sub1 = nums1[i:m]
            for ii in sub1:
                nums_new.append(ii)
            return nums_new
        if j <= n-1:
            print("nums2 meiwan")
            sub2 = nums2[j:n]
            for jj in sub2:
                nums_new.append(jj)
            return nums_new

def maxProfit(prices):
    # # 第一次
    # if not prices:
    #     return 0
    #
    # n = len(prices)
    #
    # # 初始化两个数组
    # profit1 = [0] * n
    # profit2 = [0] * n
    #
    # # 计算 profit1
    # min_price = prices[0]
    # for i in range(1, n):
    #     min_price = min(min_price, prices[i])
    #     profit1[i] = max(profit1[i - 1], prices[i] - min_price)
    #
    # # 计算 profit2
    # max_price = prices[n - 1]
    # for i in range(n - 2, -1, -1):
    #     max_price = max(max_price, prices[i])
    #     profit2[i] = max(profit2[i + 1], max_price - prices[i])
    #
    # # 计算最大收益
    # max_profit = 0
    # for i in range(n):
    #     max_profit = max(max_profit, profit1[i] + profit2[i])
    #
    # return max_profit

    if not prices:
        return 0

    n = len(prices)

    min_price = prices[0]
    profit1 = [[0] * n]
    for i in range(1,n):
        min_price = min(min_price, prices[i])
        profit1 = max(profit1[i-1], prices[i] - min_price)

    max_price = prices[n-1]
    profit2 = [[0] * n]
    for i in range(n-2,-1,-1):
        max_price = max(max_price, prices[i])
        profit2 = max(profit2[i+1], max_price - prices[i])
    # # 计算最大收益
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit1[i] + profit2[i])

    return max_profit












# 示例用法
prices = [10, 9, 8, 7, 10]
print(maxProfit(prices))  # 输出应为 3

if __name__ == '__main__':
    # 示例用法
    rst1 = SolutionQ1().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    print(rst1)
    print(merge1([1,2,3,0,0,0], 3, [2,5,6], 3))
    coins = [1, 2, 5]  # 给定硬币的面额
    amount = 11  # 目标金额
    print(minCoins(coins, amount))  # 输出凑出目标金额所需的最少硬币数量
    # 测试示例
    # solution = Solution()
    # # 回文串
    # print(Solution2().longestPalindrome("babad"))  # "bab" 或 "aba"
    # print(Solution2().longestPalindrome("cbbd"))  # "bb"
    # print(findPalindrome("cbbd"))
    test_max_depth()
    import math
    needed_list = [1,2,3,4,5]
    mid_index1 = math.ceil(len(needed_list) / 2)
    #####排序######
    print(mid_index1)

    nums = [5,1,1,2,0,0]
    rst = Solution().sortArray(nums)
    rst1 = Solution().rankBubble(nums)
    print(rst, rst1)
    #####动态规划#####
    print(money_pbm())
    ######是否有环#####
    # 测试
    # 创建一个有环的链表
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head  # 形成环

    print("链表是否有环:", hasCycle(head))  # 输出：True

    test_listnodereverse_circle()
    # s1 = 'a'
    # s2 = 'z'
    # print(ord(s1))
    # print(ord(s2))
    # mat = [[1,2,3,],[4,5,6],[7,8,9]]
    # print(len(mat))
    # print(mat)
    # sss = rotate(mat)
    # print(sss)

    # 去掉空格
    # s = "  a good   example"
    # print(s.split(" "))
    # # 字符串只包含字符和数字
    # s1 = ''.join(c.lower() for c in s if c.isalnum())
    # print(s1)
    # s = s1[::-1] # 字符串反转
    # print(s)
    # ###### uplift #######
    # y_true = [1, 0, 0, 1, 1, 1, 0, 1]
    # uplift = [0.1, 0.1, 0.1, 0.1, 0.1, -0.3, -0.4, 1,1,1]
    # treatment = [1, 1, 1, 1, 0, 0, 0, 0]
    # y_true, uplift, treatment = np.array(y_true), np.array(uplift), np.array(treatment)
    #
    # desc_score_indices = np.argsort(uplift, kind="mergesort")[::-1]
    # print(desc_score_indices)
    #
    # print(np.where(np.diff(uplift)))
    # print(np.where(np.diff(uplift))[0])




