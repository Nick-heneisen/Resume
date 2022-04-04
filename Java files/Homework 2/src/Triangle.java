import java.awt.*;

public class Triangle {
    Point a, b, c;
    public Triangle(Point a, Point b, Point c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }
    public void draw(Graphics g) {
        (new Line(this.a, this.b)).draw(g);
        (new Line(this.b, this.c)).draw(g);
        (new Line(this.c, this.a)).draw(g);
    }
}
