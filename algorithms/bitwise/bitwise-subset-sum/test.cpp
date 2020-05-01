#include <string>
#include <cstdio>

// used for debugging
std::string tobits(const int x) {
  std::string res = "";
  int n = 16;
  for (int i=n-1; i>=0; --i) {
    res += x & (1<<i) ? "1" : "0";
  }
  return res;
}

int main(void) {
  // works for small N, for larger N use std::bitset!
  int n, s;
  scanf("%d %d", &n, &s);
  int a[n];
  for (int i=0; i<n; ++i) {
    scanf("%d", &a[i]);
  }
  /* 1<<n = 2^n => and it gives us the number of bits we will need
     to indicate the indices for the subset sums */
  for (int mask=0; mask<(1<<n); ++mask) {
    long long sum = 0;
    for (int i=0; i<n; ++i) {
      // if the bit is ON we add the number to the sum
      if (mask & (1<<i)) {
        sum += a[i];
      }
      if (sum == s) {
        puts("YES");
        return 0;
      }
    }
  }
  puts("NO");
  return 0;
}

