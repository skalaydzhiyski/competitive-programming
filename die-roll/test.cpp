#include <string>
#include <cstdio>

std::string solve(int y, int w) {
  std::string res;
  int max = y>w ? y : w;
  int prob = 6 - max + 1;
  if (prob == 3) {
    res = "1/2";
  } else if (prob == 4) {
    res = "2/3";
  } else if (prob == 2) {
    res = "1/3";
  } else if (prob == 6) {
    res = "1/1";
  } else if (prob == 0) {
    res = "0/1";
  } else {
    res += std::to_string(prob) + "/6";
  }
  return res;
}

int main(void) {
  int y, w;
  scanf("%d %d", &y, &w);
  printf("%s", solve(y, w).c_str());
  return 0;
}

