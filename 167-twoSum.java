public class Main {

    public static void main(String[] args) {
        int[] numbers = {2,7,11,15};
        int target = 9;
        int[] result = twoSum(numbers,target);
        System.out.println(result[0]);
        System.out.println(result[1]);
    }

    public static int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length-1;
        int[] result = new int[2];
        int temp = numbers[start]+numbers[end];
        while (temp!=target){
            if (temp < target)
                start = start + 1;
            else
                end = end - 1;
            temp = numbers[start]+numbers[end];
        }
        result[0] = start+1;
        result[1] = end+1;
        return result;
    }

}
