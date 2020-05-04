#include <iostream>
using namespace std;

int med(int* a, int n) {
  return n%2 == 0 ? (a[n/2-1]+a[n/2])/2 : a[n/2];
}

void print(int* a, int n) {
  for (int i=0; i<n; ++i) {
    cout << a[i] << " ";
  }
  cout << endl;
}

int findmed(int* a, int* b, int n) {
  // base cases
  print(a, n);
  print(b, n);
  if (n == 0) return -1;
  if (n == 1) return (a[0]+b[0])/2;
  if (n == 2) return (max(a[0], b[0]) + min(a[1], b[1]))/2;
  int ma = med(a, n);
  int mb = med(b, n);
  cout << "medians" << endl;
  cout << ma << " " << mb << endl;
  if (ma == mb) return ma;
  // general case
  if (ma < mb) {
    if (n%2 == 0) {
      return findmed(&a[n/2-1], b, n-n/2-1);
    }
    return findmed(&a[n/2], b, n-n/2);
  }
  if (n%2 == 0) {
    return findmed(a, &b[n/2-1], n-n/2-1);
  }
  return findmed(a, &b[n/2], n-n/2);
}

int main(void) {
  int n = 5;
 	int a[] = {1, 12, 15, 26, 38};
  int b[] = {2, 13, 17, 30, 45};
  cout << findmed(a, b, n) << endl;
  return 0;
}

