#include <iostream>
#include <vector>
#include <utility>
using namespace std;

vector<int> solve(vector<int>& a) {
  int n = a.size();
  if (a[0] > a[n-1]) return {0, n-1};
  
  a.push_back(INT_MAX);
  vector<int> res;
  // find min and max out of order elements
  int min = INT_MAX;
  int max = INT_MIN;
  for (int i=1; i<n; ++i) {
    if (a[i] > a[i+1] || a[i] < a[i-1]) {
      if (a[i] > max) {
        max = a[i];
      }   
      if (a[i] < min) {
        min = a[i];
      }   
    }   
  }
  // find first occurence of min and max
  int left = 0;
  int right = n-1;
  while (a[left] <= min && left < n-1) {
    left++;
  }
  while (a[right] > max && right > 0) {
    right--;
  }
  res.push_back(left);
  res.push_back(right);
  return res[0] < res[1] ? res : vector<int>{-1, -1};
}


int main(void) {
  vector<int> a {1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19};
  //vector<int> a {1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19};
  //vector<int> a {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,2};

  auto res = solve(a);
  for (auto& n: res) {
    cout << n << " ";
  }
  cout << endl;
  return 0;
}

