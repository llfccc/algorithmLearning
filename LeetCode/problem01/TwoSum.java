package algo.problem01;

import java.util.Arrays;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums={2, 7, 11, 15};
        int target=26;
        System.out.println(Arrays.toString(nums));
        Solution s1=new Solution();
        int[] result=s1.twoSum(nums,target);
        System.out.println(Arrays.toString(result));
    }
}


class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result=new int[2];
        for(int i =0;i< nums.length-1;i++){
            for (int j=i;j<nums.length;j++){
                if (nums[i]+nums[j]==target){
                    return new int[] {i,j};
                }
            }
        }

        throw new IllegalArgumentException("No result");
    }
}