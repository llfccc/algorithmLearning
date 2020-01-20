
import java.util.Arrays;

public class StartEnd02 {
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
        int[] result=new int[2];
        result[0]=findNum(nums,target,true);
        result[1]=findNum(nums,target,false)-1;;
        return result;
    }
    public int findNum(int[] nums,int target,Boolean left){
        // left 为true代表从左开始查找到的第一个值，为false代表从右开始查找的值

        int lo = 0;
        int hi = nums.length;

        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (nums[mid] > target || (left && target == nums[mid])) {
                hi = mid;
            }
            else {
                lo = mid+1;
            }
        }

        return lo;

    }
}
