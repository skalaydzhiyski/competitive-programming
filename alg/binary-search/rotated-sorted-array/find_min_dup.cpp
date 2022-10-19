#include <iostream>
using namespace std;

// WITH DUPLICATES !
int findmin(int* a, int n) {
  int left = 0;
  int right = n-1;
  if (a[left] < a[right]) {
    return a[left];
  }
  int res = INT_MAX;
  while (left <= right) {
    int m = left + (right - left) / 2;
    if (a[m] > a[right]) {
      res = min(res, a[m]);
      left = m+1;
    } 
    else if (a[m] < a[right]) {
      res = min(res, a[m]);
      right = m;
    } else {
      res = a[m];
      right--;
    }
  }
  return a[left];
}

int main(void) {
  int n = 7;
  int a[3][7] = {
    {3,3,3,3,0,1,3},
    {3,1,3,3,3,3,3},
    {3,0,1,2,2,2,3}
  };
  for (int i=0; i<3; ++i) {
    for (auto& c: a[i]) {
      cout << c << " ";
    }
    cout << endl << "min = " << findmin(a[i], n) << endl << endl;
  }
  return 0;
}

