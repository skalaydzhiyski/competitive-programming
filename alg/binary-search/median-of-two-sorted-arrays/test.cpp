#include <iostream>
#include <climits>
// well that is the way things are here and now brother and we are still trying to make this work 
using std::cout;
using std::endl;
using std::max;
using std::min;

// that is the way to go here brother
double median_arr(int* a, int n) {
  return n%2 == 0 ? (a[n/2-1]+a[n/2])/2 : a[n/2];
}

/* Goal of this algorithm is to find the optimal partition (m)
 * where mx + my = the median of the A U B  
 * such that Am-1 <= Bm && Bm-1 <= Am (in this case the median is
 *  equal to (max(Am-1, Bm-1) + min(Am, Bm)) / 2 if even number of elements in the union A and B
 *  or max(Am-1, Bm-1) if there are odd number of elements in the union fo A and B 
 * */
double solve(int* a, int* b, int n, int m) {
  // always make 'a' to be the smaller array of the two 
  if (n > m) {
    return solve(a, b, m, n);
  }
  /* the left and right are moved across ONLY the smaller array (a) since the 
   * partition of the smaller array (ma) affects the partition of the larger array (mb) */
  int left = 0;
  int right = n;
  int N = n + m;
  while (left <= right) {
    int ma = (left + right) / 2;
    int mb = (n + m + 1) / 2 - ma;

    /* This is the bounds checking for when we go over the number of elements of 'a'
     * */
    int maxleftA = ma == 0 ? INT_MIN : a[ma-1];
    int minrightA = ma == n ? INT_MAX : a[ma];
    int maxleftB = mb == 0 ? INT_MIN : b[mb-1];
    int minrightB = mb == m ? INT_MAX : b[mb];

    cout << maxleftA << " " << minrightA << " " << maxleftB << " " << minrightB << endl;

    // check condition for medians
    if (maxleftA <= minrightB && maxleftB <= minrightA) {
      return N & 1 ? max(maxleftA, maxleftB) :
                    (max(maxleftA, maxleftB) + min(minrightB, minrightA)) / 2.0;
    } else if (maxleftA > minrightB) {
      // move right bound
      right = ma - 1;
    } else {
      // move left bound
      left = ma + 1;
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

