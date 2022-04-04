public class Student {
    private String name;
    private int quizScore;
    private int quizNumber;

    public Student(String studentName){
        this.name=studentName;
        this.quizScore=0;
        this.quizNumber=0;
    }

    public String getName(){
        return this.name;
    }

    public void addQuiz(int score){
        this.quizScore=this.quizScore+score;
        this.quizNumber++; //this.quizNumber=this.quizNumber+1;
    }

    public int getTotalScore(){
        return this.quizScore;
    }

    public int getAverageScore(){
        return (this.quizScore/this.quizNumber);
    }
}