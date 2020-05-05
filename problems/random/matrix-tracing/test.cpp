#include <iostream>
#include <vector>
using namespace std;

int step(int i, int j, int m, int n) {
  if (i == m && j == n) {
    // ++ for the count since that is the goal point!
    return 1;
  }
  int res = 0;
  if (i <= m) {
    res += step(i+1, j, m, n);
  }
  if (j <= n) {
    res += step(i, j+1, m, n);
  }
  cout << "returning res: " << res << endl;
  return res;
}

int solve(int m, int n) {
  return step(0, 0, m-1, n-1);
}

int main(void) {
  int m, n;
  cin >> m >> n;
  cout << solve(m, n) << endl;
  return 0;
}

