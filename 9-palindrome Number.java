/*
First solution by myself
*/

public class Main {

    public static void main(String[] args) {
        int x = 10;
        boolean result = isPalindrome(x);
        System.out.println(result);
    }

    public static boolean isPalindrome(int x) {
        if (x < 0)
            return false;
        int reverse = 0;
        int xc = x;
        while (xc > 0){
            int temp = xc % 10;
            reverse = 10 * reverse + temp;
            xc = xc / 10;
        }
        if (reverse == x)
            return true;
        else
            return false;
    }

}

/*
Second solution: only consider the situation of the half of the input data
*/
public class Solution {
    public bool IsPalindrome(int x) {
        // Special cases:
        // As discussed above, when x < 0, x is not a palindrome.
        // Also if the last digit of the number is 0, in order to be a palindrome, 
        // the first digit of the number also needs to be 0.
        // Only 0 satisfy this property.
        if(x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int revertedNumber = 0;
        while(x > revertedNumber) {
            revertedNumber = revertedNumber * 10 + x % 10;
            x /= 10;
        }
        
        // When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        // For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123, 
        // since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == revertedNumber || x == revertedNumber/10;
    }
}
