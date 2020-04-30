#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;

#define N 11

int findmin(int* a) {
  int left = 0;
  int right = N-1;
  int res = -1;
  while (left <= right) {
    int m = left + (right-left)/2;
    cout << left << " " << right << " ans: " << res << endl;
    if (a[m] <= right) {
      // a[m] at this point is a good answer
      res = a[m];
      // continue searching for even smaller numbers
      right = m-1;
    } else {
      left = m+1;
    }
  }
  return res;
}

int main(void) {
  int a[N] = {6,7,9,15,19,20,21,2,3,4,5};
  for (auto& n: a) {
    cout << n << " ";
  }
  cout << endl;
  cout << findmin(a) << endl;
  return 0;
}

