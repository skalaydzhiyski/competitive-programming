#include <algorithm>
#include <cstdio>
#include <climits>

int main(void) {
  int n, m, a[50];
  scanf("%d %d", &n, &m);
  for (int i=0; i<m; ++i) scanf("%d", &a[i]);

  std::sort(a, a+m);
  int min = INT_MAX;
  for (int i=0; i<=m-n; ++i) {
    int diff = a[i+n-1] - a[i];
    if (diff < min) {
      min = diff;
    }
  }
  printf("%d", min == INT_MAX ? 0 : min);
  return 0;
}

