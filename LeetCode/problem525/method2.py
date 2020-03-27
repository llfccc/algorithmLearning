class Solution:
    def findMaxLength(self, nums ) :

        for index,value in enumerate(nums):
            nums[index]=-1 if value==0 else 1
        print("trans_data:",data)
        sum = 0; max_length = 0;
        count_dict={}

        for i,i_value in enumerate(nums):
            sum += nums[i];
            if sum in count_dict:
                max_length = max(max_length, i - count_dict[sum]);
                
            else:
                count_dict[sum] = i;           
       
        print("count_dict",count_dict)
        return max_length

data=[0,1,1,1,0,1,0]
print("raw_data:",data)
ins=Solution()
result=ins.findMaxLength(data)

print("result:",result)




         
            

