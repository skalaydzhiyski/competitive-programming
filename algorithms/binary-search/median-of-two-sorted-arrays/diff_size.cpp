#include <iostream>
#include <climits>
using namespace std;

double median_arr(int* a, int n) {
  return n%2 == 0 ? (a[n/2-1]+a[n/2])/2 : a[n/2];
}

double solve(int* a, int* b, int x, int y) {
  // always make 'a' to be the smaller array of the two 
  if (x > y) {
    return solve(b, a, y, x);
  }
  int left = 0;
  int right = x;
  int N = x + y;
  while (left <= right) {
    cout << "left: " << left << "\tright: " << right << endl;

    int partX = (left + right) / 2;
    int partY = (x+y+1)/2 - partX;

    cout << "partitions" << endl;
    cout << partX << ": [" << a[partX] << "], " << partY << ": [" << b[partY] << "]" << endl;

    int maxleftX = partX == 0 ? INT_MIN : a[partX-1];
    int minrightX = partX == x ? INT_MAX : a[partX];
    cout << "maxleftX: " << maxleftX << ", " << "minrightX: " << minrightX << endl;

    int maxleftY = partY == 0 ? INT_MIN : b[partY-1];
    int minrightY = partY == y ? INT_MAX : b[partY];
    cout << "maxleftY: " << maxleftY << ", " << "minrightY: " << minrightY << endl;
    cout << endl;

    // check condition for medians
    if (maxleftX <= minrightY && maxleftY <= minrightX) {
      return N & 1 ? max(maxleftX, maxleftY) :
                    (max(maxleftX, maxleftY) + min(minrightY, minrightX)) / 2.0;
    } else if (maxleftX > minrightY) {
      cout << "move right bound" << endl;
      // move left-
      right = partX - 1;
    } else {
      cout << "move left bound" << endl;
      // move right
      left = partX + 1;
    }
  }
  return 0.;
}

int main(void) {
  int m = 5;
  int n = 6;
  int a[] = {1,2,3,4,5};
  int b[] = {22,23,24,25,26,27};
  cout << solve(a, b, m, n) << endl;
  return 0;
}

