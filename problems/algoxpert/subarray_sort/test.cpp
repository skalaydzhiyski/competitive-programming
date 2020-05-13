#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(const vector<int>& a) {
  int n = a.size();
  if (n < 2) return {};
  // todo: write your solution here
}

int main(void) {
  vector<int> a {1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19};
  for (int n: solve(a)) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}

