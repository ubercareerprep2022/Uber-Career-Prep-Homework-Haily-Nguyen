public class Tree {
    public TreeNode root;

    public Tree(TreeNode root) {
        this.root = root;
    }

    public static void main(String[] args) {
        TreeNode leftChild = new TreeNode(6, null, null);
        TreeNode rightChild = new TreeNode(3, null, null);
        TreeNode left = new TreeNode(7, null, null);
        TreeNode right = new TreeNode(17, leftChild, rightChild);
        TreeNode root = new TreeNode(1, left, right);
        /* Print the tree here */
        System.out.println(root);
    }

    public static class TreeNode {
        public int data;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int data, TreeNode left, TreeNode right) {
            this.data = data;
            this.left = left;
            this.right = right;
        }

        /**
         * Does it have a left child?
         */
        public boolean hasLeft() {
            return left != null;
        }

        /**
         * Does it have a right child?
         */
        public boolean hasRight() {
            return right != null;
        }

        /**
         * Recursively constructs a String representation of the tree from this node,
         * starting with the given indentation and indenting further going down the tree
         */
        public String toStringHelper(String indent) {
            String res = indent + data + "\n";
            if (hasLeft()) res += left.toStringHelper(indent+"  ");
            if (hasRight()) res += right.toStringHelper(indent+"  ");
            return res;
        }

        /**
         * Returns a string representation of the tree
         */
        public String toString() {
            return toStringHelper("");
        }
    }








}
