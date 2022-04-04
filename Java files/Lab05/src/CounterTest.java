public class CounterTest {
    public static void main(String args[]){
        Counter jack = new Counter();
        jack.click(); //value=1
        System.out.println("value is: "+jack.getValue());
        jack.click(); //value=2
        System.out.println("value is: "+jack.getValue());
        jack.click(); //value=3
        System.out.println("value is: "+jack.getValue());
        jack.reset(); //value=0
        System.out.println("value is: "+jack.getValue());

        //optional
        int result = jack.getValue();
        System.out.println("Expected result: 0");
        System.out.println("Computer result: "+jack.getValue());
    }
}