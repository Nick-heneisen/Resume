public class Node {
    int number;
    Node left, right;
    public Node(int a) {this(a, null, null);}
    public Node(int num, Node left, Node right) {
        this.number = num;
        this.left = left;
        this.right = right;
    }
    public String toString() {
        //return "Node: " + this.number + this.left + this.right;
        String left = (this.left == null) ? "." : this.left + "",
                right = (this.right == null) ? "." : this.right + "";

        String show = "(" + this.number + " " + left + " " + right + ")";
        return show;
    }
    public static void main(String[] args) {

        Node tree = new Node(5, new Node(3, null, new Node(4)), new Node(6));
        System.out.println(tree);

        Node b = new Node(5);
        System.out.println("insert 5: " + b);
        b.insert(6);
        System.out.println("insert 6: " + b);
        b.insert(4);
        System.out.println("insert 4: " + b);
        b.insert(3);
        System.out.println("insert 3: " + b); // (5 (4 (3 . .) .) (6 . .))

    }
    public void insert(int num) {
        if (this.number == num) return;
        if (num < this.number) {
            if (this.left == null) this.left = new Node(num);
            else this.left.insert(num);
        } else {
            if (this.right == null) this.right = new Node(num);
            else this.right.insert(num);
        }
    }
}
