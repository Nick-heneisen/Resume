import javax.swing.JComponent;
import javax.swing.JFrame;
import java.awt.Graphics;

public class Lab03 extends JComponent{
    int width, height;
    Amogus a, b, c;
    
    public Lab03(int width, int height) {
        this.width = width;
        this.height = height;
        a = new Amogus(20, 50, 0.3);
        b = new Amogus(250, 92, 0.5);
        c = new Amogus(1, 243, 0.1);
    }
    
    public void paintComponent(Graphics g){
        a.draw(g);
        b.draw(g);
        c.draw(g);
    }
    
    public static void main(String args[]) {
        JFrame frame = new JFrame();
        frame.setVisible(true);
        int width = 500, height = 500;
        frame.setSize(width, height);
        Lab03 drawing = new Lab03(width, height);
        frame.add(drawing); 
    }
}