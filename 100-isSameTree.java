
public class Main {

    public static void main(String[] args) {
        TreeNode A1 = new TreeNode(1);
        TreeNode A2 = new TreeNode(2);
        TreeNode A3 = new TreeNode(3);
        A1.left = A2;
        A1.right = A3;
        A2.left = null;
        A2.right = null;
        A3.left = null;
        A3.right = null;

        TreeNode B1 = new TreeNode(1);
        TreeNode B2 = new TreeNode(2);
        TreeNode B3 = new TreeNode(3);
        B1.left = B2;
        B1.right = B3;
        B2.left = null;
        B2.right = null;
        B3.left = null;
        B3.right = null;

        boolean result = isSameTree(A1, B1);
        System.out.println(result);
    }


    public static boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null && q==null)
            return true;
        if(p==null || q==null)
            return false;
        if(p.val == q.val){
            //System.out.println("---------------------");
            return isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
        }

        else
            return false;
    }

}
