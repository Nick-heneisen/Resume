public interface LispList {
    Object head();
    LispList tail();
    boolean empty();
    static LispList NIL = new EmptyList();
    LispList cons(Object obj);
    int length();
    LispList merge(LispList other);
    boolean contains(Object obj);
}
