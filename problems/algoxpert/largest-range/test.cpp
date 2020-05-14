#include <iostream>
#include <utility>
#include <vector>
#include <unordered_map>
#include <bitset>
using namespace std;

vector<int> solve(const vector<int>& a) {
  unordered_map<int, int> d, links;
  int n = a.size();
  for (int i=0; i<n; ++i) {
    d.insert({a[i], a[i]+1});
  }
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

int main(void) {
  vector<int> a {1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6};
  auto res = solve(a);
  cout << res.first << " " << res.second << endl;
  return 0;
}

