import java.io.*;
import java.util.ArrayList;

/* Why is there a difference in the running times for the two implementations?
As for insertion, List is faster as its time complexity is O(1) while Binary Search Tree
 has a time complexity of O(nlog(n))
As for search, List is slower as its time complexity is O(n) while Binary Search Tree
 has a time complexity of O(log(n))
 n is the number of contacts existed.
 */

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

    public int compare(String a, String b) {
        if(a.charAt(0) > b.charAt(0)){
            return 1;
        } else if (a.charAt(0) < b.charAt(0)){
            return -1;
        } else {
            return 1;
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
        if (root == null)
            return -1;

        if (root.name==name) {
            return root.number;
        }
        else if (root.name.compareTo(name) < 0) {
            return find(root.right, name);
        }
        else
            return find(root.left, name);
    }

    public static void main(String[] args) throws IOException {
        BSTPhoneBook phoneBook = new BSTPhoneBook();
        BufferedReader csvReader = new BufferedReader(new FileReader("Assignment-2.1/data.csv"));
        String row;
        while ((row = csvReader.readLine()) != null) {
            String[] data = row.split(",");
            String name = data[0];
            String number = data[1];
            phoneBook.insert(name, Long.parseLong(number));
        }
        csvReader.close();

        phoneBook.insert("ABC", Long.parseLong("1111111111"));
        phoneBook.insert("XYZ", Long.parseLong("9999999999"));
        phoneBook.insert("DEF", Long.parseLong("2222222222"));

        System.out.println(phoneBook.root);

        System.out.println("The size of this phone book is: " + phoneBook.size(phoneBook.root));

        System.out.println("Find the phone number for ABC...");
        System.out.println(phoneBook.find(phoneBook.root, "ABC"));
        System.out.println(phoneBook.find(phoneBook.root, "XYZ"));

        String fileName = "Assignment-2.1/search.txt";
        File file = new File(fileName);
        FileReader fr = new FileReader(file);
        BufferedReader br = new BufferedReader(fr);
        String line;
        while((line = br.readLine()) != null){
            // process the line
            System.out.println(line);
            System.out.println(phoneBook.find(phoneBook.root, line));
        }
    }

}
