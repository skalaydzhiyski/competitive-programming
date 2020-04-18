#include <cstdio>

int main(void) {
  int n, res = 0;
  scanf("%d", &n);
  for (int k=n; k>=2; --k) {
    res += k + (k-1)*(n-k);
  }
  printf("%d", res+1);
  return 0;
}

