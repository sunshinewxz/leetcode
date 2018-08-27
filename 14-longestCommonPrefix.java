/*
Consider the situation when strs.length == 0
*/

public class Main {
    public static void main(String[] args){
        String strs[] = {"aa","a"};
        String result = longestCommonPrefix(strs);
        System.out.println(result);
    }


    public static String longestCommonPrefix(String[] strs) {
        if (strs.length < 1)
            return "";
        StringBuilder re = new StringBuilder("");
        int j=0;
        while(j<strs[0].length()){
            for(int i = 1; i < strs.length; i++){
                if (j == strs[i].length() || strs[0].charAt(j) != strs[i].charAt(j))
                    return re.toString();
            }
            re.append(strs[0].charAt(j));
            j = j + 1;
        }
        return re.toString();
    }
}


/*
Using dichotomy is more efficient
*/
public String longestCommonPrefix(String[] strs) {
        if(strs.length < 1)
            return "";
        int minLength = Integer.MAX_VALUE;
        for(String str:strs){
            minLength = Math.min(minLength,str.length());
        }
        int low = 0;
        int high = minLength;
        int middle = 0;
        while(low <= high){
            middle = (low + high) / 2;
            if(isCommonPrefix(strs,middle))
                low =  middle + 1;
            else
                high = middle - 1;
        }
        return strs[0].substring(0,(low+high)/2);
    }

    public static boolean isCommonPrefix(String[] strs, int middle){
        String s = strs[0].substring(0,middle);
        for(int i = 1; i < strs.length; i++){
            if(!strs[i].startsWith(s))
                return false;
        }
        return true;
    }