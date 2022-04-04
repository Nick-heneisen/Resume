public class NonEmptyList implements LispList{
    Object head = head();
    LispList tail = tail();

    public NonEmptyList(Object obj, LispList tail) {
    this.head = obj;
    this.tail = tail;

    }

    public Object head() {
        return head;
    }

    public LispList tail() {
        return tail;
    }

    public boolean empty() {
        return true;
    }

    public LispList cons(Object obj) {
        return new NonEmptyList(obj, new NonEmptyList(head(), tail));
    }

    public int length() {
        return 1 + tail.length();
    }

    public String toString() {
        return head() + " " + tail().toString();
    }

    public LispList merge(LispList other) {
        if (other.empty()) {
            return this;
        }
        return new NonEmptyList(other.head(), other.tail().merge(this));
    }

    public boolean contains(Object obj) {
        if (obj == head()) {
            return true;
        } else {
            return tail.contains(obj);
        }
    }
}
