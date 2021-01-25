#include <iostream>
using std::cout;
using std::endl;

int pow(int n, int x) {
  if (x == 0) {
    return 1;
  }
  if (x == 1) {
    return n;
  }
  return x & 1 ? pow(n, x/2) * pow(n, x/2) * n :
                 pow(n, x/2) * pow(n, x/2);
}

int main(void) {
  cout << pow(3,7) << endl;
  return 0;
}

