#include <iostream>
using namespace std;

/* TODO: Investigate the importance of the fact that after splitting 
 * the array, one of the halves is ALWAYS sorted !
 * */

int find(int* a, int n, int t) {
  int left = 0;
  int right = n-1;
  while (left <= right) {
    // one of the halfs is always sorted 
    int m = left + (right - left) / 2;
    // here we need to find in what of the two halves is 't'
    if (a[m] == t) {
      return m;
    }
    // left half is sorted
    if (a[left] <= a[m]) {
      // if t is bigger than middle or is in the rotated side 
      if (t > a[m] || t < a[left]) {
        // search in right half
        left = m+1;
      } else {
        // search in left half
        right = m-1;
      }
    } 
    // right half is sorted
    else {
      // t is smaller than the right side or s bigger than rotated side (which is sorted)
      if (t < a[m] || t > a[right]) {
        // search in left half
        right = m-1;
      } else {
        // search in right half
        left = m+1;
      }
    }
  }
  // if 't' is not found in 'a'
  return -1;
}

int main(void) {
  int n = 7, t = 5;
  int a[3][7] = {
    {4,5,6,7,0,1,2},
    {2,4,5,6,7,0,1},
    {5,6,7,0,1,2,4}
  };
  for (int i=0; i<3; ++i) {
    cout << "t = " << t << endl;
    for (auto& c: a[i]) {
      cout << c << " ";
    }
    cout << endl << find(a[i], n, t) << endl;
  }
  return 0;
}

