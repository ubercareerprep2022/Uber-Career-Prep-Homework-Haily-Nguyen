import java.util.ArrayList;

public class BSTPhoneBook extends ArrayList<Phone> {
    private Node root;

    public static class Node {
        public String name;
        public long number;
        public Node left;
        public Node right;
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

        public String toString() {
            String res = "{'name': " + name + ", 'phoneNumber': " + number + "}\n";
            if (hasLeft()) res += left.toString();
            if (hasRight()) res += right.toString();
            return res;
        }
    }



    public int size(Node root) {
        if (root == null)
            return 0;
        else
            return(size(root.left) + 1 + size(root.right));
    }

    public void insert(String name, long number) {
        root = insertKey(root, name, number);
    }

    public Node insertKey(Node root, String name, long number) {
        // Return a new node if the tree is empty
        if (root == null) {
            root = new Node();
            root.number = number;
            root.name = name;
            return root;
        }

        // Traverse to the right place and insert the node
        if (root.name.compareTo(name) > 0)
            root.left = insertKey(root.left, name, number);
        else if (root.name.compareTo(name) < 0)
            root.right = insertKey(root.right, name, number);
        return root;
    }

    /**
     * Returns the phone number associated with a name in the phone book.
     * @param name The name to search for.
     * @return The phone number for the entry, or -1 if the name is not present in the phone book.
     */
    public long find(Node root, String name) {
        if (root==null || root.name==name) {
            return root.number;
        }
        else if (root.name.compareTo(name) < 0) {
            find(root.right, name);
        }
        else
            find(root.left, name);

        return -1;
    }

    public static void main(String[] args) {
        BSTPhoneBook phoneBook = new BSTPhoneBook();
        phoneBook.insert("ABC", Long.parseLong("1111111111"));
        phoneBook.insert("XYZ", Long.parseLong("9999999999"));
        phoneBook.insert("DEF", Long.parseLong("2222222222"));

        System.out.println(phoneBook.root);

        System.out.println("The size of this phone book is: " + phoneBook.size(phoneBook.root));

        System.out.println("Find the phone number for ABC...");
        System.out.println(phoneBook.find(phoneBook.root, "ABC"));

    }

}
