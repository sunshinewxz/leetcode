/*
The strategy is important. Exchange the position of the non-zero elements with the first zero.
*/
public class Main {

    public static void main(String[] args) {
        int[] nums = {1};
        moveZeroes(nums);
    }

    public static void moveZeroes(int[] nums) {
        int index = 0;
        int temp = 0;
        while(index < nums.length && nums[index] != 0){
          index = index + 1;
        }
        for(int i = index+1; i < nums.length; i++){
            if (nums[i] != 0){
                temp = nums[index];
                nums[index] = nums[i];
                nums[i] = temp;
                index = index + 1;
            }
        }

        for(int i = 0; i < nums.length; i++){
            System.out.println(nums[i]);
        }
    }

}
