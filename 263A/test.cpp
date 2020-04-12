#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdio>

int main(void) {
  int matrix[5][5], iloc, jloc;
  for (int i=0; i<5; ++i) {
    for (int j=0; j<5; ++j) { 
      std::cin >> matrix[i][j];
      if (matrix[i][j]) {
        iloc = i;
        jloc = j;
      }
    }
  }
  printf("%d", abs(2-iloc) + abs(2-jloc));
  return 0;
}
