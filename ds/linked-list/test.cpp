using namespace std;

class Node {
public:
  int value;
  Node *prev;
  Node *next;
  Node(int value);
};

class DoublyLinkedList {
public:
  Node *head;
  Node *tail;

  DoublyLinkedList() {
    head = NULL;
    tail = NULL;
  }

  void setHead(Node *node) {
    if (not head) {
      head = node;
      tail = node;
    } else {
      insertBefore(head, node);
    }
  }

  void setTail(Node *node) {
    if (not tail) {
      setHead(node);
    } else {
      insertAfter(tail, node);
    }
  }

  void insertBefore(Node *node, Node *nodeToInsert) {
    if (nodeToInsert == head and nodeToInsert == tail)
      return;
    remove(nodeToInsert);
    nodeToInsert->prev = node->prev;
    nodeToInsert->next = node;
    if (node->prev) {
      node->prev->next = nodeToInsert;
    } else {
      head = nodeToInsert;
    }
    node->prev = nodeToInsert;
  }

  void insertAfter(Node *node, Node *nodeToInsert) {
    if (nodeToInsert == head and nodeToInsert == tail)
      return;
    remove(nodeToInsert);
    nodeToInsert->next = node->next;
    nodeToInsert->prev = node;
    if (node->next) {
      node->next->prev = nodeToInsert;
    } else {
      tail = nodeToInsert;
    }
    node->next = nodeToInsert;
  }

  void insertAtPosition(int position, Node *nodeToInsert) {
    if (position == 1) {
      setHead(nodeToInsert);
      return;
    }
    Node* node = head;
    int pos = 1;
    while (node and pos++ != position) {
      node = node->next;
    }
    if (node) {
      insertBefore(node, nodeToInsert);
    } else {
      setTail(nodeToInsert);
    }
  }

  void removeNodesWithValue(int value) {
    Node* node = head;
    while (node) {
      Node* toremove = node;
      node = node->next;
      if (toremove->value == value) {
        remove(toremove);
      }
    }
  }

  void remove(Node *node) {
    if (node == head) {
      head = node->next;
    }
    if (node == tail) {
      tail = node->prev;
    }
    removeLinks(node);
  }

  void removeLinks(Node* node) {
    if (node->prev) {
      node->prev->next = node->next;
    }
    if (node->next) {
      node->next->prev = node->prev;
    }
    node->prev = nullptr;
    node->next = nullptr;
  }

  bool containsNodeWithValue(int value) {
    Node* node = head;
    while (node) {
      if (node->value == value) {
        return true;
      }
      node = node->next;
    }
    return false;
  }
};

