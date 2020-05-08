#include <iostream>
#include <vector>
#include <climits>
#include <cmath>
using namespace std;

vector<int> solve(vector<int>& a, vector<int>& b) {
  if (a.size() > b.size()) {
    return solve(b, a);
  }
  sort(b.begin(), b.end());
  for (auto& n: b) cout << n << " ";
  cout << endl;
  
  int n = a.size();
  vector<int> res{};
  int min = INT_MAX;
  for (int i=0; i<n; ++i) {
    int first = a[i];
    int second;
    int left = 0;
    int right = b.size()-1;
    int min_ = INT_MAX;
    while (left <= right) {
      int m = left + (right-left)/2;
      second = b[m];
      if (first == second) {
        return {first, second};
      }
      if (first > second) {
        left = m+1;
      } else {
        right = m-1;
      }
      int d = abs(first - second);
      if (d < min_) {
        min_ = d;
      }
    }
    if (min_ < min) {
      min = min_;
      res = {first, second};
    }
  }
  return res;
}

int main(void) {
  vector<int> a {5, 10, 20, 28, 3};
  vector<int> b {1, 2, 3};
  vector<int> res = solve(a, b);
  for (int a: res) {
    cout << a << endl;
  }
  return 0;
}

