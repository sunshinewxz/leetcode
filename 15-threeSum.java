/*
Make sure the position of the first number, and than search the other two numbers to make the sum equal -nums[i]
O(n^2)
*/
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Main {
    public static void main(String[] args){
        int nums[] = {-2,0,0,2,2};
        List result = threeSum(nums);
        System.out.println(result);
    }


    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if(nums.length < 3)
            return result;
        for(int i = 0; i < nums.length; i++){
            if (nums[i] > 0)
                break;
            if(i > 0 && nums[i] == nums[i-1])
                continue;
            int begin = i + 1;
            int end = nums.length - 1;
            while(begin < end){
                int sum = nums[i] + nums[begin] + nums[end];
                if(sum == 0){
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(nums[i]);
                    temp.add(nums[begin]);
                    temp.add(nums[end]);
                    result.add(temp);
                    begin = begin + 1;
                    end = end - 1;
                }
                else if(sum > 0)
                    end = end - 1;
                else if(sum < 0)
                    begin = begin + 1;
            }
        }
        HashSet h = new HashSet();
        h.addAll(result);
        result.clear();
        result.addAll(h);
        return result;
    }
}
