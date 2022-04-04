import java.awt.Graphics;

public class Line {
    Point one, two;
    public Line(Point one, Point two) {
        this.one = one;
        this.two = two;
    }
    public void draw(Graphics g) {
        g.drawLine(this.one.x, this.one.y, this.two.x, this.two.y);
        this.one.draw(g);
        this.two.draw(g);
    }
}
