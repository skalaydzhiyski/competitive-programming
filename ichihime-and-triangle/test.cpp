#include <cstdio>

int main(void) {
  int n, a, b, c, d;
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    scanf("%d %d %d %d", &a, &b, &c, &d);
    printf("%d %d %d\n", b, c, c);
  }
  return 0;
}

