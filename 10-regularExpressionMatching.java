/*
This is a wrong solution, I cannot contain the situation when s='aaa' and p='ab*a*c*a'.
*/


public class Main {

    public static void main(String[] args) {
        String s = "aaa";
        String p = "ab*a*c*a";
        boolean result = isMatch(s, p);
        System.out.println(result);
    }

    public static boolean isMatch(String s, String p) {
        int s_i = 0;
        int p_i = 0;
        //int i = 0;
        if (p.isEmpty())
            return s.isEmpty();
        if (p.charAt(0) == '*' && !s.isEmpty())
            return false;
        //int length = max(s.length(), p.length());
        while(s_i < s.length() && p_i < p.length()){

            if (s.charAt(s_i) == p.charAt(p_i) || p.charAt(p_i) == '.'){
                s_i = s_i + 1;
                p_i = p_i + 1;
                if (s_i < s.length() && p_i >= p.length() && p.charAt(p_i - 1) != '*')
                    return false;
//                i = i + 1;
            }
            else if (p.charAt(p_i) == '*' && (p.charAt(p_i - 1) == s.charAt(s_i) || p.charAt(p_i - 1) == '.')){
                p_i = p_i + 1;
                s_i = s_i + 1;
//                i = i + 1;
            }
            else if (s.charAt(s_i) != p.charAt(p_i) && p_i + 1 >= p.length())
                return false;
            else if (s.charAt(s_i) != p.charAt(p_i) && p.charAt(p_i + 1) == '*'){
                p_i = p_i + 2;
                if (p_i >= p.length() && s_i < s.length())
                    return false;
            }
            else
                return false;

        }
        if (s_i >= s.length() && p_i < p.length() && p.charAt(p_i) != '*'){
            return false;
        }
        else if (s_i >= s.length() && p_i < p.length() && p.charAt(p_i) == '*'){
            p_i = p_i + 1;
            while(p_i < p.length() && p.charAt(p_i) == '*')
                p_i = p_i + 1;
            if (p_i < p.length())
                return false;
        }
        return true;
    }

}



/*
The second solution provided in the leetcode website.
Divide the whole problem into smaller problems and solve it by recursion.
*/

class Solution {
    public boolean isMatch(String text, String pattern) {
        if (pattern.isEmpty()) return text.isEmpty();
        boolean first_match = (!text.isEmpty() && 
                               (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.'));
        
        if (pattern.length() >= 2 && pattern.charAt(1) == '*'){
            return (isMatch(text, pattern.substring(2)) || 
                    (first_match && isMatch(text.substring(1), pattern)));  //There are two ways to satisfy the request.
        } else {
            return first_match && isMatch(text.substring(1), pattern.substring(1));
        }
    }
}

/*
The third solution: Dynamic Planning
*/
public boolean isMatch(String s, String p) {  
    if(s.length()==0 && p.length()==0)  
        return true;  
    if(p.length()==0)  
        return false;  
    boolean[][] res = new boolean[s.length()+1][p.length()+1];  
    res[0][0] = true;  
    for(int j=0;j<p.length();j++)  
    {  
        if(p.charAt(j)=='*')  
        {  
            if(j>0 && res[0][j-1]) res[0][j+1]=true;  
            if(j<1) continue;  
            if(p.charAt(j-1)!='.')  
            {  
                for(int i=0;i<s.length();i++)  
                {  
                    if(res[i+1][j] || j>0&&res[i+1][j-1]   
                    || i>0 && j>0 && res[i][j+1]&&s.charAt(i)==s.charAt(i-1)&&s.charAt(i-1)==p.charAt(j-1))  
                        res[i+1][j+1] = true;  
                }  
            }  
            else  
            {  
                int i=0;  
                while(j>0 && i<s.length() && !res[i+1][j-1] && !res[i+1][j])  
                    i++;  
                for(;i<s.length();i++)  
                {  
                    res[i+1][j+1] = true;  
                }  
            }  
        }  
        else  
        {  
            for(int i=0;i<s.length();i++)  
            {  
                if(s.charAt(i)==p.charAt(j) || p.charAt(j)=='.')  
                    res[i+1][j+1] = res[i][j];  
            }  
        }  
    }  
    return res[s.length()][p.length()];  
} 




