import javax.swing.JComponent;
import java.awt.Graphics; 
import java.awt.Color;
import java.awt.Polygon;

public class Amogus extends JComponent {
  int width, height; 
  public Amogus(int width, int height) {
    this.width = width;
    this.height = height; 
  }
  public void paintComponent(Graphics g) {
    // default color is Color.BLACK  
    g.setColor(Color.WHITE); 
    g.fillRect(  0,   0, 500, 500); // background
    g.setColor(Color.BLACK);           // BLACK
    g.fillOval(315, 190, 95, 170); // back oval outline
    g.setColor(new Color(195, 17, 17)); // RED
    g.fillOval(325, 200, 75, 150); // back oval
    g.setColor(Color.BLACK);           // BLACK
    g.fillRect(140, 190, 220, 140); // mid rect outline
    g.fillOval(140, 275, 220, 95); // bottom oval outline
    g.fillOval(140, 90, 220, 220); // top oval outline
    g.fillRect(260, 260, 100, 190); // right rect outline
    g.fillRect(140, 260, 100, 190); // left rect outline
    g.fillOval(140, 415, 100, 60); // left oval outline
    g.fillOval(260, 415, 100, 60); // right oval outline
    g.setColor(new Color(195, 17, 17)); // RED
    g.fillOval(150, 285, 200, 75); // bottom oval
    g.fillRect(150, 200, 200, 125); // mid rect
    g.fillOval(150, 100, 200, 200); // top oval
    g.fillRect(150, 270, 80, 175); // left rect
    g.fillOval(150, 425, 80, 40); // left oval
    g.fillRect(270, 270, 80, 175); // right rect
    g.fillOval(270, 425, 80, 40); // right oval
    g.setColor(Color.BLACK);          // BLACK
    g.fillOval(120, 160, 190, 110); // face oval outline
    g.setColor(new Color(153, 204, 204)); // BLUE
    g.fillOval(130, 170, 170, 90); // face oval
    g.setColor(Color.WHITE);          //WHITE  
    g.fillOval(160, 190, 60, 20);
  }
}