public class Bug {
    private int position = 0;
    private Boolean goingLeft = false;

    public Bug(int initialPosition) {
        this.position = initialPosition;
    }
    public void turn() {
        this.goingLeft = !goingLeft;
    }
    public void move() {
        if (goingLeft) {
            this.position--;
        } else {
            this.position++;
        }
    }
    public int getPosition() {
        return this.position;
    }
}
