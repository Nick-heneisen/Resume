public class StudentTester {
    public static void main(String args[]){
        Student shane = new Student("Shane");
        shane.addQuiz(101);
        shane.addQuiz(6);
        shane.addQuiz(70);
        shane.addQuiz(50);
        shane.addQuiz(99);

        System.out.println("student name: "+shane.getName()); //expect: Shane
        System.out.println("total score: "+shane.getTotalScore()); //expect: 326
        System.out.println("average score: "+shane.getAverageScore()); //expect: 65
    }
}