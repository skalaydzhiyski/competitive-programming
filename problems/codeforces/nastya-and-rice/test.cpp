#include <cstdio>

const char* solve(int n, int a, int b, int c, int d) {
  int min = n*(a-b);
  int max = n*(a+b);
  return c+d < min || c-d > max ? "NO" : "YES";
}

int main(void) {
  int t, n, a, b, c, d;
  scanf("%d", &t);
  for (int i=0; i<t; ++i) {
    scanf("%d %d %d %d %d", &n, &a, &b, &c, &d);
    puts(solve(n, a, b, c, d));
  }
  return 0;
}

