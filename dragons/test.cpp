#include <algorithm>
#include <cstdio>

struct dragon {
  int x,y;
};

int main(void) {
  int s, n;
  scanf("%d %d", &s, &n);
  std::vector<std::pair<int>> t(n);
  for (int i=0; i<n; ++i) {
    std::pair<int> d;
    scanf("%d %d", &d.first, &d.second);
    if (d.first < s) {
      s += d.second;
    } else {
      t.push_back(d);
    }
  }
  printf("%d", s);

  return 0;
}

