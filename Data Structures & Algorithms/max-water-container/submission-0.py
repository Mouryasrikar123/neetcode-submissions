class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # high=width=height=res=0
        # for i in range(0,len(heights)):
        #     for j in range(i+1,len(heights)):
        #         width=j-i
        #         height=min(heights[j],heights[i])
        #         res=width*height
        #         if res>high:
        #             high=res
        # return high
        high=width=height=res=0
        i=0
        j=len(heights)-1
        while i < j:
            width=j-i
            height=min(heights[i],heights[j])
            res=width*height
            if res>high:
                high=res
            
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return high
            
        

        
