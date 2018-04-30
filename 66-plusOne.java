public class Main {

    public static void main(String[] args) {
        int[] digits = {1,2,3,4};
        int[] result = plusOne(digits);
        for (int i = 0; i < result.length; i++)
            System.out.println(result[i]);
    }

    public static int[] plusOne(int[] digits) {
        int l = digits.length - 1;
        if (digits[l] < 9){
            digits[l] = digits[l] + 1;
        }
        else{
            while(digits[l] == 9 && l - 1 >= 0){
                digits[l] = 0;
                l = l - 1;
            }
            if (l>=0 && digits[l] != 9)
                digits[l] = digits[l] + 1;
            else{
                int[] result;
                result = new int[digits.length + 1];
                result[0] = 1;
                for (int i = 1; i < result.length; i++)
                    result[i] = 0;
                return result;
            }
        }
        return digits;
    }

}


