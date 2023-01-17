#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>
#include <cmath>

int solve(int x) {
  int res = 0;
  for (int i=5; i>=1; --i) {
    if (x < i) continue;
    if (x % i == 0) {
      res += x/i;
      break;
    }
    res += x/i;
    x %= i; 
  }
  return res;
}

int main(void) {
  int x;
  scanf("%d", &x);
  printf("%d", solve(x));
  return 0;
}
