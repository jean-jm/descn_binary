# -*- coding: utf-8 -*-
# __author__:jean
# 2024/5/14 12:48
import re


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def subsets(nums):
    def backtrack(start, path):
        # 将当前子集加入结果集
        res.append(path[:])
        # 从start开始，逐个将元素加入子集中
        for i in range(start, len(nums)):
            path.append(nums[i])
            # 递归调用，继续往子集中加入下一个元素
            backtrack(i + 1, path)
            # 回溯，将刚刚加入的元素从子集中移除，准备尝试下一个元素
            path.pop()

    res = []
    backtrack(0, [])
    return res


def find_longset_cal_rst(s):
    # s = "1-2*3+4abcd3*aa4"
    # # 们需要假设字符串中的数字和运算符是连续且有效的（即不存在像2++3这样的无效表达式）。
    # valid_expressions = re.findall(r'[-+*\d]+', s)
    # print(valid_expressions)
    valid_exp = re.findall(r'[-+*\d]+',s)
    long_exp = ""
    final_rst = None

    for exp in valid_exp:
        try:
            rst = eval(exp)
            # 最长子串的最大结果
            if (len(exp) > len(long_exp)) or (len(exp) == len(long_exp) and rst > final_rst):
                long_exp = exp
                final_rst = rst
        except Exception as e:
            pass

    return long_exp, final_rst


def find_adjacent_ones(matrix):
    m, n = len(matrix), len(matrix[0])
    groups = []  # 用于存储每个团的1的累加和

    # 辅助函数：检查一个位置(i, j)是否属于一个团
    def dfs(i, j, group):
        # 检查边界和当前值
        if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] != 1:
            return

            # 将当前位置标记为已访问（设置为-1或其他非1值）
        matrix[i][j] = -1

        # 将当前1添加到团中
        group.append((i, j))

        # 递归地检查相邻位置
        dfs(i - 1, j, group)  # 上
        dfs(i + 1, j, group)  # 下
        dfs(i, j - 1, group)  # 左
        dfs(i, j + 1, group)  # 右

    # 遍历矩阵中的每个元素
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                group = []  # 初始化新团
                dfs(i, j, group)  # 深度优先搜索以找到团
                if len(group) > 1:  # 忽略只包含一个1的团
                    groups.append(sum(1 for _, _ in group))  # 将团内1的数量添加到列表中

    return sum(groups)  # 返回所有团内1的累加和


def find_group(matrix):
    m,n = len(matrix), len(matrix[0])
    groups = []

    # 对每个元素去递归得到group
    def dfs(i, j, group):
        if i < 0 or j < 0 or j >= n or i >= m or matrix[i][j] != 1:
            return

        matrix[i][j] = -1

        group.append((i,j))

        # 上下左右去探索
        dfs(i-1, j, group) # 上
        dfs(i+1, j, group) # 下
        dfs(i, j+1, group) # ri
        dfs(i, j-1, group) # LE

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1: # 0 就不搜索了，节约算力
                group = []
                dfs(i, j, group)
                if len(group) > 1:
                    groups.append( sum(1 for _,_ in group))
    return max(groups)













# # 示例矩阵
# matrix = [
#     [0, 1, 1, 0],
#     [0, 1, 0, 0],
#     [0, 0, 1, 1],
#     [0, 0, 0, 0]
# ]

# 调用函数并打印结果
# print(find_adjacent_ones(matrix))  # 输出应为 6，因为有两组相邻的1，每组包含3个1





if __name__ == '__main__':

    # 示例用法
    # 创建一棵二叉树
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 中序遍历
    print("中序遍历结果：")
    inorder_traversal(root)

    ######

    # 示例用法
    nums = [1, 2, 3]
    result = subsets(nums)
    print("输入数组的所有子集为：", result)

    ### 运算
    a, b = find_longset_cal_rst("bbb1-2*3aaa3-1*8")
    print(a, b)
    matrix = [
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 1],

    ]
    #len(m)代表行；ma[0]代表列
    print(len(matrix), len(matrix[0]))



