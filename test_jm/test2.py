# -*- coding: utf-8 -*-
# __author__:jean
# 2024/4/19 21:58


def isValid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            return False
    print(stack)
    ### not 没有的意思
    return not stack


if __name__ == '__main__':

    # 测试
    print(isValid("()"))  # True
    # print(isValid("()[]{}"))  # True
    # print(isValid("(]"))  # False
    # print(isValid("([)]"))  # False
    # print(isValid("{[]}"))  # True
    # print(isValid(""))
    #
    # a = [1,2,4]
    # print(a.pop())
    # print(a.pop())
    #
    # a = []
    # if not a:
    #     print('1111')
    # else:
    #     print("2222")
    s = 'aaa'
    print(s[1:2])
