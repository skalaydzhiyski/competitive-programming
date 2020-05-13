#include <iostream>
#include <vector>
#include <utility>
#include <unordered_map> 
using namespace std;

vector<vector<int>> solve(const vector<int>& a, int t) {
  vector<vector<int>> res;
  int n = a.size();
  unordered_map<int, vector<vector<int>>> pairsum;
  for (int i=0; i<n-1; ++i) {
    for (int j=i+1; j<n; ++j) {
      int current_sum = (a[i]+a[j]);
      int diff = t - current_sum;
      if (pairsum.find(diff) != pairsum.end()) {
        for (vector<int> pair: pairsum[diff]) {
          pair.push_back(a[i]);
          pair.push_back(a[j]);
          res.push_back(pair);
        }
      }
    }
    for (int k=0; k<i; ++k) {
      int current_sum = a[i] + a[k];
      if (pairsum.find(current_sum) == pairsum.end()) {
        pairsum[current_sum] = vector<vector<int>> { {a[k], a[i] } };
      } else {
        pairsum[current_sum].push_back(vector<int>{a[k], a[i]});
      }
    }
  }
  return res;
}

int main(void) {
  int t = 16;
  vector<int> a {7, 6, 4, -1, 1, 2};
  auto res = solve(a, t);
  for (const auto& inner: res) {
    for (const auto& n: inner) {
      cout << n << " ";
    }
    cout << endl;
  }
  return 0;
}

