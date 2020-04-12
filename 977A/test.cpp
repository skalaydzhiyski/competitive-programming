#include <cstdio>

int main(void) {
  unsigned short k;
  unsigned long n, res;
  scanf("%lu %hu", &n, &k);
  res = n;
  for (int i=0; i<k; ++i) {
    if (res % 10 == 0)
      res /= 10;
    else
      res --;
  }
  printf("%ld", res);
  return 0;
}


