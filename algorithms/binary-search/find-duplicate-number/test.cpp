#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int finddup(vector<int>& nums) {
  unordered_map<int, bool> m;
  for (auto& n: nums) {
    if (m[n]) {
      return n;
    }
    m[n] = 1;
  }
  return -1;
}

int main(void) {
  int n, x;
  cin >> n;
  vector<int> nums;
  for (int i=0; i<n; ++i) {
    cin >> x;
    nums.push_back(x);
  }
  cout << finddup(nums) << endl;
  return 0;
}

