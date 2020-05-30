#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/* Solution 1
 * The gist here is that every number can be at every position and 
 * the rest of the numbers in any given permutation are the numbers 
 * which are NOT the current number;
 * */
void solve2(vector<vector<int>>& res, vector<int> current, vector<int>& a) {
  if (a.size() == 0) {
    res.push_back(current);
  } else {
    for (int i=0; i<a.size(); ++i) {
      int c = a[i];
      auto rest = [&a, &c]() {
        vector<int> res;
        res.reserve(a.size()-1);
        for (int j=0; j<a.size(); ++j) {
          if (a[j] != c) {
            res.push_back(a[j]);
          }
        }
        return res;
      }();
      solve2(res, current, rest);
    }
  }
}

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
  //solve(res, 0, a);
  solve(res, {}, a);
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

