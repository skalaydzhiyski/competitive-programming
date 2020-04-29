#include <iostream>
#include <string>
#include <vector>
#include <bitset>
#include <bitset>
#include <algorithm>
#include <random>

using namespace std;

#define N 10

int binsearch(int* a, int t) {
  int left = 0;
  int right = N-1;
  while (left <= right) {
    int m = left + (right - left) / 2;
    if (a[m] < t) {
      left = m+1;
    } else if (a[m] > t) {
      right = m-1;
    } else {
      return m;
    }
  }
  return -1;
}

int main(void) {
  int a[N];
  for (int i=0; i<N; ++i) {
    a[i] = rand() % 10 + 1;
  }
  sort(a, a+N);
  for (auto& n: a) {
    cout << n << " ";
  }
  cout << endl;
  int target;
  cin >> target;
  cout << binsearch(a, target) << endl;
  return 0;
}

