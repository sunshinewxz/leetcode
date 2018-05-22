/*
The number of ASCII code is 256
*/


public class Main {

    public static void main(String[] args) {
        String s = "paper";
        String t = "title";
        boolean result = isIsomorphic(s, t);
        System.out.println(result);
    }

    public static boolean isIsomorphic(String s, String t) {
        if (s.length() != t.length())
            return false;
        int[] m1 = new int[256];
        int[] m2 = new int[256];
        for (int i = 0; i < s.length(); i++){
            if (m1[s.charAt(i)] != m2[t.charAt(i)])
                return false;
            m1[s.charAt(i)] = i + 1;
            m2[t.charAt(i)] = i + 1;
        }
        return true;

    }

}
