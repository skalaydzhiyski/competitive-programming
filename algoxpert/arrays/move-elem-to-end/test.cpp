#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

vector<int> solve(vector<int> a, int t) {
  int n = a.size();
  int idx = 0;
  for (int i=0; i<n; ++i) {
    if (a[i] != t) {
      a[idx++] = a[i];
    }
  }
  for (int i=idx; i<n; ++i) {
    a[i] = t;
  }
  return a;
}

int main(void) {
  vector<int> a{2, 1, 2, 2, 2, 3, 4, 2};
  int t = 2;
  auto res = solve(a, t);
  for (int n: res) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}

