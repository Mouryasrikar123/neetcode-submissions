class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i=0
        # j=1
        # result=[]
        # while j<len(nums):
        #     if nums[i]+nums[j]==target:
        #         result.append([i,j])
        #         return result
        #         break
        #     else:
        #         i+=1
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
                

            


        