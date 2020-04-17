#include <iostream>
#include <cstdio>

int main(void) {
  int n, p;
  std::cin >> n;
  int lvl[n];
  for (int i=0; i<n; ++i) {
    lvl[i]=0;
  }
  int count = 0;
  for (int k=0; k<2; ++k) {
    std::cin >> p;
    for (int i=0; i<p; ++i) {
      int current;
      std::cin >> current;
      if (lvl[current-1] == 0) {
        count++;
      }
      lvl[current-1] = 1;
    }
  }
  std::cout << (count == n ? "I become the guy." : "Oh, my keyboard!");
  return 0;
}

