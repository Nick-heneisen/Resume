import javax.swing.*;
import java.awt.*;

public class P24{
    public static void main(String[] args){
        JFrame a = new JFrame();
        a.add(new Two());
        a.setSize(600,600);
        a.setVisible(true);
    }
}

class Two extends JComponent{
    public void paintComponent(Graphics g){
        Graphics2D g2 = (Graphics2D) g;
        float thickness = 6;
        Stroke oldStroke = g2.getStroke();
        g2.setStroke(new BasicStroke(thickness));

        Rectangle a = new Rectangle(100, 100, 200, 50);
        g2.setColor(Color.BLUE);
        g2.draw(a);
        Rectangle b = new Rectangle(150, 130, 100, 250);
        g2.setColor(Color.RED);
        g2.draw(b);
        Rectangle ab = a.intersection(b);
        g2.setColor(Color.GREEN);
        g2.draw(ab);
        Rectangle c = new Rectangle(400, 400, 50, 50);
        Rectangle ac = a.intersection(c);
        g2.setStroke(oldStroke);
    }
}