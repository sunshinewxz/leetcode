/*
It is important to get the relationship between result and x.
*/


import static java.lang.Math.abs;

public class Main {

    public static void main(String[] args) {
        int x = 1534236469;
        int result = reverse(x);
        System.out.println(result);
    }

    public static int reverse(int x) {
        int result = 0;
        while (x != 0){
            if (abs(result) > 214748364)
                return 0;
            result = 10 * result + x % 10;
            x = x / 10;
        }

        return result;
    }
}


