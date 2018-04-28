/*
Longest Common Substring
Reverse S and become S'. Find the longest common substring between S and S'. However, we could see that the longest common substring method fails when there exists a reversed copy of a non-palindromic substring in some other part of S. To rectify this, each time we find a longest common substring candidate, we check if the substring’s indices are the same as the reversed substring’s original indices. If it is, then we attempt to update the longest palindrome found so far; if not, we skip this and find the next candidate.

Time complexity: O(n^2)
Space complexity: O(n^2)
*/

public static String longestPalindrome(String s){
        String s2 = new StringBuffer(s).reverse().toString();
        char[] ary = s.toCharArray();
        char[] ary2 = s2.toCharArray();
        String result = null;

        int[][] temp = new int[ary2.length][ary.length];
        int length = 0;
        for (int i = 0; i < ary.length; i++) {
            for (int j = 0; j < ary2.length; j++) {
                if (ary[i] == ary2[j]) {
                    if (i > 0 && j > 0) {
                        temp[i][j] = temp[i - 1][j - 1] + 1;
                    } else {
                        temp[i][j] = 1;
                    }
                } else {
                    temp[i][j] = 0;
                }

                if (temp[i][j] > length && i + 1 - temp[i][j] + j == ary.length - 1) {

                    length = temp[i][j];
                    int len_temp = temp[i][j];
                    int m = 0;
                    int tem = i;
                    char[] substring = new char[len_temp];
                    while (len_temp > 0) {
                        substring[m] = ary[tem];
                        m = m + 1;
                        tem = tem - 1;
                        len_temp = len_temp - 1;
                    }
                    result = String.valueOf(substring);

                }
            }
        }
        return result;
    }