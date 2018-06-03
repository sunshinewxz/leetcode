/*
There are lots of situations needed to be considered.
*/

public class Main {

    public static void main(String[] args) {
        String s = "0P";
        boolean result = isPalindrome(s);
        System.out.println(result);
    }

    public static boolean isPalindrome(String s) {
        char[] word = s.toCharArray();
        if (s.length()==0 || s.length()==1)
            return true;
        int start = 0;
        int end = s.length()-1;
        //turn all uppercase letters into lowercase letters
        for (int i=0;i<s.length();i++){
            if(word[i] >= 'A' && word[i] <= 'Z')
                word[i] = (char)('a'+s.charAt(i)-'A');
        }
        while(start<=end){
            char st = word[start];
            char en = word[end];
            start = start + 1;
            end = end - 1;
            while(!((st>='a' && st<='z') || (st>='0' && st<='9')) && start < s.length()){
                st = word[start];
                start = start + 1;
            }
            while(!((en>='a' && en<='z') || (en>='0' && en<='9')) && end > 0){
                en = word[end];
                end = end - 1;
            }

            if (((st>='a' && st<='z') || (st>='0' && st<='9')) && ((en>='a' && en<='z') || (en>='0' && en<='9')) && (st != en))
                return false;
        }
        return true;

    }

}
