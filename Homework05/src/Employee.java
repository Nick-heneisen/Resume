public class Employee {
    private String name = null;
    private double salary = 0;

    public Employee(String employeeName, double employeeSalary) {
    this.name = employeeName;
    this.salary = employeeSalary;
    }
    public String getName() {
        return this.name;
    }
    public double getSalary() {
        return this.salary;
    }
    public void raiseSalary(double byPercent) {
        this.salary = this.salary  + this.salary * (byPercent / 100);
    }
}
