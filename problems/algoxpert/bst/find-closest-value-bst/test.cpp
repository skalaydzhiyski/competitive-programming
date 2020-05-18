#include <iostream>
using namespace std;

class Node {
public:
  int data;
  Node* left;
  Node* right;

  Node(const int val) {
    data = val;
    left = nullptr;
    right = nullptr;
  }

  void inorder() {
    cout << "left: ";
    if (left) {
      left.inorder();
    }
    cout << data << " ";
    cout << endl << "right: ";
    if (right) {
      right.inorder();
    }
  }

  void insert(int val) {
    if (v < data) {
      if (!left) {
        Node new_node(val);
        left = new_node;
      } else {
        left->insert(val);
      }
    } else {
      if (!right) {
        Node new_node(val);
        right = new_node;
      } else {
        right->insert(val);
      }
    }
  }

  bool contains(int val) {
    if (val == data) {
      return 1;
    } else if (val < data && left) {
      return left->contains(val);
    } else if (val > data && right) {
      return right->contains(val);
    }
    return false;
  }
};

int main(void) {
  // TODO: continue here and think about a good way of inserting elements
  //  given the dictionary provided by AlgoExpert for the test cases
  return 0;
}

