/*
It is important to master List<List<Integer>> related commands and recursive usage.
*/

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        TreeNode A1 = new TreeNode(3);
        TreeNode A2 = new TreeNode(9);
        TreeNode A3 = new TreeNode(20);
        TreeNode A4 = new TreeNode(15);
        TreeNode A5 = new TreeNode(7);

        A1.left = A2;
        A1.right = A3;
        A2.left = null;
        A2.right = null;
        A3.left = A4;
        A3.right = A5;
        A4.left = null;
        A4.right = null;
        A5.left = null;
        A5.right = null;

        List<List<Integer>> result = levelOrder(A1);
        System.out.println(result);
    }


    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        levelRecursion(root,result,0);
        return result;
    }

    private static void levelRecursion(TreeNode node, List<List<Integer>> result, int level){
        if (node==null){
            return;
        }
        if (result.size()<level+1){
            result.add(new ArrayList<Integer>());
        }
        result.get(level).add(node.val);
        levelRecursion(node.left, result, level+1);
        levelRecursion(node.right, result, level+1);
    }

}
