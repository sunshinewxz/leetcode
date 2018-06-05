/*
Not familiar with this method.
*/

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        String s = "a1b2";
        List<String> result = letterCasePermutation(s);
        System.out.println(result);
    }

    public static List<String> letterCasePermutation(String S) {
        List<String> result = new ArrayList<>();
        dfs(S.toCharArray(),0,result);
        return result;
    }

    public static void dfs(char[] S, int i, List<String> result){
        if(i==S.length){
            result.add(new String(S));
            return;
        }
        dfs(S,i+1,result);
        if(!Character.isLetter(S[i]))
            return;
        S[i] ^= 1 << 5;
        dfs(S,i+1,result);
        S[i] ^= 1 << 5;
    }

}
