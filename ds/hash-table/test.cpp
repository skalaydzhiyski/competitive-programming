#include <iostream>
#include <string>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <memory>
using namespace std;

#define HASH_STORE_SIZE 10

struct Node {
  int value;
  shared_ptr<Node> next;
};

class HashMap {
  shared_ptr<Node> store[HASH_STORE_SIZE];
  int random;
public:
  HashMap();

  int make_hash(const string&);
  void add(const string&, int);
  int get(const string&);
  void print_all();
};

HashMap::HashMap() {
  srand(42);
  random = rand() % 10;
  for (int i=0; i<HASH_STORE_SIZE; ++i) {
    store[i] = make_shared<Node>();
    store[i]->value = 0;
  }
}

int HashMap::make_hash(const string& key) {
  int index;
  for (int i=0; i<key.size(); ++i) {
    index += (int)key[i] + random;
  }
  return index % 10;
}

void HashMap::add(const string& key, const int value) {
  int idx = make_hash(key); 
  cout << "random: " << random << "  adding at index " << idx << " , key " << key << endl;
  auto node = store[idx];
  if (node->value == 0) {
    store[idx]->value = value;
    return;
  }
  while (node) {
    if (not node->next) {
      node->next = make_shared<Node>();
      node->next->value = value;
      return;
    }
    node = node->next;
  }
}

int HashMap::get(const string& key) {
  cout << "getting value for key " << key << " with hash: " << make_hash(key) << endl;
  return store[make_hash(key)]->value;
}

void HashMap::print_all() {
  for (int i=0; i<HASH_STORE_SIZE; ++i) {
    cout << i << ": ";
    auto node = store[i];
    while (node) {
      cout << node->value;
      if (node->next) {
         cout << " -> ";
      }
      node = node->next;
    }
    cout << endl;
  }
}

int main(void) {
  HashMap map;
  map.add("spas", 1024);
  map.add("george", 100);
  map.add("pesho", 200);
  map.add("petkan", 300);
  map.add("magda", 400);
  map.add("timi", 500);
  map.print_all();
  cout << endl;
  cout << map.make_hash("spas") << endl;
  cout << map.get("spas") << endl;
  return 0;
}

