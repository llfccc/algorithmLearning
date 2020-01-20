package algo.problem01;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
public class TwoSum02 {
    public static void main(String[] args) {
        int[] nums={2, 7, 7, 7};
        int target=14;
        System.out.println(Arrays.toString(nums));
        Solution02 s1=new Solution02();
        int[] result=s1.twoSum(nums,target);
        System.out.println(Arrays.toString(result));
    }
}


class Solution02 {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map=new HashMap<>();
        for(int i =0;i< nums.length;i++){
            map.put(nums[i],i);
        }
        for(int i =0;i< nums.length;i++){
            int complement=target-nums[i];
            if(map.containsKey(complement) && map.get(complement)!=i){

                return new int[] {i,map.get(complement)};
            }

        }

        throw new IllegalArgumentException("No result");
    }
}