/*
It can avoid overflow through setting the variable of sum.
*/

public class NumArray {

    private int[] mems;

    public NumArray(int[] nums) {
        mems = new int[nums.length];
        int sum = 0;
        for (int i = 0; i < nums.length; i++){
            sum = sum + nums[i];
            mems[i] = sum;
        }

    }

    public int sumRange(int i, int j) {
        return i==0 ? mems[j] : mems[j] - mems[i - 1];
    }

    public static void main(String[] args) {
        int[] nums = {-2, 0, 3, -5, 2, -1};
        NumArray obj = new NumArray(nums);
        int param_1 = obj.sumRange(0,2);
        System.out.println(param_1);
    }

}