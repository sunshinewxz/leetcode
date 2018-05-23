import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String pattern = "abba";
        String str = "dog dog dog dog";
        boolean result = wordPattern(pattern, str);
        System.out.println(result);
    }


    public static boolean wordPattern(String pattern, String str) {
        char[] pat = pattern.toCharArray();
        String[] word = str.split(" ");
        Map<Character, String> maps = new HashMap<>();
        if (pat.length != word.length)
            return false;
        for (int i = 0; i < pat.length; i++){
            if(maps.containsKey(pat[i])){
                if (!maps.get(pat[i]).equals(word[i]))
                    return false;
            }
            else{
                if(maps.containsValue(word[i]))
                    return false;
                maps.put(pat[i],word[i]);
            }
        }
        return true;

    }

}
