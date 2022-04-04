import javax.swing.*;
import java.awt.*;

public class Shapes extends JComponent {
    public static void main(String[] args) {
        JFrame a = new JFrame();
        a.setVisible(true);
        a.setSize(500, 500);
        a.add(new Shapes());
    }
    Point a;
    Line l1, l2;
    Triangle t;
    public Shapes() {
        this.a = new Point(140, 110);
        Point a = new Point(40, 280), b = new Point(180, 220);
        this.l1 = new Line(a, b);
        Point c = new Point(40, 280), d = new Point(280, 170);
        this.l2 = new Line(c, d);
        Point f = new Point(40, 280), g = new Point(120, 370);
        this.t = new Triangle(f, g, new Point(300, 195));
    }
    public void paintComponent(Graphics g) {
        this.a.draw(g);
        this.l1.draw(g);
        this.l2.draw(g);
        this.t.draw(g);
    }
}
