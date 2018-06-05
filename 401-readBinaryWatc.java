/*
Although the code seems simple, the performance is not good. This method needs a lot of time.
*/

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        int num = 1;
        List<String> result = readBinaryWatch(num);
        System.out.println(result);
    }

    public static List<String> readBinaryWatch(int num) {
        List<String> result = new ArrayList<>();
        for(int h = 0; h < 12; h++){
            for(int m = 0; m < 60; m++){
                if (Integer.bitCount(h * 64 + m) == num)
                    result.add(String.format("%d:%02d",h,m));
            }
        }
        return result;
    }

}
