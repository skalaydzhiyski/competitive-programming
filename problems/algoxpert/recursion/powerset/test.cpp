#include <iostream>
#include <vector>
using namespace std;

void solve_iter(vector<vector<int>>& res, vector<int>& a) {
  int n = a.size();
  // for every elemnt in the master set
  for (int i=0; i<n; ++i) {
    int current_size = res.size();
    // add the current elemnt to every set from ther resulting powerset
    for (int j=0; j<current_size; ++j) {
      // we need to keep the copy of the old set res[j]
      auto current = res[j];
      // add the current number to the new set 
      current.push_back(a[i]);
      // and lastly add the new set to the resulting powerset
      res.push_back(current);
    }
  }
}

vector<vector<int>> powerset(vector<int>& a) {
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

