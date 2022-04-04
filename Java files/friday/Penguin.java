import java.awt.Graphics;

public class Penguin { //actually a circle
    int x, y, radius;
    int id;
    static int nextID = 6;
    public Penguin(int x, int y, int radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.id = Penguin.nextID++;
        System.out.println("Penguin #" + this.id + " Has been created.");
    }
    int i = 100;
    public void ward(Graphics a) {
        System.out.println("Penguin #" + this.id + " is here." + ++i);
    }
}