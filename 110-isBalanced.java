/*
Runtime beats 85.84% of java submission.
Calculate the depth of every node.
*/

import static java.lang.Math.max;

public class Main {

    public static void main(String[] args) {
//        TreeNode A1 = new TreeNode(3);
//        TreeNode A2 = new TreeNode(9);
//        TreeNode A3 = new TreeNode(20);
//        TreeNode A4 = new TreeNode(15);
//        TreeNode A5 = new TreeNode(7);
//
//        A1.left = A2;
//        A1.right = A3;
//        A2.left = null;
//        A2.right = null;
//        A3.left = A4;
//        A3.right = A5;
//        A4.left = null;
//        A4.right = null;
//        A5.left = null;
//        A5.right = null;

        TreeNode A1 = new TreeNode(1);
        TreeNode A2 = new TreeNode(2);
        TreeNode A3 = new TreeNode(2);
        TreeNode A4 = new TreeNode(3);
        TreeNode A5 = new TreeNode(3);
        TreeNode A6 = new TreeNode(4);
        TreeNode A7 = new TreeNode(4);

        A1.left = A2;
        A1.right = A3;
        A2.left = A4;
        A2.right = A5;
        A3.left = null;
        A3.right = null;
        A4.left = A6;
        A4.right = A7;
        A5.left = null;
        A5.right = null;
        A6.left = null;
        A6.right = null;
        A7.left = null;
        A7.right = null;

        boolean result = isBalanced(A1);
        System.out.println(result);
    }

    public static int subHeight(TreeNode node){
        if (node == null)
            return 0;
        return 1+max(subHeight(node.left),subHeight(node.right));
    }

    public static boolean isBalanced(TreeNode root) {
        boolean result;
        if (root == null)
            return true;
        int l = subHeight(root.left);
        int r = subHeight(root.right);
        if(l+1<r || r+1<l)
            return false;
        else
            return isBalanced(root.left) && isBalanced(root.right);

    }

}
