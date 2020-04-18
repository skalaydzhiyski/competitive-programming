#include <cstdio>

bool solve(int h, int n, int m) {
  // nice simple and clean brother
  while (h > 0 && n && h > h/2+10) {
    h = h/2 + 10;
    n--;
  }
  return h <= m*10;
}

int main(void) {
  int t, h, n, m;
  scanf("%d", &t);
  for (int i=0; i<t; ++i) {
    scanf("%d %d %d", &h, &n, &m);
    puts(solve(h, n, m) ? "YES" : "NO");
  }
  return 0;
}

