/*
Time Limited Exceeded
input:2126753390
and 1702766719 is the first bad version
*/
public class Main {

    public static void main(String[] args) {
        int n = 5;
        int result = firstBadVersion(n);
        System.out.println(result);
    }

    public static boolean isBadVersion(int version){
        switch (version)
        {
            case 1:
                return false;
            case 2:
                return false;
            case 3:
                return false;
            case 4:
                return true;
            case 5:
                return true;
        }
        return true;
    }

    public static int firstBadVersion(int n) {
        int index = n/2 + 1;
        int start = 1;
        int end = n;
        while(true){
            if(isBadVersion(index) == true){
                if(isBadVersion(index - 1) == false)
                    return index;
                end = index;
                index = (start+end)/2;
            }
            if(isBadVersion(index) == false){
                if(isBadVersion(index+1) == true)
                    return index+1;
                start = index;
                index = (start+end)/2;
            }
        }

    }

}

/*
Accepted
*/

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        int index;
        while(start<end){
            index = start+(end-start)/2;
            if(isBadVersion(index))
                end = index;
            else
                start = index+1;
        }
        return start;
    }
}
