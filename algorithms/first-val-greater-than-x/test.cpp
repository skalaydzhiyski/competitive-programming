#include <iostream>
#include <bitset>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

#define N 1000

int solve(int* a, int x) {
  // do bin search
  int left = 0;
  int right = N-1;
  int res = -1;
  while (left < right) {
    int m = left + (right-left)/2;
    if (a[m] >= x) {
      res = a[m];
      right = m-1;
    } else {
      left = m+1;
    }
  }
  return res;
}

int main(void) {
  int x = 18, a[N];
  for (int i=0; i<N; ++i) {
    a[i] = rand() % 1000 + 1;
  }
  for (auto& c: a) { cout << c << " "; }
  cout << endl << " ------------------------ " << endl;
  sort(a, a+N);
  for (auto& c: a) { cout << c << " "; }
  cout << endl;
  cout << solve(a, x) << endl;
  return 0;
}

