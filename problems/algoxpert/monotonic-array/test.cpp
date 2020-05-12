#include <iostream>
#include <vector>
using namespace std;

bool solve(vector<int>& a) {
  if (a.size() <= 1) {
    return 1;
  }
  bool is_dec = 1;
  bool is_inc = 1;
  for (int i=0; i<a.size()-1; ++i) {
    if (a[i] > a[i+1])
      is_inc = 0;
    if (a[i] < a[i+1])
      is_dec = 0;
  }
  return is_dec | is_inc;
}

int main(void) {
  vector<int> a {-1, -5, -10, -1100, -1100, -1101, -1102, -9001};
  cout << solve(a) << endl;
  return 0;
}

