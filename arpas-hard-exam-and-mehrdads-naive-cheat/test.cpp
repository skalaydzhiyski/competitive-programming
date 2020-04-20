#include <cstdio>

int main(void) {
  int digits[] = {8, 4, 2, 6};
  int n, x = 1378;
  scanf("%d", &n);
  printf("%d", n==0 ? 1 : digits[(n-1)%4]);
  return 0;
}

