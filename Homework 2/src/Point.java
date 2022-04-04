import java.awt.Graphics;

public class Point {
    int x, y;
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public void draw(Graphics g) {
        g.drawOval(this.x - 5, this.y - 5, 10, 10);
    }
}
