#include <iostream>
using namespace std;

/* This is a clear example how not always divide and conquer works.
 * In this case, we have no other way around finding the number of negative numbers
 * in a UNSORTED array, since we ultimately need to visit every element to check it.
 * Regardless of whether we use recursion or iteration, the complexity is still O(N).
 * * Note here that iterative solution is faster because we reduce the number of stack operations
 *    the recursive solution is doing for every recursive call.
 * */

int countneg(int* a, int left, int right) {
  cout << "inside call to countneg() with left: " << left << " and right: " << right << endl;
  if (left == right) {
    return a[left] < 0;
  }
  if (left == right-1) {
    return a[left] < 0 || a[right] < 0;
  }
  int m = left + (right-left)/2;
  int count = countneg(a, left, m) + countneg(a, m+1, right);
  return count;
}

int main(void) {
  int n;
  cin >> n;
  int a[n];
  for (int i=0; i<n; ++i) {
    cin >> a[i];
  }
  cout << "iterative" << endl;
  int countops = 0, res=0;
  for (int i=0; i<n; ++i) {
    if (a[i] < 0) {
      res++;
    }
    countops++;
  }
  cout << "divide and conquer" << endl;
  cout << countneg(a, 0, n-1) << endl;
  return 0;
}

