#include <iostream>
#include <bitset>
#include <cstdio>
using namespace std;

int main(void) {
  // warm up unique numbers
  bitset<MAX> bits;
  int n;
  scanf("%d", &n);
  for (int i=0; i<n; ++i) {
    long x;
    scanf("%ld", &x);
    bits[x] = 1;
  }
  cout << bits << endl;
  printf("%d", bits.count());
  return 0;
}

