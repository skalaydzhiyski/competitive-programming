#include <iostream>
#include <vector>
using namespace std;

int findfirst(int* a, int n, int t) {
  int left = 0;
  int right = n-1;
  int res = -1;
  while (left <= right) {
    int m = left + (right-left)/2;
    if (a[m] == t) {
      right = m-1;
      res = m;
    } else if (a[m] > t) {
      right = m-1;
    } else {
      left = m+1;
    }
  }
  return res;
}

vector<int> solve(int* a, int n, int t) {
  int first = findfirst(a, n, t);
  int last = findfirst(a, n, t+1);
  return {first, last-1};
}

int main(void) {
  int n = 15;
  int a[] = {1,2,2,3,3,4,4,4,5,5,6,8,8,8,9};
  for (auto& n: a) cout << n << " ";
  cout << endl;
  int t;
  cin >> t;
  vector<int> res = solve(a, n, t);
  for (auto& n: res) cout << n << " ";
  cout << endl;
  return 0;
}

