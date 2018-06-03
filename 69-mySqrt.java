/*
It is important to set appropriate type of data;
*/

public class Main {

    public static void main(String[] args) {
        int x = 2147395599;
        int result = mySqrt(x);
        System.out.println(result);
    }

    public static int mySqrt(int x) {
        long start = 0;
        long end = x/2 + 1;
        long index = 0;
        long temp = 0;
        while(start <= end){
            index = (start+end)/2;
            temp = index * index;
            if (temp == x)
                return (int)index;
            else if(temp > x)
                end = index - 1;
            else
                start = index + 1;

        }
        return (int)end;
    }

}

/*
The type of data has to be set as double.
*/

class Solution {
    public int mySqrt(int x) {
        if (x == 0)
            return 0;
        double temp = 0;
        double index = 1;
        while(temp != index){
            temp = index;
            index = (index + x/index)/2;
        }
        return (int)index;
    }
}
