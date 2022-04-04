import javax.swing.JComponent;
import java.awt.Graphics; 
import java.awt.Color;
import java.awt.Polygon;

public class Amogus {
  int x, y;
  double scale; 
  public Amogus(int x, int y, double scale) {
    this.x = x;
    this.y = y; 
    this.scale = scale;
  }
  private int scale(int size) {
      return (int)(this.scale * size);
  }
  public void draw(Graphics g) {
    // default color is Color.BLACK  
    g.setColor(Color.WHITE); 
    g.fillRect(x+0, y+0, scale(500), scale(500)); // background
    g.setColor(Color.BLACK);           // BLACK
    g.fillOval(x+scale(315), y+scale(190), scale(95), scale(170)); // back oval outline
    g.setColor(new Color(195, 17, 17)); // RED
    g.fillOval(x+scale(325), y+scale(200), scale(75), scale(150)); // back oval
    g.setColor(Color.BLACK);           // BLACK
    g.fillRect(x+scale(140), y+scale(190), scale(220), scale(140)); // mid rect outline
    g.fillOval(x+scale(140), y+scale(275), scale(220), scale(95)); // bottom oval outline
    g.fillOval(x+scale(140), y+scale(90), scale(220), scale(220)); // top oval outline
    g.fillRect(x+scale(260), y+scale(260), scale(100), scale(190)); // right rect outline
    g.fillRect(x+scale(140), y+scale(260), scale(100), scale(190)); // left rect outline
    g.fillOval(x+scale(140), y+scale(415), scale(100), scale(60)); // left oval outline
    g.fillOval(x+scale(260), y+scale(415), scale(100), scale(60)); // right oval outline
    g.setColor(new Color(195, 17, 17)); // RED
    g.fillOval(x+scale(150), y+scale(285), scale(200), scale(75)); // bottom oval
    g.fillRect(x+scale(150), y+scale(200), scale(200), scale(125)); // mid rect
    g.fillOval(x+scale(150), y+scale(100), scale(200), scale(200)); // top oval
    g.fillRect(x+scale(150), y+scale(270), scale(80), scale(175)); // left rect
    g.fillOval(x+scale(150), y+scale(425), scale(80), scale(40)); // left oval
    g.fillRect(x+scale(270), y+scale(270), scale(80), scale(175)); // right rect
    g.fillOval(x+scale(270), y+scale(425), scale(80), scale(40)); // right oval
    g.setColor(Color.BLACK);          // BLACK
    g.fillOval(x+scale(120), y+scale(160), scale(190), scale(110)); // face oval outline
    g.setColor(new Color(153, 204, 204)); // BLUE
    g.fillOval(x+scale(130), y+scale(170), scale(170), scale(90)); // face oval
    g.setColor(Color.WHITE);          //WHITE  
    g.fillOval(x+scale(160), y+scale(190), scale(60), scale(20));
  }
}