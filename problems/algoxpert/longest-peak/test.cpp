#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int solve(const vector<int>& a) {
  int n = a.size();
  if (n < 2) return 0;

  vector<int> peaks;
  for (int i=1; i<n-1; ++i) {
    bool ispeak = a[i]>a[i-1] && a[i]>a[i+1];
    if (ispeak) {
      peaks.push_back(i);
    }
  }
  int max = 0;
  int j;
  for (int i=0; i<peaks.size(); ++i) {
    int count = 1;
    j = peaks[i];
    while (a[j] > a[j-1] && j > 0) {
      count++;
      j--;
    }
    j = peaks[i];
    while (a[j] > a[j+1] && j < n-1) {
      count++;
      j++;
    }
    if (count > max) {
      max = count;
    }
  }
  return max == 1 ? -1 : max;
}

int main(void) {
  vector<int> a {1,2,3,3,4,0,10,6,5,-1,-3,2,3};
  cout << solve(a) << endl;
  return 0;
}

