#include <iostream>
#include <vector>
using namespace std;

vector<int> solve(const vector<vector<int>>& a) {
  vector<int> res;
  int n = a.size();
  bool dir = 0;
  for (int k=0; k<n; ++k) {
    for (int i=k; i>=0; --i) {
      res.push_back(dir ? a[i][k-i] : a[k-i][i]);
    }
    dir = !dir;
  }
  for (int k=0; k<n-1; ++k) {
    for (int i=n-1; i>k; --i) {
      res.push_back(dir ? a[i][n-i+k] : a[n-i+k][i]);
    }
    dir = !dir;
  }
  return res;
}

int main(void) {
  // works only for square matrices (if you want look for a more iterative that handles more cases } 
  vector<vector<int>> m = {{1,3,4,10},{2,5,9,11},{6,8,12,15},{7,13,14,16}};
  vector<vector<int>> m = {{1, 2, 3, 4, 5}};
  auto res = solve(m);
  for (int n: res) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}


