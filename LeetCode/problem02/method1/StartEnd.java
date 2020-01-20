package method1;

import java.util.Arrays;

public class StartEnd {
    public static void main(String[] args) {
        int[] nums={5,7,7,8,8,10};
        int target=8;
        System.out.print("原始数据为：");
        System.out.println(Arrays.toString(nums));
        Solution s1=new Solution();
        int[] result=s1.searchRange(nums,target);
        System.out.print("答案为：");
        System.out.println(Arrays.toString(result));
    }

}

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result=new int[] {-1,-1};
        for(int i=0;i<nums.length;i++){
            if (nums[i]==target){
                result[0]=i;
                break;
            }
        }
        if (result[0]==-1){
            return result;
        }

        for(int j=nums.length-1;j>=0;j--){
            if(nums[j]==target){
                result[1]=j;
                break;
            }
        }
        return result;
    }
}
