import java.util.ArrayList;

public class PhoneBook extends ArrayList<Phone> {

    @Override
    public String toString() {
        StringBuilder directory = new StringBuilder();
        for (Phone phone : this) {
            directory.append("{'name': "+ phone.getName() + ", 'phoneNumber': " + phone.getNumber() + "}\n");
        }
        return directory.toString();
    }

    public int size(PhoneBook phoneBook) {
        return phoneBook.size();
    }
    /**
     * Inserts an entry in this phone book.
     * @param name The name for the entry.
     * @param phoneNumber The phone number for the entry.
     */
    public void insert(ArrayList<Phone> currBook, String name, String phoneNumber){
        Phone newPhone = new Phone();
        newPhone.setName(name);
        newPhone.setNumber(phoneNumber);
        currBook.add(newPhone);
    }

    /**
     * Returns the phone number associated with a name in the phone book.
     * @param name The name to search for.
     * @return The phone number for the entry, or -1 if the name is not present in the phone book.
     */
    public long find(ArrayList<Phone> currBook, String name) {
        for (Phone phone : currBook) {
            if (phone.getName() == name)
                return phone.getNumber();
        }
        return -1;
    }



    public static void main(String[] args) {
        Phone abc = new Phone();
        abc.setName("ABC");
        abc.setNumber("1111111111");

        Phone xyz = new Phone();
        xyz.setName("XYZ");
        xyz.setNumber("9999999999");

        Phone def = new Phone();
        def.setName("DEF");
        def.setNumber("2222222222");


        PhoneBook phoneBook = new PhoneBook();
        phoneBook.add(abc);
        phoneBook.add(xyz);
        phoneBook.add(def);
        System.out.println(phoneBook);

        System.out.println("After inserting CDE...");
        phoneBook.insert(phoneBook,"CDE", "1223123213");
        System.out.println(phoneBook);

        System.out.println("The size of this phone book is: " + phoneBook.size(phoneBook));

        System.out.println("Find the phone number for ABC...");
        System.out.println(phoneBook.find(phoneBook, "ABC"));

    }
}

