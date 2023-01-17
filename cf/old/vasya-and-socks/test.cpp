#include <cstdio>

int main(void) {
  int n, m;
  scanf("%d %d", &n, &m);
  if (n<m) {
    printf("%d", n);
    return 0;
  }
  if (n/m == 1 && n > m) {
    printf("%d", n+1);
    return 0;
  }
  int res = n;
  while (n >= m) {
    printf("n: %d n/m: %d, rem: %d curreent res : %d \n", n, n/m, n%m , res);
    int remainder = n%m == 1 ? n%m : 0;
    res += n/m + remainder;
    n /= m;
  }
  printf("%d", res);
  return 0;
}

