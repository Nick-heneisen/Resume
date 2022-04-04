import java.awt.*;

public class Circle {
    int value;
    int x, y;
    int radius = 16;
    public Circle(int v, int x, int y) {
        this.value = v;
        this.x = x;
        this.y = y;
    }
    public void draw(Graphics g) {
        int xc = this.x + this.radius, yc = this.y + this.radius;
        g.setColor(Color.WHITE);
        g.fillOval(this.x, this.y, 2 * this.radius, 2 * this.radius);
        g.setColor(Color.BLACK);
        g.drawString(this.value + "", xc-2, yc+2);
        g.drawOval(this.x, this.y, 2 * this.radius, 2 * this.radius);
    }
    public void moveTo(int x, int y) {
        this.x = x - radius;
        this.y = y - radius;
    }
    public boolean contains(int x, int y) {
        int xc = this.x + this.radius, yc = this.y + this.radius;
        int dx = xc - x, dy = yc - y;
        return Math.sqrt(dx*dx + dy*dy) <= this.radius;
    }
}
