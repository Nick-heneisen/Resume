public class EmptyList implements LispList {

    public Object head() throws UnsupportedOperationException {
        return null;
    }

    public LispList tail() throws UnsupportedOperationException {
        return null;
    }

    public boolean empty() {
        return true;
    }

    public LispList cons(Object obj) {
        return new NonEmptyList(obj, new EmptyList());
    }

    public int length() {
        return 0;
    }

    public String toString() {
        return "";
    }

    public LispList merge(LispList other) {
        return other;
    }

    public boolean contains(Object obj) {
        return false;
    }
}
