/*
It is important to know:
carry = (p + q) / 2;
temp = (p + q) % 2; 
*/
public class Main {

    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";
        String result = addBinary(a, b);
        System.out.println(result);
    }

    public static String addBinary(String a, String b) {
        int carry = 0;
        int p = 0;
        int q = 0;
        int m = a.length() - 1;
        int n = b.length() - 1;
        StringBuffer res = new StringBuffer();
        while (m >= 0 || n >= 0){
            p = m>=0? a.charAt(m)-'0':0;
            q = n>=0? b.charAt(n)-'0':0;
            res.append((p+q+carry) % 2);
            carry = (p+q+carry)/2;
            m = m - 1;
            n = n - 1;
        }
        if (carry>0)
            res.append(carry);
        return res.reverse().toString();
    }

}
