#include <vector>
using namespace std;

class LinkedList {
public:
  int value;
  LinkedList *next;

  LinkedList(int value);
  void addMany(vector<int> values);
  vector<int> getNodesInArray();
};

void removeKthNodeFromEnd(LinkedList *head, int k) {
  LinkedList* current = head;
  LinkedList* ptr_prev = head;
  LinkedList* ptr = head->next;
  int counter = 0;
  while (counter++ != k) {
    current = current->next;
  }
  if (not current) {
    head = ptr;
    head->value = ptr->value;
    return;
  }
  while (current) {
    if (not current->next) {
      ptr_prev->next = ptr->next;
      ptr->next = nullptr;
      ptr = nullptr;
      return;
    }
    current = current->next;
    ptr = ptr->next;
    ptr_prev = ptr_prev->next;
  }
}

