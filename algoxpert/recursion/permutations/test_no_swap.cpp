#include <iostream>
#include <vector>
using namespace std;

vector<int> remove(vector<int>& a, int n) {
  vector<int> res;
  for (int ai: a) {
    if (ai != n) {
      res.push_back(ai);
    }
  }
  return res;
}

void solve(vector<vector<int>>& res,
           vector<int> c, vector<int> a) {
  if (a.size() == 0) {
    res.push_back(c);
  } else {
    for (int n: a) {
      auto rest = remove(a, n);
      auto perm = c;
      perm.push_back(n);
      solve(res, perm, rest);
    }
  }
}

vector<vector<int>> getPermutations(vector<int>& a) {
  if (a.size() == 0) {
    return {};
  }
  vector<vector<int>> res;
  solve(res, vector<int>{}, a);
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

