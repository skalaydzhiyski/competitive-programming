#include <cstdio>

int main(void) {
  int n;
  scanf("%d", &n);
  int a[n];
  for (int i=0; i<n; ++i) {
    scanf("%d", &a[i]);
  }
  int len = 1, max=1;
  for (int i=1; i<n; ++i) {
    if (a[i] < a[i-1]) {
      len = 1;
    } else {
      len++;
      if (len > max) {
        max = len;
      }
    }
  }
  printf("%d", max);
  return 0;
}

