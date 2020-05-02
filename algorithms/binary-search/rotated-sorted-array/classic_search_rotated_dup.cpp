#include <iostream>
using namespace std;

// WITH DUPLICATES
int find(int* a, int n, int t) {
  int left = 0;
  int right = n-1;
  while (left <= right) {
    int m = left + (right-left)/2;
    cout << left << " " << right << " " << m << endl;
    if (a[m] == t) {
      return m;
    }
    // left side sorted 
    if (a[m] > a[right]) {
      if (t > a[m] || t < a[left]) {
        left = m+1;
      } else {
        right = m-1;
      }
    }
    else if (a[m] < a[right]) {
      if (t < a[m] || t > a[right]) {
        right = m-1;
      } else {
        left = m+1;
      }
    } else {
      right--;
    }
  }
  return -1;
}

int main(void) {
  int n = 7, t = 1;
  int a[3][7] = {
    {3,3,3,3,0,1,3},
    {3,1,3,3,3,3,3},
    {3,0,1,2,2,2,3}
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

