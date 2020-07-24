#include <iostream>
#include <string>

bool is_palindrome(const string& a) {
  int n = a.size();
  for (int i=0; i<n; ++i) {
    if (a[i] != a[n-i-1]) {
      return false;
    }
  }
  return true;
}

int main(void) {
  string input = "abcdcba";
  cout << is_palindrome(input) << endl;
  return 0;
}

