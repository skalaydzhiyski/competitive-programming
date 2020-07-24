#include <iostream>
#include <string>
using namespace std;

string solve(const string& str, int key) {
  int n = str.size();
  string res = "";
  for (int i=0; i<n; ++i) {
    int idx = ((int) (str[i]-97 + key) % 26);
    res += (char) (97 + idx);
  }
  return res;
}

int main(void) {
  string a = "xyz";
  int k = 2;
  string res = solve(a, k);
  cout <<  res << endl;
  return 0;
}

