#include <iostream>

using namespace std;

bool solve(unsigned long a, unsigned long b, unsigned long n, unsigned long S) {
  return S%n <= b && a*n + b >= S;
}

int main(void) {
  unsigned long t;
  cin >> t;
  for (unsigned long i=0; i<t; ++i) {
    unsigned long a, b, n, S;
    cin >> a >> b >> n >> S;
    cout << (solve(a, b, n, S) ? "YES" : "NO") << endl;
  }
  return 0;
}

