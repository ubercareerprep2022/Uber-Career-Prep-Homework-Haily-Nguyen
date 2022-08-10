import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;


public class Organization {

    public static void main(String[] args) {
        Employee ceo = new Employee("A", "CEO");
        Employee cfo = new Employee("B", "CFO");
        Employee cto = new Employee("C", "CTO");
        Employee director = new Employee("I", "Director");
        Employee manager1 = new Employee("D", "Manager");
        Employee manager2 = new Employee("E", "Manager");
        Employee sale1 = new Employee("J", "Sales Rep");
        Employee sale2 = new Employee("K", "Sales Intern");
        Employee engineer1 = new Employee("G", "Engineer");
        Employee engineer2 = new Employee("H", "Engineer");
        Employee engineer3 = new Employee("F", "Engineer");

        ceo.directReports = new ArrayList<Employee>(Arrays.asList(cto, cfo));
        cto.directReports = new ArrayList<Employee>(Arrays.asList(director));
        cfo.directReports = new ArrayList<Employee>(Arrays.asList(manager1, manager2));
        director.directReports = new ArrayList<Employee>(Arrays.asList(sale1));
        manager1.directReports = new ArrayList<Employee>(Arrays.asList(engineer1, engineer2, engineer3));
        sale1.directReports = new ArrayList<Employee>(Arrays.asList(sale2));
        manager2.directReports = sale2.directReports = engineer1.directReports = engineer2.directReports
                = engineer3.directReports = new ArrayList<>();
        levelOrder(ceo);
        System.out.println(ceo.printNumLevels(ceo));
    }

    public static class Employee {
        public String name;
        public String title;
        public ArrayList<Employee> directReports;

        public Employee(String name, String title) {
            this.name = name;
            this.title = title;
        }

        public int printNumLevels(Employee ceo) {
            if (ceo.directReports.size() == 0) return 1;
            int level = 0;
            /* Recursively update the level until reaching the last level
            with no direct reports */
            for (Employee employee : ceo.directReports) {
                int subLevel = printNumLevels(employee);
                if (subLevel > level)
                    level = subLevel;
            }
            return level + 1;    // count the ceo as well
        }
    }



    /**
     * Print by level using two queues.
     */
    public static void levelOrder(Employee ceo) {
        if (ceo == null)
            return;

        Queue<Employee> structure = new LinkedList<>();
        // Push root to the queue
        structure.add(ceo);
        System.out.print("Name: " + ceo.name + ", Title: " + ceo.title + "\n\n");

        // Push delimiter into the queue to make sure each level is separated.
        structure.add(null);

        // Loop until queue is empty
        while (!structure.isEmpty()) {
            Employee curr = structure.poll();

            // Check if the current employee has direct reports
            if (curr == null) {
                if (!structure.isEmpty()) {
                    structure.add(null);
                    System.out.println();
                }
            } else {
                if (curr.directReports != null)
                    for (Employee employee : curr.directReports) {
                        structure.add(employee);
                        System.out.print("Name: " + employee.name + ", Title: " + employee.title + "\n");
                    }
            }
        }
    }
}