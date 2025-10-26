import java.util.*;

public class task_tree {
    static class Node {
        int key;
        Node left, right;
        Node(int k) { key = k; }
    }

    static Node insert(Node root, int key) {
        if (root == null) return new Node(key);
        if (key < root.key) root.left = insert(root.left, key);
        else if (key > root.key) root.right = insert(root.right, key);
        return root;
    }

    static Node minValue(Node node) {
        Node cur = node;
        while (cur.left != null) cur = cur.left;
        return cur;
    }

    static Node del(Node root, int key) {
        if (root == null) return root;
        if (key < root.key) root.left = del(root.left, key);
        else if (key > root.key) root.right = del(root.right, key);
        else {
            if (root.left == null) return root.right;
            else if (root.right == null) return root.left;
            Node temp = minValue(root.right);
            root.key = temp.key;
            root.right = del(root.right, temp.key);
        }
        return root;
    }

    static void inorder(Node root) {
        if (root != null) {
            inorder(root.left);
            System.out.print(root.key + " ");
            inorder(root.right);
        }
    }

    static Node search(Node root, int key) {
        if (root == null || root.key == key) return root;
        if (key < root.key) return search(root.left, key);
        else return search(root.right, key);
    }

    public static void main(String[] args) {
        Node root = null;
        int[] a = {8,3,10,1,6,14,4,7,13};
        for (int x : a) root = insert(root, x);
        System.out.print("Обход: ");
        inorder(root);
        System.out.println();
        root = del(root, 3);
        System.out.print("После удаления 3: ");
        inorder(root);
        System.out.println();
        int f = 7;
        System.out.println("Поиск " + f + ": " + (search(root, f) != null ? "найден" : "нет"));
    }
}
