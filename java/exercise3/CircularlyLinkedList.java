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
        if (!this.isEmpty()) {
            Node<E> current = this.tail.getNext();
            cloneList.addLast(current.getElement());
            current = current.getNext();
            while (current != this.tail.getNext()) {
                cloneList.addLast(current.getElement());
                current = current.getNext();
            }
        }
        return cloneList;
    }

    public boolean sameSequence(CircularlyLinkedList<E> other) {
        if (this.size() != other.size()) {
            return false;
        }

        if (this.isEmpty() && other.isEmpty()) {
            return true;
        }

        Node<E> start = this.tail.getNext();
        for (int i = 0; i < this.size(); i++) {
            Node<E> currentSelf = start;
            Node<E> currentOther = other.tail.getNext();
            boolean match = true;
            for (int j = 0; j < this.size(); j++) {
                if (!currentSelf.getElement().equals(currentOther.getElement())) {
                    match = false;
                    break;
                }
                currentSelf = currentSelf.getNext();
                currentOther = currentOther.getNext();
            }
            if (match) {
                return true;
            }
            start = start.getNext();
        }

        return false;
    }

    public static void main(String[] args) {
        CircularlyLinkedList<String> originalList = new CircularlyLinkedList<>();
        originalList.addLast("MSP");
        originalList.addLast("ATL");
        originalList.addLast("BOS");
        System.out.println(originalList);

        CircularlyLinkedList<String> clonedList = originalList.clone();
        System.out.println(clonedList);

        originalList.addLast("ABC");
        System.out.println(originalList);
        clonedList.addLast("XYZ");
        System.out.println(clonedList);

        CircularlyLinkedList<String> list1 = new CircularlyLinkedList<>();
        list1.addLast("MSP");
        list1.addLast("ATL");
        list1.addLast("BOS");

        CircularlyLinkedList<String> list2 = new CircularlyLinkedList<>();
        list2.addLast("ATL");
        list2.addLast("BOS");
        list2.addLast("MSP");

        CircularlyLinkedList<String> list3 = new CircularlyLinkedList<>();
        list3.addLast("BOS");
        list3.addLast("MSP");
        list3.addLast("ATL");

        CircularlyLinkedList<String> list4 = new CircularlyLinkedList<>();
        list4.addLast("MSP");
        list4.addLast("BOS");
        list4.addLast("ATL");

        System.out.println(list1);
        System.out.println(list2);
        System.out.println(list3);
        System.out.println(list4);

        System.out.println(list1.sameSequence(list2));
        System.out.println(list1.sameSequence(list3));
        System.out.println(list1.sameSequence(list4));
    }
}
