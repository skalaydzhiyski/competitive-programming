#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string solve(int n) {
  if (n == 1) {
    return "-1";
  }
  // get all digits 
  string res = "2";
  for (int i=0; i<n-1; ++i) {
    res += "3";
  }
  return res;
}

int main(void) {
  int t, n;
  scanf("%d", &t);
  for (int i=0; i<t; ++i) {
    scanf("%d", &n);
    cout << solve(n) << endl;
  }
  return 0;
}

