#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Solution 2 
void solve(vector<vector<int>>& res, int i, vector<int>& a) {
  if (i == a.size()-1) {
    res.push_back(a);
    return;
  }
  for (int j=i; j<a.size(); ++j) {
    swap(a[i], a[j]);
    solve(res, i+1, a);
    swap(a[i], a[j]);
  }
}

vector<vector<int>> getPermutations(vector<int>& a) {
  if (a.size() == 0) {
    return {};
  }
  vector<vector<int>> res;
  solve(res, 0, a);
  return res;
}

int main(void) {
  vector<int> a {1, 2, 3};
  auto res = getPermutations(a);
  for (vector<int> inner: res) {
    for (int n: inner) {
      cout << n << " ";
    }
    cout << endl;
  }
  return 0;
}

