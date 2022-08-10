public class BinarySearchTree {
    private Node root;

    /**
     * Inserts a key into this binary search tree.
     * If there are n nodes in the tree, then the average runtime of this method should be log(n).
     *
     * @param key The key to insert.
     * @return
     */
    public void insert(int key) {
        root = insertKey(root, key);
    }

    public Node insertKey(Node root, int key) {
        // Return a new node if the tree is empty
        if (root == null) {
            root = new Node();
            root.key = key;
            return root;
        }

        // Traverse to the right place and insert the node
        if (key < root.key)
            root.left = insertKey(root.left, key);
        else if (key > root.key)
            root.right = insertKey(root.right, key);
        return root;
    }

    /**
     * Checks whether or not a key exists in this binary search tree.
     * If there are n nodes in the tree, then the average runtime of this method should be log(n).
     *
     * @param key The key to check for.
     * @return true if the key is present in this binary search tree, false otherwise.
     */
    public boolean findKey(Node root, int key) {
        // Please implement this method.
        // Base Cases: Root is null or key is the root itself already
        if (root==null) {
            return false;
        } else if (root.key == key)
            return true;
        // Key is greater than root's key
        else if (root.key < key)
            findKey(root.right, key);

        // Key is smaller than root's key
        findKey(root.left, key);
        return false;
    }

    public void inorder() {
        inorderRec(root);
    }

    /**
     * Prints the binary search tree in inorder traversal.
     *
     * @param root The root of the tree traversing.
     */
    public void inorderRec(Node root) {
        if (root != null) {
            inorderRec(root.left);
            System.out.print(root.key + " -> ");
            inorderRec(root.right);
        }
    }


    public static class Node {
        public int key;
        public Node left;
        public Node right;
    }

    // Driver Program to test above functions
    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.root = new Node();
        tree.root.key = 5;
        tree.insert(0);
        tree.insert(3);
        tree.insert(2);
        tree.insert(6);
        tree.insert(9);
        tree.insert(10);
        tree.insert(16);
        tree.insert(4);

        System.out.print("Inorder traversal: ");
        tree.inorder();
        System.out.println();
        System.out.println("Is 5 in this BST?");
        System.out.println(tree.findKey(tree.root, 5));
        System.out.println("Is 4 in this BST?");
        System.out.println(tree.findKey(tree.root, 4));
        System.out.println("Is 15 in this BST?");
        System.out.println(tree.findKey(tree.root, 15));
    }
}



