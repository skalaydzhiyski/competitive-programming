#include <cstdio>

#define MAXN 100000

int solve(int n, int* a, int* p) {
  int res = 0;
  for (int i=0; i<n; ++i) {
    int future = 0, j = i+1;
    while (p[i] <= p[j] && j < n) {
      future += a[j++] * p[i];
    }
    res += a[i] * p[i] + future;
    if (future) {
      i=j-1;
    }
  }
  return res;
}

int main(void) {
  int n, a[MAXN], p[MAXN];
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    scanf("%d %d", &a[i], &p[i]);
  }
  printf("%d", solve(n, a, p));
  return 0;
}

