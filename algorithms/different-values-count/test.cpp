#include <iostream>
#include <bitset>
#include <cstdio>
#include <cstdlib>

#define NBITS 1000000

int main(void) {
  int n;
  scanf("%d", &n);
  std::bitset<NBITS> visited;
  for (int i=0; i<n; ++i) {
    // this should be scanf in the real-world scenario
    long long x = rand() % NBITS + 1;
    // set bit on !
    visited[x] = 1;
  }
  std::cout << visited.count() << std::endl;
  return 0;
}

