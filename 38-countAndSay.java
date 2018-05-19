public class Main {

    public static void main(String[] args) {
        int n = 5;
        String result = countAndSay(n);
        System.out.println(result);
    }

    public static String countAndSay(int n) {
        if (n<2)
            return "1";
        String s = "1";
        int num = 1;
        StringBuffer temp = new StringBuffer();
        for (int i=1; i<n; i++){
            num = 1;
            temp.setLength(0);
            for (int j=1; j<s.length(); j++){
                if(s.charAt(j)==s.charAt(j-1))
                    num = num + 1;
                else{
                    temp.append(num).append(s.charAt(j-1));
                    num = 1;
                }

            }
            temp.append(num).append(s.charAt(s.length()-1));
            s = temp.toString();
        }
        return temp.toString();

    }

}