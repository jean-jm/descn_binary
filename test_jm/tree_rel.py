# -*- coding: utf-8 -*-
# __author__:jean
# 2024/4/24 15:28

from sklift.metrics import uplift_curve, uplift_auc_score, uplift_by_percentile,qini_auc_score


class NodeTree():
    def __int__(self):
        pass

    def find_ways(self,node):
        cur = node.val
        le = node.left
        rt = node.right
        if cur + le == 12:
            return [node.val, node.le.val]
        else:
            print("---")
        return False


if __name__ == '__main__':

    # 示例用法
    W = 5
    n = 3
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]
    print(K)







