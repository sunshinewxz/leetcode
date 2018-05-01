/*
Dynamic Programming
*/

import static java.lang.Math.max;

public class Main {

    public static void main(String[] args) {
        int[] nums = {2,7,9,3,1};
        int result = rob(nums);
        System.out.println(result);
    }

    public static int rob(int[] nums) {
        int[] mems = new int[nums.length];
        if (nums.length <= 1)
            return nums.length < 1 ? 0 : nums[0];
        mems[0] = nums[0];
        mems[1] = max(nums[0], nums[1]);
        for (int i = 2; i < nums.length; i++){
            mems[i] = max(mems[i-2] + nums[i], mems[i-1]);
        }
        return mems[mems.length - 1];

    }
}
