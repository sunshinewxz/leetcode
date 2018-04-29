/*
Actually this problem is not difficult, it just needs to consider lots of situations, so I debug it for a long time.
Considering different situations is pretty important.
*/


public class Main {

    public static void main(String[] args) {
        String str = "42";
        int result = myAtoi(str);
        System.out.println(result);
    }

    public static int myAtoi(String str) {
        char[] temp = str.trim().toCharArray();   //delete all the whitespace characters
        char[] fin = new char[1000];
        int len = 0;                              //define len to avoid too large data to oversize
        int start = 0;                            //define start to delete the 0 in the start of the data
        if (temp.length <= 0)
            return 0;
        if ((temp[0] < '0' || temp[0] > '9') & temp[0] != '-' & temp[0] != '+'){
            return 0;
        }
        if (temp[0] == '+'){
            temp[0] = '0';
        }

        long result = 0;
        int i = 0;
        if (temp[0] == '-'){
            i = 1;
            fin[0] = '-';
            len = len + 1;
        }
        while(i < temp.length && temp[i] >= '0' && temp[i] <= '9'){
            fin[i] = temp[i];
            len = len + 1;
            i = i + 1;
        }
        if (fin[0] == '-'){
            int m = 1;
            while(fin[m] == '0'){
                m = m+1;
            }
            start = m;
            if (len-start > 11)
                return -2147483648;
        }

        if (fin[0] != '-'){
            int m = 0;
            while(fin[m] == '0'){
                m = m+1;
            }
            start = m;
            if (len-start > 10)
                return 2147483647;
        }
        for (int j = start; j < len; j++){
            result = result * 10 + fin[j] - '0';

        }
        result = (fin[0] == '-')? -result:result;
        if (result > 2147483647){
            return 2147483647;
        }

        if (result < -2147483648)
            return -2147483648;
        int final_result = (int)result;
        return final_result;
    }
}


/*
The second solution: clear and logical
*/
public class Solution {  
    public int atoi(String str) {  
        // 1. whitespaces  
        str = str.trim();  

        // 2. null or empty string  
        if (str == null || str.length() == 0) return 0;  
          
        // 3. +/- sign  
        boolean positive = true;  
        int i = 0;  
        if (str.charAt(0) == '+') {  
            i++;  
        } else if (str.charAt(0) == '-') {  
            positive = false;  
            i++;  
        }  
          
        // 4. calculate real value  
        double tmp = 0;  
        for ( ; i < str.length(); i++) {  
            int digit = str.charAt(i) - '0';  
              
            if (digit < 0 || digit > 9) break;  
              
            // 5. handle min & max  
            if (positive) {  
                tmp = 10*tmp + digit;  
                if (tmp > Integer.MAX_VALUE) return Integer.MAX_VALUE;  
            } else {  
                tmp = 10*tmp - digit;  
                if (tmp < Integer.MIN_VALUE) return Integer.MIN_VALUE;  
            }  
        }  
          
        int ret = (int)tmp;  
        return ret;  
    }  
}  


/*
The third solution
*/

public class Solution {
    public int myAtoi(String str) {
        if (str.isEmpty()) return 0;
        int sign = 1, base = 0, i = 0, n = str.length();
        while (i < n && str.charAt(i) == ' ') ++i;
        if (str.charAt(i) == '+' || str.charAt(i) == '-') {
            sign = (str.charAt(i++) == '+') ? 1 : -1;
        }
        while (i < n && str.charAt(i) >= '0' && str.charAt(i) <= '9') {
            if (base > Integer.MAX_VALUE / 10 || (base == Integer.MAX_VALUE / 10 && str.charAt(i) - '0' > 7)) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            base = 10 * base + (str.charAt(i++) - '0');
        }
        return base * sign;
    }
}

