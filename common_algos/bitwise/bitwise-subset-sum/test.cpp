#include <string>
#include <cstdio>

std::string tobits(const int x) {
  std::string res = "";
  int n = 16;
  for (int i=n-1; i>=0; --i) {
    res += x & (1<<i) ? "1" : "0";
  }
  return res;
}

int main(int argc, const char** argv) {
  int n, s;
  scanf("%d %d", &n, &s);
  int a[n];

  for (int i=0; i<n; ++i)
    scanf("%d", &a[i]);

  for (int mask=0; mask<(1<<n); ++mask) {
    long long sum = 0;
    for (int i=0; i<n; ++i) {
      if (mask & (1<<i))
        sum += a[i];
      if (sum == s) {
        puts("YES");
        return 0;
      }
    }
  }
  puts("NO");
  return 0;
}

