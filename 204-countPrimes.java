/*
Should be careful of the value of num
*/

import java.util.Arrays;

public class Main {

    public static void main(String[] args) {
        int n = 10;
        int result = countPrimes(n);
        System.out.println(result);
    }


    public static int countPrimes(int n) {
        int num = n-2;
        if (n < 2)
            return 0;

        boolean[] list = new boolean[n];
        Arrays.fill(list,2,n,true);
        for (int i=2;i*i<=n;i++){
            if (list[i]) {
                for (int j = i; i * j < n; j++) {
                    if (list[i*j]){
                        list[i * j] = false;
                        num = num - 1;
                    }

                }
            }
        }
        return num;
    }

}
