#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/* Example of hill climbing algorithm */

int solve(const vector<int>& a) {
  int n = a.size();
  vector<int> rewards(n, 1);
  for (int i=1; i<n; ++i) {
    // uphill
    if (a[i] > a[i-1]) {
      rewards[i] = rewards[i-1] + 1;
    } 
  }
  for (int j=n-2; j>=0; --j) {
    if (a[j] > a[j+1]) {
      rewards[j] = max(rewards[j], rewards[j+1]+1);
    }
  }
  // res
  int res = 0;
  for (int n: rewards) res += n;
  return res;
}

int main(void) {
  vector<int> a {8, 4, 2, 1, 3, 6, 7, 9, 5};
  for (int n: a) {
    cout << n << " ";
  }
  cout << endl;
  int res = solve(a);
  cout << res << endl;
  return 0;
}

