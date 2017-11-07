package op.ex.common;

import java.util.*;

/**
 * Created by huash on 2015/7/28.
 */

class TreeNode{
    int value;
    TreeNode left;
    TreeNode right;

    public TreeNode(int value, TreeNode left, TreeNode right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public TreeNode(int value) {
        this.value = value;
    }

    public TreeNode() {
    }
}

class Query{
    int u;
    int v;

    public Query(int u, int v) {
        this.u = u;
        this.v = v;
    }
}
public class LCA_Tarjan {

    public static TreeNode makeTreeFromArray(List<Integer> list){
        if (list == null || list.size() <= 0){
            return null;
        }
        int i = list.size() / 2;
        TreeNode root = new TreeNode(list.get(i));
        root.left = makeTreeFromArray(list.subList(0, i));
        root.right = makeTreeFromArray(list.subList(i+1, list.size()));
        return root;
    }

    static Map<Query, Integer> response = new HashMap<>();
    public static void dfs(TreeNode root, Map<Integer, List<Integer>> queries){
        if (root == null){
            return;
        }
        int u = root.value;
        if (root.left != null){
            dfs(root.left, queries);
            union(u, root.left.value);
            ancestor[find(u)] = u;
        }
        if (root.right !=null){
            dfs(root.right, queries);
            union(u, root.right.value);
            ancestor[find(u)] = u;
        }

        visited[root.value] = true;
        List<Integer> vs = queries.get(u);
        if (vs!=null && !vs.isEmpty()){
            for (int v : vs){
                if (visited[v]){
                    response.put(new Query(u, v), u);
                }
            }
        }
    }

    static final int MAXN = 100;
    static boolean[] visited = new boolean[MAXN];
    static int[] father = new int[MAXN];
    static int[] rank = new int[MAXN];
    static int[] ancestor = new int[MAXN];
    public static void makeSet(){
        Arrays.fill(visited, false);
        Arrays.fill(rank, 0);
        response.clear();
        for (int i = 0; i < father.length; i++) {
            father[i] = i;
            ancestor[i] = i;
        }
    }
    public static int find(int x){
        if (x != father[x]){
            father[x] = find(father[x]);
        }
        return father[x];
    }
    public static void union(int x, int y){
        x = find(x);
        y = find(y);
        if (x != y){
            if (rank[x] > rank[y]){
                father[y] = x;
                rank[x] += rank[y];
            }else {
                father[x] = y;
                rank[y] += rank[x];
            }
        }

    }
    public static void outputTree(TreeNode root){
        if (root == null){
            System.out.println("[]");
            return;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        q.add(root);
        TreeNode nexLevel = null;
        while (!q.isEmpty()){
            TreeNode node = q.poll();
            if (nexLevel == node){
                nexLevel = null;
            }
            if (nexLevel == null){
                System.out.println();
                nexLevel = node.left != null ? node.left : node.right;
            }
            System.out.print(node.value+" ");
            if (node.left != null){
                q.add(node.left);
            }
            if (node.right != null){
                q.add(node.right);
            }
        }

    }

    public static void main(String[] args){
        Random rand = new Random();
        for (int i = 0; i < 10; i++) {
            int len = rand.nextInt(10) + 1;
            List<Integer> list = new ArrayList<>(len);
            for (int j = 0; j < len; j++) {
                list.add(rand.nextInt(100));
            }
            TreeNode root = makeTreeFromArray(list);
            outputTree(root);
            makeSet();
            Map<Integer, List<Integer>> queries = new HashMap<>();
            for (int j = 0; j < 5; j++) {
                int u = list.get(rand.nextInt(len));
                int v = list.get(rand.nextInt(len));
                List<Integer> vs = queries.get(u);
                if (vs == null){
                    vs = new ArrayList<>();
                    queries.put(u, vs);
                }
                vs.add(v);
            }
            dfs(root, queries);
            for (Query q : response.keySet()){
                System.out.println(String.format("LCA(%d, %d) = %d", q.u, q.v, response.get(q)));
            }
            System.out.println();
        }
    }


}
