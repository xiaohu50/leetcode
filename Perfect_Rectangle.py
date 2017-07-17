from collections import defaultdict

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # inspired by https://github.com/kamyu104/LeetCode/blob/master/Python/perfect-rectangle.py
        # 对于所有的矩形的四个角所在点，有如下的特性
        #   所有点不能同时是两个矩形的公共方向的角（比如同是left_bottom）
        #   如果点位于最终大矩形的四角，则独一份，无共点
        #   如果点位于最终大矩形的四条边上（非四角），则只有可能是两个点公共拼成直线
        #   如果点位于最终大矩形的内部，则只有可能是三个矩形（两角一边）或者是四个矩形（四角）的共点
        # 非常直觉的上面的点的特征是题目的必要条件，至于充分条件没有想到合适的解决方法
        left = min([rect[1] for rect in rectangles])
        right = max([rect[3] for rect in rectangles])
        top = max([rect[2] for rect in rectangles])
        bottom = min([rect[0] for rect in rectangles])
        
        points = defaultdict(int)
        
        for b, l, t, r in rectangles:
            # use a bitmap for direction check
            for corner, bm in zip(((b, l), (b, r), (t, l), (t, r)), (1, 2, 4, 8)):
                if points[corner] & bm:
                    # 检查是否和别的矩形有公共方向的点
                    return False
                else:
                    points[corner] |= bm
            
        for x, y in points:
            # 判断除最终大矩形四个角点之外的所有点
            if (x>bottom and x<top) or (y>left and y<right) :
                if points[(x, y)] not in (3, 5, 10, 12, 15):
                    return False
        
        return True
