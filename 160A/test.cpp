#include <iostream>
#include <cstdio>
#include <algorithm>
#include <numeric>

int main(void) {
  int n, total=0, subsum=0;
  scanf("%d", &n);
  int coins[n];
  for (int i=0; i<n; ++i) {
    scanf("%d", &coins[i]);
    total += coins[i];
  }
  if (n == 1) {
    puts("1");
    return 0;
  }

  std::sort(coins, coins+n);
  for (int i=n-1; i>=0; --i) {
    subsum += coins[i];
    total -= coins[i];
    if (subsum > total) {
      printf("%d", n-i);
      return 0;
    }
  }
  return 0;
}

