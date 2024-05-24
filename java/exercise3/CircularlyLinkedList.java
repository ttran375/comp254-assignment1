package exercise3;

public class CircularlyLinkedList<E> {

    private static class Node<E> {
        private E element;
        private Node<E> next;

        public Node(E e, Node<E> n) {
            element = e;
            next = n;
        }

        public E getElement() {
            return element;
        }

        public Node<E> getNext() {
            return next;
        }

        public void setNext(Node<E> n) {
            next = n;
        }
    }

    private Node<E> tail = null;
    private int size = 0;

    public CircularlyLinkedList() {
    }

    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public E first() {
        if (isEmpty())
            return null;
        return tail.getNext().getElement();
    }

    public E last() {
        if (isEmpty())
            return null;
        return tail.getElement();
    }

    public void rotate() {
        if (tail != null)
            tail = tail.getNext();
    }

    public void addFirst(E e) {
        if (size == 0) {
            tail = new Node<>(e, null);
            tail.setNext(tail);
        } else {
            Node<E> newest = new Node<>(e, tail.getNext());
            tail.setNext(newest);
        }
        size++;
    }

    public void addLast(E e) {
        addFirst(e);
        tail = tail.getNext();
    }

    public E removeFirst() {
        if (isEmpty())
            return null;
        Node<E> head = tail.getNext();
        if (head == tail)
            tail = null;
        else
            tail.setNext(head.getNext());
        size--;
        return head.getElement();
    }

    public String toString() {
        if (tail == null)
            return "()";
        StringBuilder sb = new StringBuilder("(");
        Node<E> walk = tail;
        do {
            walk = walk.getNext();
            sb.append(walk.getElement());
            if (walk != tail)
                sb.append(", ");
        } while (walk != tail);
        sb.append(")");
        return sb.toString();
    }

    public CircularlyLinkedList<E> clone() {
        CircularlyLinkedList<E> cloneList = new CircularlyLinkedList<>();
        if (!isEmpty()) {
            Node<E> current = tail.getNext();
            cloneList.addLast(current.getElement());
            current = current.getNext();
            while (current != tail.getNext()) {
                cloneList.addLast(current.getElement());
                current = current.getNext();
            }
        }
        return cloneList;
    }

    public static void main(String[] args) {
        CircularlyLinkedList<String> originalList = new CircularlyLinkedList<>();
        originalList.addLast("MSP");
        originalList.addLast("ATL");
        originalList.addLast("BOS");
        System.out.println("Original: " + originalList);

        CircularlyLinkedList<String> clonedList = originalList.clone();
        System.out.println("Cloned: " + clonedList);

        originalList.addLast("ABC");
        System.out.println("Original after adding ABC: " + originalList);

        clonedList.addLast("XYZ");
        System.out.println("Cloned after adding XYZ: " + clonedList);
    }

    private void concatenate(CircularlyLinkedList<String> circularlyList2) {
        Node head = tail.getNext();
        tail.setNext((Node<E>) circularlyList2.tail.getNext());
        circularlyList2.tail.setNext(head);
        tail = (Node<E>) circularlyList2.tail;
    }
}
