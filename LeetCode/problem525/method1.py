class Solution:
    def findMaxLength(self, nums ) :
        max_length=0

        for i,i_value in enumerate(nums):
            sum=-1 if i_value==0 else 1
            for j,j_value in enumerate(nums):
                if j<=i:
                    continue
                if j_value==0:
                    sum-=1
                else:
                    sum+=1
                if(sum==0):
                    max_length=max(max_length,j-i+1)

        return max_length

data=[0,1,1,1,0,1,0]
ins=Solution()
result=ins.findMaxLength(data)
print("data:",data)
print("result:",result)




         
            

