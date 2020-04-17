#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <cstdio>

int main(void) {
  int s, n;
  bool dead = false;
  std::cin >> s >> n;
  std::vector<std::pair<int, int>> t;
  for (int i=0; i<n; ++i) {
    std::pair<int, int> d;
    std::cin >> d.first >> d.second;
    if (d.first < s) {
      s += d.second;
    } else {
      t.push_back(d);
    }
  }
  std::sort(t.begin(), t.end());
  int size = t.size();
  for (auto it = t.begin(); it != t.end(); ++it) {
    if ((*it).first < s) {
      s += (*it).second;
      size--;
    } 
  }
  if (size == 0) {
    puts("YES");
  } else {
    puts("NO");
  }
  return 0;
}

