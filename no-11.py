#如果左指针对应的值小于等于右指针对应的值，可以断定 若果左指针位置不变，无论右指针如何移动，容器容量都不会超过之前。

class Solution:
    def maxArea(self, height: List[int]) -> int:
    	l, r = 0, len(height) - 1
    	a = []
    	while l < r:
    		s = min(height[l],height[r]) * (r - l)
    		if height[l] <= height[r]:
    			l += 1
    		else:
    			r -= 1
    		a.append(s)
    	return max(a)



#暴力
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        a = []
        for i in range(n):
            for j in range(i + 1,n):
                s = (j - i) * min([height[i],height[j]])
                a.append(s)
        return max(a)