/*
index = i + 2 * j
I need to find out the relationship between i and j with different numRows.
The first row and the last row are different from the other rows, so I need to consider separately.
It is important to exclude exceptions (numRows < 2 || s.length() < 3 || numRows > s.length()).
*/




import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        String s = "ABC";
        int numRows = 4;
        String result = convert(s, numRows);
        System.out.println(result);
    }

    public static String convert(String s, int numRows) {
        StringBuffer result = new StringBuffer();
        char[] list = s.toCharArray();
        if (numRows < 2 || s.length() < 3 || numRows > s.length()){
            return s;
        }

        for (int i = 0; i < numRows; i++){
            result.append(list[i]);
            for (int j = numRows - 1, index = i + 2 * (j - i); index < s.length(); ){
                result.append(list[index]);
                if (index == i){
                    int m = result.length() - 1;
                    result.deleteCharAt(m);
                }
                if (i > 0 & i < numRows - 1 & index+2*i < s.length()){
                    result.append(list[index + 2 * i]);
                }
                j = j + numRows - 1;
                index = i + 2 * (j - i);
            }
        }
        return result.toString();
    }
}


