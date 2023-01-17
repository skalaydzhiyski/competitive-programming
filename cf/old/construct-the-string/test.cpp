#include <string>
#include <cstdio>

static const std::string alpha = "abcdefghijklmnopqrstuvwxyz";

std::string solve(int n, int a, int b) {
  std::string res = "";
  char ch;
  for (int i=0; i<n; ++i) {
    res += alpha[i % b];
  }
  return res;
}

int main(void) {
  int t, n, a, b;
  scanf("%d", &t);
  for (int i=0; i<t; ++i) {
    scanf("%d %d %d", &n, &a, &b);
    puts(solve(n, a, b).c_str());
  }
  return 0;
}

