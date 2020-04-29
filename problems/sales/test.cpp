#include <algorithm>
#include <cstdio>

using namespace std; 

int main(void) {
  int n, m, a[100];
  scanf("%d %d", &n, &m);
  for (int i=0; i<n; ++i) {
    scanf("%d", &a[i]);
  }
  sort(a, a+n);
  int res = 0;
  for (int i=0; i<m; ++i) {
    if (a[i] < 0) {
      res += a[i];
    }
  }
  printf("%d", -res);
  return 0;
}

