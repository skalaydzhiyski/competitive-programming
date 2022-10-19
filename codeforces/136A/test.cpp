#include <cstdio>

int main(void) {
  int n, fr;
  scanf("%d", &n);
  int res[n];
  for (int i=0; i<n; ++i) {
    scanf("%d", &fr);
    res[fr-1] = i+1;
  }
  for (int i=0; i<n; ++i) {
    printf("%d ", res[i]);
  }
  return 0;
}

