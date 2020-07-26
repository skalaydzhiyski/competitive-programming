#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

bool balancedBrackets(string str) {
  unordered_map<char, char> pairs {{'{','}'}, {'(',')'}, {'[',']'}};
  vector<char> stack;
  for (const auto& c: str) {
    int size = stack.size();
    switch (c) {
      case '{':
        stack.push_back(pairs[c]);
        break;
      case '[':
        stack.push_back(pairs[c]);
        break;
      case '(':
        stack.push_back(pairs[c]);
        break;
      case '}':
        if (!size && c == stack[size-1]) {
          stack.pop_back();
          break;
        } 
        return false;
      case ']':
        if (!size && c == stack[size-1]) {
          stack.pop_back();
          break;
        }
        return false;
      case ')':
        if (!size && c == stack[size-1]) {
          stack.pop_back();
          break;
        }
        return false;
    }
  }
  return !stack.size();
}

int main(void) {
  string s{"(((((({{{{{[[[[[([)])]]]]]}}}}}))))))"};
  cout << balancedBrackets(s) << endl;
  return 0;
}

