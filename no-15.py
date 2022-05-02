class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = list()

        #枚举
        for first in range(n):
            #需要和上一次枚举的数不同,continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            #c对应的指针初始指向数组的最右端
            third = n - 1
            target = - nums[first]
            # 枚举b
            for second in range (first + 1, n):
                #需要和上一次枚举的数不相同
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                # 需要保证b的指针在c的指针的左侧
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着b后续的增加，就不会有满足 a+b+c=0 并且b<c的c了
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first],nums[second], nums[third]] )
        return ans


