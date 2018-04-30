/*
The original method, but it wastes some space.
*/


import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        int rowIndex = 3;
        List result = new ArrayList();
        result = getRow(rowIndex);
        System.out.println(result);
    }

    public static List<Integer> getRow(int rowIndex) {
        List result = new ArrayList();
        int[][] pascal_tri = new int[34][34];
        // initialize all the 1
        for (int i = 0; i <= rowIndex; i++){
            pascal_tri[i][0] = 1;
            pascal_tri[i][i] = 1;
        }
        for (int i = 2; i<= rowIndex; i++){
            for (int j = 1; j<= i; j++){
                pascal_tri[i][j] = pascal_tri[i - 1][j - 1] + pascal_tri[i - 1][j];
            }
        }
        for (int j = 0; j<= rowIndex; j++)
            result.add(pascal_tri[rowIndex][j]);
        return result;

    }

}


/*
The second solution, and it uses only O(k) extra space
*/
public ArrayList<Integer> getRow(int rowIndex) {
    ArrayList<Integer> res = new ArrayList<Integer>();
    if(rowIndex<0)
        return res;
    res.add(1);
    for(int i=1;i<=rowIndex;i++)
    {
        for(int j=res.size()-2;j>=0;j--)
        {
            res.set(j+1,res.get(j)+res.get(j+1));
        }
        res.add(1);
    }
    return res;
}

