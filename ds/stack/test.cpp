#include <iostream>
#include <cstdlib>
using namespace std;

struct Node {
  int value;
  Node* next;
};
struct Node* top;

void push(int value) {
  Node* temp = new Node();
  temp->value = value;
  temp->next = top;
  top = temp;
}

int pop() {
  int res = top->value;
  Node* temp = top;
  top = top->next;
  temp->next = nullptr;
  free(temp);
  return res;
}

void print_all() {
  Node* current = top;
  while (current) {
    cout << current->value << ", next (" << current->next << ")";
    if (current->next) {
      cout << " -> ";
    }
    current = current->next;
  }
  cout << endl;
}

int peek(Node* top) {
  return top->value;
}

int main(void) {
  push(1);
  push(2);
  push(3);
  push(4);
  print_all();
  return 0;
}
