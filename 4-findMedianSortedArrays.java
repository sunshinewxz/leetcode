/*
Recursive Approach

len(left_A)=i,len(right_A)=m−i.

If we can ensure:
1. len(left_part) = len(right_part)
2. max(left_part) = min(right_part)

then we divide all elements in {A, B} into two parts with equal length, and one part is always greater than the other.
median = [max(left_part) + min(right_part)] / 2

To ensure these two conditions, we just need to ensure:
1. i + j = m - i + n - j (or: m - i + n - j + 1)
if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1) / 2 - i
2. B[j - 1] <= A[i] and A[i - 1] <= B[j]

If i = 0, then A[i - 1] doesn't exist, then we don't need to check A[i - 1] <= B[j]; i = m, j = 0, j = n are the same conditions

Binary search following steps described below:
1. Set imin = 0, imax = m, then start searching in [imin, imax]
2. Set i = (imin + imax) / 2, j = (m + n + 1) / 2 - i
3. Now we have len(left_part) = len(right_part), and there are only 3 situations that we may encounter:
	(1)(j = 0 or i = m or B[j - 1] <= A[i]) and (i = 0 or j = n or A[i - 1] <= B[j])
	(2)j > 0 and B[j - 1] > A[i]      i++
	(3)i > 0 and A[i - 1] > B[j]      i--
4. when m + n is odd: median = max(A[i - 1], B[j - 1])
when m + n is even: median = [max(A[i - 1], B[j - 1]) + min(A[i], B[j])] / 2

*/

class Solution {
    public double findMedianSortedArrays(int[] A, int[] B) {
        int m = A.length;
        int n = B.length;
        if (m > n) { // to ensure m<=n
            int[] temp = A; A = B; B = temp;
            int tmp = m; m = n; n = tmp;
        }
        int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
        while (iMin <= iMax) {
            int i = (iMin + iMax) / 2;
            int j = halfLen - i;
            if (i < iMax && B[j-1] > A[i]){
                iMin = iMin + 1; // i is too small
            }
            else if (i > iMin && A[i-1] > B[j]) {
                iMax = iMax - 1; // i is too big
            }
            else { // i is perfect
                int maxLeft = 0;
                if (i == 0) { maxLeft = B[j-1]; }
                else if (j == 0) { maxLeft = A[i-1]; }
                else { maxLeft = Math.max(A[i-1], B[j-1]); }
                if ( (m + n) % 2 == 1 ) { return maxLeft; }

                int minRight = 0;
                if (i == m) { minRight = B[j]; }
                else if (j == n) { minRight = A[i]; }
                else { minRight = Math.min(B[j], A[i]); }

                return (maxLeft + minRight) / 2.0;
            }
        }
        return 0.0;
    }
}

