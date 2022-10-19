#include <iostream>
#include <utility>
#include <vector>
#include <unordered_map>
#include <bitset>
using namespace std;

const vector<int> solve_old(const vector<int>& a) {
  unordered_map<int, int> d, links;
  int n = a.size();
  for (int i=0; i<n; ++i) {
    d.insert({a[i], a[i]+1});
  }
  // find start -> end pair (connected sequence)
  for (int i=0; i<n; ++i) {
    int first = a[i];
    int k = a[i];
    while (d.find(k) != d.end()) {
      k = d[k];
      d.erase(k-1);
    }
    if (first < k+1) {
      if (links.find(k) != links.end()) {
        links.insert({first, links[k]});
        d.erase(k);
      } else {
        links.insert({first, k-1});
      }
    }
  }
  // max pair
  pair<int, int> res;
  int max = 0;
  for (const auto& p: links) {
    int diff = p.second - p.first;
    if (diff > max) {
      res = {p.first, p.second};
      max = diff;
    }
  }
  return {res.first, res.second};
}

const vector<int> solve(const vector<int>& a) {
  int n = a.size();
  vector<int> res;
  unordered_map<int, bool> m;
  for (int i=0; i<n; ++i) {
    m[a[i]] = 1;
  }
  int max = 0;
  for (int i=0; i<n; ++i) {
    int left = a[i] - 1;
    int right = a[i] + 1;
    int len = 1;
    // stretch left
    while (m.find(left) != m.end()) {
      len++;
      left--;
    }
    while (m.find(right) != m.end()) {
      len++;
      right++;
    }
    if (len > max) {
      max = len;
      res = {left+1, right-1};
    }
  }
  return res;
}

int main(void) {
  vector<int> a {1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6};
  auto res = solve(a);
  for (auto& n: res) {
    cout << n << endl;
  }
  return 0;
}

