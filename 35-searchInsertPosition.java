public class Main {

    public static void main(String[] args) {
        int[] nums = {1,3,5,6};
        int target = 0;
        int result = searchInsert(nums, target);
        System.out.println(result);
    }

    public static int searchInsert(int[] nums, int target) {
        int i = 0;
        while (i < nums.length && target >= nums[i]){
            if (target != nums[i])
                i = i + 1;
            else
                return i;
        }
        return i;

    }

}


