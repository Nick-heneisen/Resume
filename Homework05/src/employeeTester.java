public class employeeTester {
    public static void main(String[] args) {
        Employee jim = new Employee("jimmy j.", 40000);

        System.out.println(jim.getName() + " has a salary of " + jim.getSalary());
        System.out.println("Initial salary: " + jim.getSalary());
        jim.raiseSalary(50);
        System.out.println("New salary: " + jim.getSalary());
    }
}
