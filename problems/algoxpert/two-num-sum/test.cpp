#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

// faster time: O(N), space: O(N)
vector<int> solve_fastest(vector<int>& v, int t) {
  unordered_set<int> nums;
  int n = v.size();
  for (int n: v) {
    int match = t - n;
    if (nums.find(match) != nums.end()) {
      return {n, match}; 
    }
    nums.insert(n);
  }
  return {};
}

// fast time: O(Nlog(N))  , space: O(1) 
vector<int> solve_fast(vector<int>& v, int t) {
  sort(v.begin(), v.end());
  int n = v.size();
  int left = 0;
  int right = n-1;
  // we can't overlap the iterators
  while (left < right) {
    int s = v[left] + v[right];
    if (s == t) {
      return { v[left], v[right] };
    }
    if (s < t) {
      left++;
    } else {
      right--;
    }
  }
  return {};
}

// slow time: 
vector<int> solve(vector<int>& v, int t) {
  for (int i=0; i<v.size(); ++i) {
    for (int j=i+1; j<v.size(); j++) {
      if (v[i] + v[j] == t) {
        return {v[i], v[j]};
      }
    }
  }
  return {};
}

int main(void) {
  vector<int> a {3, 5, -4, 8, 11, 1, -1, 6};
  int t = 10;
  const auto res = solve_fastest(a, t);
  for (const auto& n: res) {
    cout << n << endl;
  }
  return 0;
}

