class Solution:
    def searchRange(self, nums: list, target: int):
        idx=[-1,-1]
        if not nums:
            return idx
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)>>1
            if nums[mid]==target:
                idx[0]=mid
                while idx[0]>0 and nums[idx[0]-1]==target:
                    idx[0]-=1
                idx[1]=mid
                while idx[1]<len(nums)-1 and nums[idx[1]+1]==target:
                    idx[1]+=1
                return idx
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return idx
if __name__=="__main__":
    a=Solution()
    print(a.searchRange([1,1,2],1))