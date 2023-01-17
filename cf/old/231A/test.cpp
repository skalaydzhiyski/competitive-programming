#include <iostream>
#include <cstdio>

int main(void) {
  int n, confidence;
  scanf("%d", &n);
  int outer = 0;
  for (int i=0; i<n; ++i) {
    int sum = 0;
    for (int j=0; j<3; ++j) {
      std::cin >> confidence;
      sum += confidence;
    }
    if (sum >= 2) {
      outer++;
    }
  }
  printf("%d", outer);
  return 0;
}

