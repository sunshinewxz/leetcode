/*
runtime beats 99.67% of java submissions
*/

import static java.lang.Math.min;

public class Main {

    public static void main(String[] args) {
        TreeNode A1 = new TreeNode(3);
        TreeNode A2 = new TreeNode(9);
//        TreeNode A3 = new TreeNode(20);
//        TreeNode A4 = new TreeNode(15);
//        TreeNode A5 = new TreeNode(7);

        A1.left = null;
        A1.right = A2;
        A2.left = null;
        A2.right = null;
//        A3.left = A4;
//        A3.right = A5;
//        A4.left = null;
//        A4.right = null;
//        A5.left = null;
//        A5.right = null;

        int result = minDepth(A1);
        System.out.println(result);
    }

    public static int nodeDepth(TreeNode node, int depth){
        if (node.right == null && node.left == null)
            return depth + 1;
        if (node.right != null && node.left != null)
            return 1+min((nodeDepth(node.left,depth)),(nodeDepth(node.right,depth)));
        else{
            //depth = 1+min((nodeDepth(node.left,depth)),(nodeDepth(node.right,depth)));
            return node.right == null? 1+nodeDepth(node.left,depth):1+nodeDepth(node.right,depth);
        }
    }

    public static int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        int depth = 0;
        depth = nodeDepth(root,depth);
        return depth;
    }

}

/*
Combine two functions into one function.
*/
import static java.lang.Math.min;
class Solution {
    public static int minDepth(TreeNode root) {
        if (root == null)
            return 0;
        if (root.right != null && root.left != null)
            return 1+min(minDepth(root.left),minDepth(root.right));
        else{
            return root.right == null? 1+minDepth(root.left):1+minDepth(root.right);
        }
    }
}
