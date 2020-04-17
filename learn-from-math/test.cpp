#include <cmath>
#include <cstdio>

bool composite(int x) {
  if (x <= 2) {
    return false;
  }
  for (int i=2; i*i<=x; ++i) {
    if (x % i == 0) {
      return true;
    }
  }
  return false;
}

int main(void) {
  int n;
  scanf("%d", &n);
  for (int i=3; i<n; ++i) {
    if (composite(i) && composite(n-i)) {
      printf("%d %d", i, n-i);
      return 0;
    }
  }
  return 0;
}

