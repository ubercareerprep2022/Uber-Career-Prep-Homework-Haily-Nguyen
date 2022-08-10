public class Phone {
    private String name;
    private long number;

    public long getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = Long.parseLong(number);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}

