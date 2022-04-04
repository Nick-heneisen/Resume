import java.util.Random;
public class E622{
    public static void main(String[] args){
        Random Number = new Random();
        int trials = 1000;

        System.out.println("Scenerio 1: Player does not change his door");
        int numofwins = 0;
        for (int i = 1; i < trials; i++) { //starts at trial 1
            int cardoor = Number.nextInt(3);
            int playerdoor = Number.nextInt(3);
            if (playerdoor == cardoor) // if the player chooses the car door he wins
                numofwins++;
        }
        System.out.println("Number of trials: " + trials + " and won: " + numofwins);

        System.out.println("Scenerio 2: Player changes the door");
        numofwins = 0;
        for (int i = 1; i < trials; i++){ //starts at trial 1
            int cardoor = Number.nextInt(3);
            int playerdoor = Number.nextInt(3);
            int notpicked = cardoor; // I set the scenerio if the door that wasn't pick was the carprize.
            while (notpicked == cardoor || notpicked == playerdoor){ // while the not picked door equals cardoor or the lastdoor equals the contestant door
                notpicked = Number.nextInt(3); //it will always run when this is true so we know that notpicked door (will not equal to the cardoor and that its not picked)
            }
            int otherdoor = 3 - (playerdoor + notpicked); // this will get the remaining door not the player could chose
            if (otherdoor == cardoor)
                numofwins++;
        }
        System.out.println("number of trials: " + trials + " and won: " + numofwins);
    }
}