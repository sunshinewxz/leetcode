/*
consider all the situations
*/
public class Main {
    public static void main(String[] args){
        int[] height = {1,8,6,2,5,4,8,3,7};
        int result = maxArea(height);
        System.out.println(result);
    }


    public static int maxArea(int[] height) {
        int area = 0;
        for(int i = 0; i < height.length-1; i++){
            for(int j = i+1; j < height.length; j++){
                int temp = (j-i) * Math.min(height[i], height[j]);
                if(temp > area)
                    area = temp;
            }
        }
        return area;
    }

}

/*
use some strategies
*/
public static int maxArea(int[] height) {
        int l = 0;
        int r = height.length-1;
        int area = 0;
        int temp = 0;
        while(l < r){
            temp = (r-l) * Math.min(height[l],height[r]);
            if(temp > area)
                area = temp;
            if(height[l] < height[r])
                l = l + 1;
            else
                r = r - 1;
        }
        return area;
    }