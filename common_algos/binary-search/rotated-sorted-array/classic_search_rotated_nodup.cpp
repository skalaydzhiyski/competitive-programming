#include <iostream>
using namespace std;

int find(int* a, int n, int t) {
  int left = 0;
  int right = n-1;
  while (left <= right) {
    int m = left + (right - left) / 2;
    // check if found! 
    if (a[m] == t) return m;

    // left half is sorted
    if (a[m] > a[left]) {
      if (t > a[m] || t < a[left]) {
        // go right
        left = m+1;
      } else {
        right = m-1;
      }
    }
    // right half is sorted
    else {
      if (t < a[m] || t > a[right]) {
        // go left
        right = m-1;
      } else {
        left = m+1;
      }
    }
  }
  // if 't' is not found in 'a'
  return -1;
}

int main(void) {
  int n = 7, t = 2;
  int a[3][7] = {
    {4,5,6,7,0,1,2},
    {2,4,5,6,7,0,1},
    {4,5,6,0,1,2,3}
  };
  for (int i=0; i<3; ++i) {
    cout << "t = " << t << endl;
    for (auto& c: a[i]) {
      cout << c << " ";
    }
    cout << endl << find(a[i], n, t) << endl << endl;
  }
  return 0;
}

