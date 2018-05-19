/*
My method
*/
public class Main {

    public static void main(String[] args) {
        String s = "Hello World";
        int result = lengthOfLastWord(s);
        System.out.println(result);
    }

    public static int lengthOfLastWord(String s) {
        String[] word = s.split("\\s+");
        if (word.length < 1)
            return 0;
        return word[word.length-1].length();
    }

}

/*
Just one line of code.
*/
class Solution {
    public int lengthOfLastWord(String s) {
        return s.trim().length()-s.trim().lastIndexOf(" ")-1;
    }
}