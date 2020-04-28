#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <bitset>

#define NBITS 16

static std::bitset<NBITS> bitsets[2];
static int x[2][5] = {
  {1, 4, 5, 7, 0},
  {1, 5, 7, 3, 2}
};

int intersect(int i, int j) {
  // return count of on bits
  return (bitsets[i] & bitsets[j]).count();
}

int main(int argc, char** argv) {
  // init bitsets
  for (int i=0; i<2; ++i) {
    for (int j=0; j<5; ++j) {
      bitsets[i][x[i][j]] = 1;
    }
  }
  // find max intersect
  int max = 0;
  for (int i=0; i<2; ++i) {
    for (int j=i+1; j<5; ++j) {
      int res = intersect(i, j);
      if (res > max) {
        max = res;
      }
    }
  }
  std::cout << max << std::endl;
  return 0;
}


