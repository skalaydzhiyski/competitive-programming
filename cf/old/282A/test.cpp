#include <string>
#include <iostream>
#include <cstdio>

int main(void) {
  int n,  x=0;
  scanf("%d", &n);
  std::string op;
  for (int i=0; i<n; ++i) {
    std::cin >> op;
    if (op.find("+") != std::string::npos) {
      x++;
    } else {
      x--;
    }
  }
  printf("%d", x);
  return 0;
}

