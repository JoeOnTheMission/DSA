class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        pos = [0]
        total = 0
        for num in nums:
            total+= num
            pos.append(total)
     
        neg =[]
        for j in range(len(nums)):
            neg.append(pos[-1] - pos[j+1])
     
        i = 0
        j = len(nums)-1
        while i <len(nums):
            num = nums[i]
            res[i] += max(num*i,pos[i]) - min(num*i,pos[i])
            res[i] += max(neg[i],num*j) - min(neg[i],num*j)
            print(i,j)
            i+=1
            j-=1
        return res