public class Grade {
    private double gpa = 0;
    public static void main(String[] args) {
        Grade nick = new Grade(Math.random() * 4);
        System.out.println("Your GPA:" + nick.getNumericGrade());
        System.out.println("Your letter grade: " + nick.pickGrade());
    }
    public Grade(double studentGpa) {
        gpa = studentGpa;
    }
    public double getNumericGrade() {
        return gpa;
    }

    public String pickGrade() {
        String grade = null;
        if (gpa >= 3.7) {
            grade = "A+";
        } else if (gpa >= 3.3 && gpa < 3.7) {
            grade = "A-";
        } else if (gpa >= 3.0 && gpa < 3.3) {
            grade = "B+";
        } else if (gpa >= 2.7 && gpa < 3.0) {
            grade = "B";
        } else if (gpa >= 2.3 && gpa < 2.7) {
            grade = "B-";
        } else if (gpa >= 2.0 && gpa < 2.3) {
            grade = "C+";
        } else if (gpa >= 1.7 && gpa < 2.0) {
            grade = "C";
        } else if (gpa >= 1.3 && gpa < 1.7) {
            grade = "C-";
        } else if (gpa >= 1.0 && gpa < 1.3) {
            grade = "D+";
        } else if (gpa < 1.0) {
            grade = "F";
        }
        return grade;
    }
}
