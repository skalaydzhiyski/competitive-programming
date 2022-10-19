#include <iostream>
#include <string>
#include <cstdlib>
#include <vector>
#include <unordered_map>
using namespace std;

using Node = unordered_map<string, int>;

class MinMaxStack {
  vector<Node> stack;
public:
  int peek() {
    return stack[stack.size()-1]["value"];
  }

  int pop() {
    int res = stack.back()["value"];
    stack.pop_back();
    return res;
  }

  void push(int number) {
    if (stack.empty()) {
      Node node {
        {"value", number}, {"min", number}, {"max", number}
      };
      stack.push_back(node);
      return;
    }
    Node top = stack[stack.size()-1];
    Node node {{"value", number}};
    node["max"] = max(number, top["max"]);
    node["min"] = min(number, top["min"]);
    stack.push_back(node);
  }

  int getMin() {
    return stack[stack.size()-1]["min"];
  }

  int getMax() {
    return stack[stack.size()-1]["max"];
  }
};

int main(void) {
  MinMaxStack stack;
  stack.push(1);
  stack.push(2);
  stack.push(3);
  return 0;
}


