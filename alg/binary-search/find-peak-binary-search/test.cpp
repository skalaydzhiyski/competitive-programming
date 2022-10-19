#include <iostream>

#define n 11
using namespace std;

int findpeak(int* a) {
  // assumes we don't have repating elements here
  int left = 0;
  int right = n-1;
  int res = -1;
  while (left <= right) {
    int m = left + (right-left)/2;
    if (a[m-1] < a[m] && a[m] < a[m+1]) {
      // increasing -> move right 
      left = m+1;
    } else if (a[m-1] > a[m] && a[m] > a[m+1]) {
      // decreasing -> move left
      right = m-1;
    } else {
      // we have found the peak=
      res = a[m];
      // break since there is no other better peak from the problem statement.
      break;
    }
  }
  return res;
}

int main(void) {
  int a[n] = {2,3,4,6,9,12,11,9,6,4,1};
  for (auto& c: a) {
    cout << c << " ";
  }
  cout << endl;
  cout << findpeak(a) << endl;
  return 0;
}

