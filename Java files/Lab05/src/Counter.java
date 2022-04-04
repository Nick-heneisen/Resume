public class Counter {
    private int value;

    public void click(){
        value=value+1;
    }

    public int getValue(){
        return value;
    }

    public void reset(){
        value=0;
    }
}