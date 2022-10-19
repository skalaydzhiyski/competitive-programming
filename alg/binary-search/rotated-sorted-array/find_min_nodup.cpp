#include <iostream>
using namespace std;

// WITH NO DUPLICATES
int findmin(int* a, int n) {
  int left = 0;
  int right = n-1;
  int res = INT_MAX;
  while (left <= right) {
    int m = left + (right - left) / 2;
    // array has no rotations 
    if (a[left] < a[right]) {
      return a[left];
    }
    // left side sorted
    if (a[m] < res) {
      res = a[m];
    }
    if (a[m] > a[right]) {
      left = m+1;
    } 
    // right side sorted
    else {
      right = m-1;
    }
  }
  return res;
}

int main(void) {
  int n = 7;
  int a[3][7] = {
    {5,6,0,1,2,3,4},
    {3,4,5,6,7,0,1},
    {7,6,5,4,3,2,1}
  };
  for (int i=0; i<3; ++i) {
    for (auto& c: a[i]) {
      cout << c << " ";
    }
    cout << endl << "min = " << findmin(a[i], n) << endl << endl;
  }
  return 0;
}

