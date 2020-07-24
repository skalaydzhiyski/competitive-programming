#include <iostream>
#include <cstdlib>
using namespace std;

struct Node {
  int value;
  Node* next;
};
Node* head; // pop from the head 
Node* tail; // append to the tail 

void enqueue(int value) {
  Node* temp = new Node();
  temp->value = value;
  if (not tail) {
    tail = temp;
    head = temp;
    return;
  }
  tail->next = temp;
  tail = temp;
}

int dequeue() {
  int res = head->value;
  Node* temp = head;
  head = head->next;
  free(temp);
  return res;
}

void display() {
  Node* current = head;
  cout << "H ";
  while (current) {
    cout << current->value;
    if (current->next) {
      cout << " -> ";
    } else {
      cout << " T" << endl;
    }
    current = current->next;
  }
  cout << endl;
}

int main(void) {
  enqueue(1);
  enqueue(2);
  enqueue(3);
  enqueue(4);
  enqueue(5);
  display();
  cout << "popped item " << dequeue() << endl; 
  cout << "popped item " << dequeue() << endl; 
  display();
  cout << "adding 128 to the queuq" << endl;
  enqueue(128);
  display();
  return 0;
}
