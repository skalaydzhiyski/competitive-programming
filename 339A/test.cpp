#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cstdio>

int main(void) {
  std::string input;
  std::cin >> input;
  std::replace(input.begin(), input.end(), '+', ' ');
  std::vector<int> nums;
  std::stringstream ss(input);
  int temp, n=0;
  while (ss >> temp) {
    nums.push_back(temp);
    n++;
  }
  std::sort(nums.begin(), nums.end());
  std::string res = "";
  for (const auto& current : nums) {
    res += std::to_string(current);
    res += "+";
  }
  printf("%s", res.substr(0, res.size() - 1).c_str());
  return 0;
}

