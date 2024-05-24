package exercise1;

public class DoublyLinkedList<E> {

  private static class Node<E> {

    private E element;
    private Node<E> prev;
    private Node<E> next;

    public Node(E e, Node<E> p, Node<E> n) {
      element = e;
      prev = p;
      next = n;
    }

    public E getElement() {
      return element;
    }

    public Node<E> getPrev() {
      return prev;
    }

    public Node<E> getNext() {
      return next;
    }

    public void setPrev(Node<E> p) {
      prev = p;
    }

    public void setNext(Node<E> n) {
      next = n;
    }

  }

  private Node<E> header;
  private Node<E> trailer;
  private int size = 0;

  public DoublyLinkedList() {
    header = new Node<>(null, null, null);
    trailer = new Node<>(null, header, null);
    header.setNext(trailer);
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
    return header.getNext().getElement();
  }

  public E last() {
    if (isEmpty())
      return null;
    return trailer.getPrev().getElement();
  }

  public void addFirst(E e) {
    addBetween(e, header, header.getNext());
  }

  public void addLast(E e) {
    addBetween(e, trailer.getPrev(), trailer);
  }

  public E removeFirst() {
    if (isEmpty())
      return null;
    return remove(header.getNext());
  }

  public E removeLast() {
    if (isEmpty())
      return null;
    return remove(trailer.getPrev());
  }

  private void addBetween(E e, Node<E> predecessor, Node<E> successor) {
    Node<E> newest = new Node<>(e, predecessor, successor);
    predecessor.setNext(newest);
    successor.setPrev(newest);
    size++;
  }

  private E remove(Node<E> node) {
    Node<E> predecessor = node.getPrev();
    Node<E> successor = node.getNext();
    predecessor.setNext(successor);
    successor.setPrev(predecessor);
    size--;
    return node.getElement();
  }

  public String toString() {
    StringBuilder sb = new StringBuilder("(");
    Node<E> walk = header.getNext();
    while (walk != trailer) {
      sb.append(walk.getElement());
      walk = walk.getNext();
      if (walk != trailer)
        sb.append(", ");
    }
    sb.append(")");
    return sb.toString();
  }

  public void swapTwoNodes(Node<E> node1, Node<E> node2) {
    if (node1 == node2) {
      return;
    }

    // Check if node1 and node2 are adjacent
    if (node1.getNext() == node2) {
      Node<E> tempPrev = node1.getPrev();
      Node<E> tempNext = node2.getNext();

      node1.setNext(tempNext);
      node1.setPrev(node2);

      node2.setNext(node1);
      node2.setPrev(tempPrev);

      if (tempPrev != null) {
        tempPrev.setNext(node2);
      } else {
        header.setNext(node2);
      }

      if (tempNext != null) {
        tempNext.setPrev(node1);
      } else {
        trailer.setPrev(node1);
      }

    } else if (node2.getNext() == node1) {
      swapTwoNodes(node2, node1);
    } else {
      Node<E> node1Next = node1.getNext();
      Node<E> node1Prev = node1.getPrev();
      Node<E> node2Next = node2.getNext();
      Node<E> node2Prev = node2.getPrev();

      if (node1Next != null) {
        node1Next.setPrev(node2);
      }
      if (node1Prev != null) {
        node1Prev.setNext(node2);
      }
      if (node2Next != null) {
        node2Next.setPrev(node1);
      }
      if (node2Prev != null) {
        node2Prev.setNext(node1);
      }

      node1.setNext(node2Next);
      node1.setPrev(node2Prev);
      node2.setNext(node1Next);
      node2.setPrev(node1Prev);

      if (header.getNext() == node1) {
        header.setNext(node2);
      } else if (header.getNext() == node2) {
        header.setNext(node1);
      }

      if (trailer.getPrev() == node1) {
        trailer.setPrev(node2);
      } else if (trailer.getPrev() == node2) {
        trailer.setPrev(node1);
      }
    }
  }

  public static void main(String[] args) {
    DoublyLinkedList<String> list = new DoublyLinkedList<>();
    list.addLast("MSP");
    list.addLast("ATL");
    list.addLast("BOS");
    list.addLast("LAX");
    System.out.println("Before swapping: " + list);

    Node<String> node1 = list.header.getNext().getNext();
    Node<String> node2 = list.trailer.getPrev();
    list.swapTwoNodes(node1, node2);
    System.out.println("After swapping: " + list);
  }
}
