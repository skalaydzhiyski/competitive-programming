#include <iostream>
#include <vector>
using namespace std;

// iterative
void solve_iter(vector<vector<int>>& res, const vector<int>& a) {
  for (int i=0; i<a.size(); ++i) {
    int size = res.size();
    for (int j=0; j<size; ++j) {
      auto current = res[j];
      auto new_set = current;
      new_set.push_back(a[i]);
      res.push_back(new_set);
    }
  }
}

vector<vector<int>> powerset(const vector<int>& a) {
  vector<vector<int>> res{{}};
  solve_iter(res, a);
  return res;
}

int main(void) {
  vector<int> a {1,2,3};
  auto res = powerset(a);
  for (auto inner: res) {
    for (int n: inner) {
      cout << n << " ";
    }
    cout << endl;
  }
  return 0;
}

