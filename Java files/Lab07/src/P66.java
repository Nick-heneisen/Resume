import java.util.Random;
import java.util.Scanner;

public class P66 {
    Random r = new Random();
    int pile = r.nextInt(101);

    public static void main(String[] args) {
        Boolean gaming = true;
        Boolean gameOver = false;
        int turn = 0;


        Boolean smart = false;
        if (Math.random() >= 0.5) {
            smart = !smart;
        } // determines smart or not

        Boolean pTurn = false;
        if (Math.random() >= 0.5) {
            pTurn = !pTurn;
        } // determines if the player goes first

        P66 game = new P66();
        Scanner input = new Scanner(System.in);

        if (game.pile < 10) {
            game.pile += 10 - game.pile;
        }
        while (gaming) {
            if (gameOver) {
                if (pTurn) {
                    System.out.println("Game over. You win!!");
                    gaming = false;
                } else {
                    System.out.println("Game over. You lose!");
                    gaming = false;
                }
            }
            if (turn == 0 && gaming) {
                if (smart) {
                    System.out.println("The computer is smart.");
                } else {
                    System.out.println("The computer is stupid.");
                }
                if (pTurn) {
                    System.out.println("You go first.");
                } else {
                    System.out.println("The computer goes first.");
                }
                turn++;
            } else if (pTurn && gaming) {
                System.out.println("There are " + game.pile + " marbles left.");
                System.out.println("How many marbles will you take?");
                int marbles = input.nextInt();
                if ((marbles <= game.pile / 2 || game.pile == 1) && marbles > 0) {
                    game.pile -= marbles;
                    if (game.pile == 0) {
                        gameOver = true;
                    }
                    pTurn = !pTurn;
                } else {
                    System.out.println("Invalid number (more than half / 0 or less.)");
                }
            } else if (gaming) {
                System.out.println("There are " + game.pile + " marbles left.");
                int cpuTaken = game.getMove(smart);
                game.pile -= cpuTaken;
                System.out.println("The computer took " + cpuTaken + " marbles.");
                if (game.pile == 0) {
                    gameOver = true;
                }
                pTurn = !pTurn;
            }
        }
    }

    public int getMove(Boolean smart) {
        if (smart) {
            if (pile > 63) {
                return pile - 63;
            } else if (pile > 31) {
                return pile - 31;
            } else if (pile > 15) {
                return pile - 15;
            } else if (pile > 7) {
                return pile - 7;
            } else if (pile > 3) {
                return pile - 3;
            } else if (pile == 63) {
                return r.nextInt(pile / 2);
            } else if (pile == 31) {
                return r.nextInt(pile / 2);
            } else if (pile == 15) {
                return r.nextInt(pile / 2);
            } else if (pile == 7) {
                return r.nextInt(pile / 2);
            } else {
                return 1;
            }
        } else {
            if (pile < 3) {
                return 1;
            } else {
                int num = r.nextInt(pile / 2);
                if (num != 0) {
                    return num;
                } else {
                    num++;
                    return num;
                }
            }
        }
    }
}