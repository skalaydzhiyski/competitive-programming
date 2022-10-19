#include <iostream>
using namespace std;

int solve(int* arr, int n) {
  int left = 0;
  int right = n-1;
  int res = 0;
  while (left <= right) {
    int m = left + (right-left)/2;
    if (arr[m] <= arr[right]) {
      // store res
      res = n-m;
      // find better
      right = m-1;
    } else {
      left = m+1;
    }
  }
  return res != n ? res : 0;
}

static const int n = 6;
int main(void) {
  int a[2] [n]= {
    {8,9,10,2,5,6},
    {2,5,6,8,9,10}
  };
  for (int i=0; i<2; ++i) {
    cout << solve(a[i], n) << endl;
  }
  return 0;
}

