#include <iostream>
using namespace std;

int solve(int* a, int n, int t) {
  int left = 0;
  int right = n-1;
  int res = -1;
  while (left <= right) {
    int m = left + (right-left)/2;
    if (a[m] == t) {
      res = m;
      break;
    } else if (a[m-1] == t) {
      res = m-1;
      break;
    } else if (a[m+1] == t) {
      res = m+1;
      break;
    } else if (a[m] > t) {
      left = m+2;
    } else if (a[m] < t) {
      // go left by 
      right = m-2;
    }
  }
  return res;
}

int main(void) {
  int a[9] = {2,1,3,5,4,7,6,8,9};
  cout << solve(a, 9, 5) << endl;
  cout << solve(a, 9, 10) << endl;
  return 0;
}

