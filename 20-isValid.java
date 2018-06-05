import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        String s = "((";
        boolean result = isValid(s);
        System.out.println(result);
    }

    public static boolean isValid(String s) {
        if (s.length() == 0)
            return true;
        if (s.length() == 1)
            return false;
        Stack<Character> st = new Stack<Character>();
        for (int i=0; i<s.length(); i++){
            if(s.charAt(i)=='(' || s.charAt(i)=='[' || s.charAt(i)=='{')
                st.push(s.charAt(i));
            else{
                if (st.empty())
                    return false;
                char top = st.pop();
                if (s.charAt(i) == ')' && top != '(')
                    return false;
                if (s.charAt(i) == ']' && top != '[')
                    return false;
                if (s.charAt(i) == '}' && top != '{')
                    return false;
            }
        }
        return st.empty();
    }
}
