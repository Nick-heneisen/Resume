import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.util.ArrayList;
import javax.swing.JComponent;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseListener;

public class Sequence extends JComponent implements MouseMotionListener, MouseListener {
    public void mouseDragged(MouseEvent e) {
        int x = e.getX(), y = e.getY();
        System.out.println("(" + x + "," + y + ")");
        if (current == null) {

        } else {
            current.moveTo(x, y);
            this.repaint();
        }
        Circle first = this.circles.get(0);
        first.moveTo(x, y);
        this.repaint();
    }
    public void mouseMoved(MouseEvent e) { }
    public void mouseEntered(MouseEvent e) { }
    public void mouseExited(MouseEvent e) { }
    public void mouseClicked(MouseEvent e) { }
    Circle current;
    public void mousePressed(MouseEvent e) {
        int x = e.getX(), y = e.getY();
        for (Circle c : this.circles) {
            if (c.contains(x, y)) {
                this.current = c;
                break;
            }
        }
    }
    public void mouseReleased(MouseEvent e) {
        this.current = null;
    }

    private ArrayList<Integer> values;
    ArrayList<Circle> circles = new ArrayList<Circle>();
    public Sequence() {
        this.values = new ArrayList<Integer>();
        this.addMouseMotionListener(this);
        this.addMouseListener(this);
    }
    public Sequence(int[] values){
        this(); // ha, ha!
        for (int v : values) {
            this.values.add( v);
            this.circles.add(new Circle(v, (int)(Math.random() * 400 + 50),
                                            (int)(Math.random() * 400 + 50)));
        }
    }
    public void add(int n) {
        this.values.add(n);
    }
    public Integer get(int n) {
        return this.values.get(n);
    }
    public int length() { return this.values.size(); }
    public String toString() {
        return this.values.toString();
    }
    public void paintComponent(Graphics g) {
        // g.drawString(this + "", 80, 120);
        for (int index = 0; index < this.values.size()-1; index += 1) {
            Circle a = this.circles.get(index),
                   b = this.circles.get(index + 1);
            g.drawLine(a.x+a.radius, a.y+a.radius, b.x+b.radius, b.y+b.radius);
            this.circles.get(index).draw(g);
        }
        this.circles.get(this.values.size()-1).draw(g);
    }
    public static void main(String[] args) {
        Sequence m = new Sequence( new int[] { 1, 2, 3, 4, 5, 6 } );
        JFrame f = new JFrame("Homework 3");
        f.add(m);
        System.out.println(m);
        f.setVisible(true);
        f.setSize(500, 500);
    }
}
