#include <iostream>
#include <cmath>

using namespace std;

int findpow(long s) {
  int p = 1;
  while (pow(10, p) <= s) { p++; }
  return p-1;
}

long long solve(long s) {
  long long res = 0;
  while (s >= 10) {
    int d = pow(10, findpow(s));
    res += d;
    s = s-d + d/10;
  }
  return res + s;
}

int main(void) {
  int t;
  long s;
  cin >> t;
  for (int i=0; i<t; ++i) {
    cin >> s;
    cout << solve(s) << endl; 
  }
  return 0;
}

