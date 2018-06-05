/*
Comparing the left part of the tree with the right part of the tree.
*/

public class Main {

    public static void main(String[] args) {
        TreeNode A1 = new TreeNode(1);
        TreeNode A2 = new TreeNode(2);
        TreeNode A3 = new TreeNode(2);
        TreeNode A4 = new TreeNode(3);
        TreeNode A5 = new TreeNode(4);
        TreeNode A6 = new TreeNode(4);
        TreeNode A7 = new TreeNode(3);

        A1.left = A2;
        A1.right = A3;
        A2.left = A4;
        A2.right = A5;
        A3.left = A6;
        A3.right = A7;
        A4.left = null;
        A4.right = null;
        A5.left = null;
        A5.right = null;
        A6.left = null;
        A6.right = null;
        A7.left = null;
        A7.right = null;


        boolean result = isSymmetric(A1);
        System.out.println(result);
    }

    public static boolean isSymmetric(TreeNode root) {
        if(root==null)
            return true;
        return checkNodes(root.left, root.right);
    }

    public static boolean checkNodes(TreeNode node1, TreeNode node2){
        if (node1 == null && node2 == null)
            return true;
        if (node1 == null || node2 == null)
            return false;

        if(node1.val != node2.val)
            return false;
        else
            return checkNodes(node1.left, node2.right) && checkNodes(node1.right, node2.left);
    }

}
