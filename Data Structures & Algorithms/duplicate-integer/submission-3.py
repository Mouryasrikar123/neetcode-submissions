class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res=[]
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
        # for i in nums:
        #     if i not in res:
        #         res.append(i)
        # if len(nums)-len(res)>0:
        #     return True 
        # else:
        #     return False 