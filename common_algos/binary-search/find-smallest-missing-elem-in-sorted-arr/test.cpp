#include <iostream>

using namespace std;

int solve(int* a, int n) {
  int left = 0;
  int right = n-1;
  int res = -1;
  while (left <= right) {
    int m = left + (right-left)/2;
    if (a[m] > m) {
      // we are supposed to have the number of idx at this pos
      res = m;
      // find even smaller 
      right = m-1;
    } else {
      // go right 
      left = m+1;
    }
  }
  return res;
}

int main(void) {
  int n = 7;
  int a1[] = {0,1,2,6,9,11,15};
  int a2[] = {1,2,3,4,6,9,11};
  int a3[] = {0,1,2,3,4,5,6};
  cout  << solve(a1, n) << endl;
  cout  << solve(a2, n) << endl;
  cout  << solve(a3, n) << endl;
  return 0;
}

