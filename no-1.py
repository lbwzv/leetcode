# for循环
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
            for i in range(len(nums)):
		x = nums[i]
		for i in range(i+1, len(nums)):
		    y = nums[i]
		    if target == x + y
			return{i, j]
	    return[]


# 哈希表
class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int]:
	hashtable = dict()
	for i nums in enumerate(nums):
# 这个函数的基本应用就是用来遍历一个集合对象，它在遍历的同时还可以得到当前元素的索引位置。
	    if target - num  in hashtable:
		return[hashtable[target - num], i]
	    hashtable[num[i]] = i
	return []
