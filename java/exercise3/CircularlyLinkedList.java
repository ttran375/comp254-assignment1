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
        CircularlyLinkedList<E> other = new CircularlyLinkedList<>();
        if (size == 0) {
            return other;
        }

        Node<E> walk = tail.getNext();
        for (int i = 0; i < size; i++) {
            other.addLast(walk.getElement());
            walk = walk.getNext();
        }
        return other;
    }

    public boolean areEqual(CircularlyLinkedList<E> other) {
        if (this.size != other.size)
            return false;
        if (this.isEmpty() && other.isEmpty())
            return true;
        if (this.isEmpty() || other.isEmpty())
            return false;

        Node<E> node1 = this.tail.getNext();
        Node<E> node2 = other.tail.getNext();

        for (int i = 0; i < this.size; i++) {
            if (node1.getElement().equals(node2.getElement())) {
                Node<E> temp1 = node1;
                Node<E> temp2 = node2;
                boolean match = true;
                for (int j = 0; j < this.size; j++) {
                    if (!temp1.getElement().equals(temp2.getElement())) {
                        match = false;
                        break;
                    }
                    temp1 = temp1.getNext();
                    temp2 = temp2.getNext();
                }
                if (match)
                    return true;
            }
            node1 = node1.getNext();
        }
        return false;
    }

    public static void main(String[] args) {
        CircularlyLinkedList<String> circularList = new CircularlyLinkedList<String>();
        circularList.addFirst("LAX");
        circularList.addLast("MSP");
        circularList.addLast("ATL");
        circularList.addLast("BOS");
        System.out.println("Original: " + circularList);

        CircularlyLinkedList<String> clonedList = circularList.clone();
        System.out.println("Cloned: " + clonedList);

        CircularlyLinkedList<String> L1 = new CircularlyLinkedList<>();
        L1.addLast("A");
        L1.addLast("B");
        L1.addLast("C");

        CircularlyLinkedList<String> L2 = new CircularlyLinkedList<>();
        L2.addLast("B");
        L2.addLast("C");
        L2.addLast("A");

        CircularlyLinkedList<String> L3 = new CircularlyLinkedList<>();
        L3.addLast("C");
        L3.addLast("B");
        L3.addLast("A");

        System.out.println("L1 and L2 are equal: " + L1.areEqual(L2)); // Should print true
        System.out.println("L1 and L3 are equal: " + L1.areEqual(L3)); // Should print false
    }
}
