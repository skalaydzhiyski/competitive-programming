#include <vector>
using namespace std;

// Do not edit the class below except
// for the depthFirstSearch method.
// Feel free to add new properties
// and methods to the class.
class Node {
public:
  string name;
  vector<Node *> children;

  Node(string str) { name = str; }

  vector<string> depthFirstSearch(vector<string> *array) {
    vector<string> res{name};
    for (Node* child: children) {
      auto child_nodes = child->depthFirstSearch(&res);
      res.insert(res.end(), child_nodes.begin(), child_nodes.end());
    }
    return res;
  }

  Node *addChild(string name) {
    Node *child = new Node(name);
    children.push_back(child);
    return this;
  }
};


