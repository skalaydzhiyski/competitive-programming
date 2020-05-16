#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Optimal time: O(N2) , space O(N)
vector<vector<int>> solve(vector<int>& v, int t) {
  sort(v.begin(), v.end());
  vector<vector<int>> res;
  int n = v.size();
  for (int i=0; i<n-2; ++i) {
    int left = i+1;
    int right = n-1;
    while (left < right) {
      int sum = v[i] + v[left] + v[right];
      if (sum == t) {
        res.push_back({v[i], v[left], v[right]});
        left++;
        right--;
      } else if (sum > t) {
        right--;
      } else {
        left++;
      }
    }
  }
  return res;
}

int main(void) {
  vector<int> a {12, 3, 1, 2, -6, 5, -8, 6};
  int t = 0;
  const auto res = solve(a, t);
  for (const vector<int>& inner: res) {
    for (int n: inner) {
      cout << n << " ";
    }
    cout << endl;
  }
  return 0;
}

