#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> arrayOfProducts(vector<int> array) {
  int p = 1;
  for (auto& x: array) {
    cout << x << endl;
    if (x == 0) {
      continue;
    }
    p *= x;
  }
  cout << array.size() << endl;
  vector<int> res; 
  res.reserve(array.size());
  for (int i=0; i<array.size(); ++i) {
    if (array[i] == 0) {
      fill(res.begin(), res.end(), 0);
      res.at(i) = p;
      break;
    }
    res.push_back(p/array[i]);
  }
  return res;
}

int main(void) {
 // vector<int> a {5,1,4,2};
  vector<int> a {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
  auto res = arrayOfProducts(a);
  for (auto& x: res) {
    printf("%d ", x);
  }
  return 0;
}

